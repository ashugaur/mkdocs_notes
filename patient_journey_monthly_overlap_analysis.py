#%% Patient journey using roadmapper

"""
objective: 
source: https://github.com/csgoh/roadmapper/wiki/Usage-Documentation, https://github.com/csgoh/roadmapper, https://github.com/csgoh/roadmapper/wiki/Gallery
description: 

data_dictionary
"""

# load functions
exec(open(r"C:\my disk\edupunk\automation\control\py functions\run_all_py_files_in_a_folder.py").read())

#working_dir(r'C:\my disk\edupunk\metadata\data')
#working_dir(r'C:\my disk\____tmp')
#working_dir(r'C:\my disk\courses\ipba\data')
working_dir(r'C:\my disk\edupunk\automation\visual library\journey')

import pandas as pd
from roadmapper.roadmap import Roadmap
from roadmapper.timelinemode import TimelineMode
import subprocess as sp
from datetime import datetime
import pyperclip
import random
from faker import Faker
fake = Faker()
from datetime import datetime, timedelta
import timeit
import random
import numpy as np


#%% create simulated dataset

# simulation

def simulate_patient_records(nbr_of_patients_):

    # print('\ngenerating simulated data...')
    start_time = timeit.default_timer()

    #generates range of list starting from 0 and allocates weight to it
    def weight_list(value):
        weights = [x for x in range(0, value)]
        weights_sum = sum(weights)
        weights = [w/weights_sum for w in weights]
        weights.sort(reverse=True)
        return weights

    _ndcs = pd.DataFrame({'sn':[1,2,3,4,5,6,7],
                        'ndc':[1,2,3,4,5,6,7],
                        'group':['oad','dpp','sglt','glp','basal','bolus','premix']})
    ndcs = {k: g["ndc"].tolist() for k, g in _ndcs.groupby("sn")}


    df = pd.DataFrame()
    nbr_of_patients = nbr_of_patients_
    itr, total_records = 0, 0
    for k in range(0, nbr_of_patients):
        
        itr+=1

        # fixed fields
        patient_idx = random.randint(20000, 99999)
        sd = fake.date_between(start_date='-1y', end_date='-1y') #start date for patient record
        ed = fake.date_between(start_date=sd+timedelta(days=random.randint(10,200)), end_date='-3m')
        individual_records = int(((ed-sd).days) / 45)+1
        total_records += individual_records

        sndc = random.choice(list(ndcs.keys())[:7]) #start group of ndc

        for i in range(0, individual_records):

            # unique fields
            quantityx = random.choice([15, 30, 45, 60, 75, 90])

            # interdependent fields
            if i == 0:
                service_datex = sd
                ndcx = random.choice(ndcs.get(sndc))
                days_supplyx = random.choice([15, 30, 45, 60, 75, 90])
            elif 0 > i <= 3:
                days_supplyw = weight_list(days_supplyx)
                #next days supply to be probabilistically close to previous for rv, rj claims
                service_datex = service_datex+timedelta(days=int(''.join(str(x) for x in random.choices(range(0, days_supplyx), days_supplyw))))
                ndcx = random.choice(ndcs.get(sndc))
                days_supplyx = random.choice([15, 30, 45, 60, 75, 90])
            else:
                service_datex = service_datex+timedelta(days=days_supplyx)
                ndcx = random.choice(ndcs.get(sndc))
                days_supplyx = random.choice([30, 45, 60, 90])

            tmp_dict = {'patient_id'                : [patient_idx],
                        'ndc'                       : [ndcx],
                        'service_date'              : [service_datex],
                        'days_supply'               : [days_supplyx]}
        
            tmp_line = pd.DataFrame(tmp_dict)
            
            df = pd.concat([df, tmp_line])

    df = df.reset_index(drop=True)
    df = pd.merge(df, _ndcs[['ndc', 'group']], how='left')
    del df['ndc']
    df=df.reset_index(drop=True)

    #s1='\n total records generated: '+ str(total_records) + ' for '+ str(nbr_of_patients) + ' patients'
    #print(s1+'\n'+'-'*len(s1))
    elapsed = timeit.default_timer() - start_time
    print('\nnote: time taken to simulate data', elapsed)

    return df

# run simulation
p1 = simulate_patient_records(10)
p1['patient_id']='p1'
p2 = simulate_patient_records(5)
p2['patient_id']='p2'

df = pd.concat([p1,p2]).reset_index(drop=True)


#%% overlaps

#dedup
df = df.drop_duplicates()

