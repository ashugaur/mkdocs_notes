import pandas as pd
import os

## 웃 data pull

path = _analytics.replace('\\', '/') + '/'
os.chdir(path)

_file = path+r"compare_2_dataframes.xlsx"

df1 = pd.read_excel(_file, sheet_name='Sheet1', na_values=['NA'], usecols='B:I', skiprows=range(1))
df1

df2 = pd.read_excel(_file, sheet_name='Sheet2')
df2


## compare
def compare_dataframes(df1, df2):
    # Check if column names are the same
    if set(df1.columns) != set(df2.columns):
        print("Column names are different.")
        return

    # Check if there are any differences
    if df1.equals(df2):
        print("Dataframes are identical.")
        return
    else:
        # Identify differences
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        differences = pd.concat([df1[diff_mask], df2[diff_mask]], keys=['df1', 'df2'])
        print("WARNING: Differences found.")
        #print(differences)

        return differences

compare_dataframes(df1, df2)


### check and match both data schemas
table1 = 'df1' # alias for df1
table2 = 'df2' # alias for df2

## compare metadata_summary
def metadata_summary(df1, df2):
    global merged_metadata; global nonmatching_fields; global merged_metadata_summary
    merged_metadata = pd.merge(pd.DataFrame(df1.dtypes).reset_index(), \
                           pd.DataFrame(df2.dtypes).reset_index(), how='outer', \
                           indicator=True).rename(columns={'index': 'column', \
                           0: 'format'})[['column', 'format', '_merge']]
    merged_metadata['_merge'] = merged_metadata['_merge'].map({'left_only': table1, \
                           'right_only': table2, 'both': 'both'})
    merged_metadata_summary = pd.DataFrame(merged_metadata['_merge'].value_counts()). \
                            reset_index().rename(columns={'_merge': 'table', 'column': 'column count'})
    merged_metadata_summary = merged_metadata_summary.sort_values('table')
    nonmatching_fields = merged_metadata[~(merged_metadata['_merge'] == 'both')]

metadata_summary(df1, df2)

# explore
merged_metadata
nonmatching_fields
merged_metadata_summary


## 웃 modify datasets as neceassary

# rename columns
def rename_columns(column_name_1st_table, column_name_2nd_table):
    df1[column_name_1st_table + '_re'] = df1[column_name_1st_table]
    del df1[column_name_1st_table]
    df2[column_name_1st_table + '_re'] = df2[column_name_2nd_table]
    del df2[column_name_2nd_table]

#('column-name-in-first-table', 'column-name-in-second-table')
rename_columns('F', 'G')

# convert to numeric
#df1['d'] = pd.to_numeric(df1['d'], errors='coerce')

# convert to datetime
#df1['dt1'] = pd.to_datetime(df1['dt1']).dt.normalize()
#df2['dt1'] = pd.to_datetime(df2['dt1']).dt.normalize()

# replace missing values with nan
#df1 = df1.replace(r' ', np.nan)
#df2 = df2.replace(r' ', np.nan)

# round off all numeric columns
#df1 = df1.round(1)
#df2 = df2.round(1)

# format all character columns to lower
#df1 = df1.apply(lambda x: x.str.lower() if(x.dtype == 'object') else x)
#df2 = df2.apply(lambda x: x.str.lower() if(x.dtype == 'object') else x)

# remove leading/training blanks from all character columns
#df1 = df1.apply(lambda x: x.str.strip() if(x.dtype == 'object') else x)
#df2 = df2.apply(lambda x: x.str.strip() if(x.dtype == 'object') else x)


## compare metadata_summary again
metadata_summary(df1, df2)

# explore
merged_metadata
nonmatching_fields
merged_metadata_summary

### compare again
comparison = compare_dataframes(df1, df2)

# records where row entries do not match
comparison[comparison.isnull().sum(axis=1) != len(comparison.columns)]