#sort
df = df.sort_values(['patient_id', 'group', 'service_date']).reset_index(drop=True)

#next ds
df['service_date_next'] = df['service_date'] + pd.to_timedelta(df['days_supply'], unit='d')
df['service_date_lag1'] = df.groupby(['patient_id', 'group'])['service_date'].shift(-1)
df['overlap'] = df['service_date_next'] - df['service_date_lag1']
df['overlap'] = pd.to_timedelta(df['overlap'].fillna(0), errors="ignore").dt.days


# if there is no overlap
create_nbr_of_overlaps = 3
overlap_records=[]

if pd.to_timedelta(df['overlap'].fillna(0), errors="ignore").max().days == 0:

    for i in range(0, create_nbr_of_overlaps):
        rec = random.randint(0,(len(df)))
        overlap_records.append(rec)
    overlap_records.sort()

    for i in overlap_records:
        df.loc[i, 'days_supply'] = df.loc[i, 'days_supply']+random.randint(0,5)

    #dedup
    df = df.drop_duplicates()

    #sort
    df = df.sort_values(['patient_id', 'group', 'service_date']).reset_index(drop=True)

    #next ds
    df['service_date_next'] = df['service_date'] + pd.to_timedelta(df['days_supply'], unit='d')
    df['service_date_lag1'] = df.groupby(['patient_id', 'group'])['service_date'].shift(-1)
    df['overlap'] = df['service_date_next'] - df['service_date_lag1']
    df['overlap'] = pd.to_timedelta(df['overlap'].fillna(0), errors="ignore").dt.days

# clean
df['service_date_lag1'] = np.where(df['service_date_lag1'].isnull(), df['service_date_next'], df['service_date_lag1'])


#%% write roadmap script

def visualize_patient_roadmap(df, _width, _height, _title):

    now = datetime.now()
    file_dt = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day) + '_' + '{:02d}'.format(now.hour) + '{:02d}'.format(now.minute) + '{:02d}'.format(now.second)
    output = 'patient_journey_monthly_generated_'+file_dt+'.png'

    _start_dt = df['service_date'].min().strftime("%Y-%m-%d")
    _number_of_items = round((pd.to_timedelta(df['service_date'].max() - df['service_date'].min()).days/30)+1)


    # roadmap_statement
    rs = ''
    pat_loop = df['patient_id'].drop_duplicates().to_list()
    for i in range(0, len(df)):
        if i==0:
            rs = rs+'roadmap = Roadmap({0}, {1}, colour_theme="BLUEMOUNTAIN", show_marker=False)\n'.format(_width, _height)
            rs = rs+'roadmap.set_title("{}")\n'.format(_title)
            rs = rs+'roadmap.set_timeline(TimelineMode.MONTHLY, start="{0}", number_of_items={1})'.format(_start_dt, _number_of_items)

    for i in pat_loop:

        dfx=df[df['patient_id']==i].reset_index(drop=True)

        rs = rs+'\n\ngroup = roadmap.add_group("{}")\n'.format(i)

        _l = dfx['group'].drop_duplicates().to_list()

        for j in _l:
            dfy = dfx[dfx['group']==j].reset_index(drop=True)
            for w in range(0, len(dfy)):
                _sd = dfy.loc[w,'service_date'].strftime("%Y-%m-%d")
                _ed = dfy.loc[w,'service_date_next'].strftime("%Y-%m-%d")
                if ((w==0) & (dfy.loc[w,'overlap'] == 0)):
                    rs = rs+'\ntask = group.add_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                elif ((w==0) & (dfy.loc[w,'overlap'] != 0)):
                    rs = rs+'\ntask = group.add_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)
                elif (dfy.loc[w,'overlap'] >= 0):
                    rs = rs+'parellel_task = task.add_parallel_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                elif (dfy.loc[w,'overlap'] < 0):
                    rs = rs+'parellel_task = task.add_parallel_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)

    rs = rs+'\nroadmap.draw()\n'

    # read & copy to clipboard
    rs = rs+'roadmap.save(output)\n'

    #print(rs)
    pyperclip.copy(rs)

    # execute
    exec(rs)

    # open
    sp.Popen('explorer ' + '"' + output + '"')


visualize_patient_roadmap(df, 2000, 500, 'Hello')

#df.to_clipboard()



#%% manual

df = pd.read_excel(r"C:\my disk\edupunk\automation\visual library\journey\patient_journey_monthly_overlap_analysis_manual_input.xlsx", sheet_name="output")

visualize_patient_roadmap(df, 2000, 500, 'Hello')




#%% write roadmap script: actual vs calculated

""" 
_width=1400
_height=400
_title="hello"
 """
def visualize_patient_roadmap(df, _width, _height, _title):

    df1, df2 = df.copy(), df.copy()
    df1['patient_id']=df1['patient_id']+'_actual'
    df2['patient_id']=df2['patient_id']+'_calculated'
    df=pd.concat([df1, df2])

    now = datetime.now()
    file_dt = '{:02d}'.format(now.year) + '{:02d}'.format(now.month) + '{:02d}'.format(now.day) + '_' + '{:02d}'.format(now.hour) + '{:02d}'.format(now.minute) + '{:02d}'.format(now.second)
    output = 'patient_journey_monthly_generated_'+file_dt+'.png'

    _start_dt = df['service_date'].min().strftime("%Y-%m-%d")
    _number_of_items = round((pd.to_timedelta(df['service_date'].max() - df['service_date'].min()).days/30)+1)


    # roadmap_statement
    rs = ''
    pat_loop = df['patient_id'].drop_duplicates().to_list()
    for i in range(0, len(df)):
        if i==0:
            rs = rs+'roadmap = Roadmap({0}, {1}, colour_theme="BLUEMOUNTAIN", show_marker=False)\n'.format(_width, _height)
            rs = rs+'roadmap.set_title("{}")\n'.format(_title)
            rs = rs+'roadmap.set_timeline(TimelineMode.MONTHLY, start="{0}", number_of_items={1})'.format(_start_dt, _number_of_items)

    for i in pat_loop:
        dfx=df[df['patient_id']==i].reset_index(drop=True)

        if '_calculated' in dfx['patient_id'].drop_duplicates()[0]:
            rs = rs+'\n\ngroup = roadmap.add_group("{}")\n'.format(i)
            _l = dfx['group'].drop_duplicates().to_list()

            for j in _l:
                dfy = dfx[dfx['group']==j].reset_index(drop=True)
                for w in range(0, len(dfy)):
                    _sd = dfy.loc[w,'service_date'].strftime("%Y-%m-%d")
                    _ed = dfy.loc[w,'service_date_next'].strftime("%Y-%m-%d")
                    if ((w==0) & (dfy.loc[w,'overlap'] == 0)):
                        rs = rs+'\ntask = group.add_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                    elif ((w==0) & (dfy.loc[w,'overlap'] != 0)):
                        rs = rs+'\ntask = group.add_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)
                    elif (dfy.loc[w,'overlap'] >= 0):
                        rs = rs+'parellel_task = task.add_parallel_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                    elif (dfy.loc[w,'overlap'] < 0):
                        rs = rs+'parellel_task = task.add_parallel_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)

        else:
            rs = rs+'\n\ngroup = roadmap.add_group("{}")\n'.format(i)
            _l = dfx['group'].drop_duplicates().to_list()

            for j in _l:
                dfy = dfx[dfx['group']==j].reset_index(drop=True)
                for w in range(0, len(dfy)):
                    _sd = dfy.loc[w,'service_date'].strftime("%Y-%m-%d")
                    _ed = dfy.loc[w,'service_date_lag1'].strftime("%Y-%m-%d")
                    if ((w==0) & (dfy.loc[w,'overlap'] == 0)):
                        rs = rs+'\ntask = group.add_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                    elif ((w==0) & (dfy.loc[w,'overlap'] != 0)):
                        rs = rs+'\ntask = group.add_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)
                    elif (dfy.loc[w,'overlap'] >= 0):
                        rs = rs+'parellel_task = task.add_parallel_task("{0}", "{1}", "{2}")\n'.format(j, _sd, _ed)
                    elif (dfy.loc[w,'overlap'] < 0):
                        rs = rs+'parellel_task = task.add_parallel_task("", "{0}", "{1}", fill_colour="red")\n'.format(_sd, _ed)

    rs = rs+'\nroadmap.draw()\n'

    # read & copy to clipboard
    rs = rs+'roadmap.save(output)\n'

    #print(rs)
    pyperclip.copy(rs)

    # execute
    exec(rs)

    # open
    sp.Popen('explorer ' + '"' + output + '"')


#%% manual

df = pd.read_excel(r"C:\my disk\edupunk\automation\visual library\journey\patient_journey_monthly_overlap_analysis_manual_input.xlsx", sheet_name="output")

visualize_patient_roadmap(df, 2000, 500, 'Hello')
