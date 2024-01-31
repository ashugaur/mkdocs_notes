#%% v1

import pandas as pd
from io import StringIO

# Your data
data_str = """
| size   | animals_in_zoo                          |
|:-------|:----------------------------------------|
| big    | tiger + bear + crocodile                |
| big    | tiger + bear + crocodile + crane        |
| big    | tiger + bear + crocodile + crane + tuna |
| big    | lions                                    |
| big    | tuna                                    |
| big    | crane                                   |
| medium | leopard + platpus                       |
| medium | leopard                                 |
| medium | leopard + platpus + pigeon              |
| medium | leopard + platpus + pigeon + mullett    |
| medium | mullett                                 |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    return ' + '.join(mapping_df[mapping_df['animal'].isin(animal_list)]['category'])

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(x.split(' + ')))

# Print the result
print(data_df[['size', 'animals_in_zoo', 'category']])



#%% v2

import pandas as pd
from io import StringIO

# Your data
data_str = """
| size   | animals_in_zoo                          |
|:-------|:----------------------------------------|
| big    | tiger + bear + crocodile                |
| big    | tiger + bear + crocodile + crane        |
| big    | tiger + bear + crocodile + crane + tuna |
| big    | lion                                    |
| big    | tuna                                    |
| big    | crane                                   |
| medium | leopard + platpus                       |
| medium | leopard                                 |
| medium | leopard + platpus + pigeon              |
| medium | leopard + platpus + pigeon + mullett    |
| medium | mullett                                 |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    category_list = mapping_df[mapping_df['animal'].isin(animal_list)]['category'].tolist()
    if len(category_list) == len(animal_list):
        return ' + '.join(category_list)
    else:
        return None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(x.split(' + ')))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['category'].isnull().astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v3

import pandas as pd
from io import StringIO
import re

# Your data
data_str = """
| size   | animals_in_zoo                                 |
|:-------|:-----------------------------------------------|
| big    | tiger + bear + crocodile                       |
| big    | tiger + bear + crocodile + crane               |
| big    | tiger + bear + crocodile + crane + tuna        |
| big    | lion                                           |
| big    | tuna                                           |
| big    | crane                                          |
| medium | leopard + platpus                              |
| medium | leopard                                        |
| medium | leopard + platpus + pigeon                     |
| medium | leopard + platpus + pigeon + mullett           |
| medium | mullett                                        |
| big    | tiger + bear + crocodile + crane + tuna + lion |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    category_list = mapping_df[mapping_df['animal'].isin(animal_list)]['category'].tolist()
    if len(category_list) == len(animal_list):
        return ' + '.join(category_list)
    else:
        return None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['category'].isnull().astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v4

import pandas as pd
from io import StringIO
import re

# Your data
data_str = """
| size   | animals_in_zoo                                 |
|:-------|:-----------------------------------------------|
| big    | tiger + bear + crocodile                       |
| big    | tiger + bear + crocodile + crane               |
| big    | tiger + bear + crocodile + crane + tuna        |
| big    | lion                                           |
| big    | tuna                                           |
| big    | crane                                          |
| medium | leopard + platpus                              |
| medium | leopard                                        |
| medium | leopard + platpus + pigeon                     |
| medium | leopard + platpus + pigeon + mullett           |
| medium | mullett                                        |
| big    | tiger + bear + crocodile + crane + tuna + lion |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    category_list = mapping_df[mapping_df['animal'].isin(animal_list)]['category'].tolist()
    unique_categories = sorted(set(category_list), key=category_list.index)
    return ' + '.join(unique_categories)

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['category'].isnull().astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v5

import pandas as pd
from io import StringIO
import re

# Your data
data_str = """
| size   | animals_in_zoo                                 |
|:-------|:-----------------------------------------------|
| big    | tiger + lion + leopard + bear                  |
| medium | leopard + platpus + pigeon + crocodile         |
| big    | tiger + bear + crocodile                       |
| big    | tiger + bear + crocodile + crane               |
| big    | tiger + bear + crocodile + crane + tuna        |
| big    | lion                                           |
| big    | tuna                                           |
| big    | crane                                          |
| medium | leopard + platpus                              |
| medium | leopard                                        |
| medium | leopard + platpus + pigeon                     |
| medium | leopard + platpus + pigeon + mullett           |
| medium | mullett                                        |
| big    | tiger + bear + crocodile + crane + tuna + lion |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    category_list = mapping_df[mapping_df['animal'].isin(animal_list)]['category'].tolist()
    unique_categories = sorted(set(category_list), key=category_list.index)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = (data_df['category'].isnull() & ~data_df['animals_in_zoo'].str.strip().eq('')).astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])



#%% v6

import pandas as pd
from io import StringIO
import re

# Your data
data_str = """
| size   | animals_in_zoo                                 |
|:-------|:-----------------------------------------------|
| big    | tiger + lion + leopard + bear                  |
| medium | leopard + platpus + pigeon + crocodile         |
| big    | tiger + bear + crocodile                       |
| big    | tiger + bear + crocodile + crane               |
| big    | tiger + bear + crocodile + crane + tuna        |
| big    | lion                                           |
| big    | tuna                                           |
| big    | crane                                          |
| medium | leopard + platpus                              |
| medium | leopard                                        |
| medium | leopard + platpus + pigeon                     |
| medium | leopard + platpus + pigeon + mullett           |
| medium | mullett                                        |
| big    | tiger + bear + crocodile + crane + tuna + lion |
"""

# Your mapping file
mapping_str = """
| animal    | category   |
|:----------|:-----------|
| tiger     | mammal     |
| bear      | omnivore   |
| crocodile | amphibian  |
| pigeon    | bird       |
| crane     | bird       |
| tuna      | fish       |
| lion      | mammal     |
| leopard   | mammal     |
| platpus   | amphibian  |
| mullett   | fish       |
"""

# Convert the string data to pandas DataFrames
data_df = pd.read_csv(StringIO(data_str), sep=r'\s*\|\s*', engine='python')
mapping_df = pd.read_csv(StringIO(mapping_str), sep=r'\s*\|\s*', engine='python')

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    category_list = mapping_df[mapping_df['animal'].isin(animal_list)]['category'].tolist()
    unique_categories = []
    for animal in animal_list:
        category = next((cat for cat in category_list if mapping_df.at[mapping_df['animal'].eq(animal).idxmax(), 'category'] == cat), None)
        if category:
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = (data_df['category'].isnull() & ~data_df['animals_in_zoo'].str.strip().eq('')).astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v7

import pandas as pd
import re

# Your data
data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'big'}, 'animals_in_zoo': {0: 'tigers + lion + leopard + bear', 1: 'leopard + platpus + pigeon + crocodile', 2: 'crocodile + tiger + bear + platpus', 3: 'tiger + bear + crocodile + crane', 4: 'tiger + bear + crocodile + crane + tuna', 5: 'lion', 6: 'tunas', 7: 'crane', 8: 'leopard + platpus', 9: 'leopard', 10: 'leopard + platpus + pigeon', 11: 'leopard + platpus + pigeon + mullett', 12: 'mullett', 13: 'tiger + bear + crocodile + crane + tuna + lion'}})

mapping_df = pd.DataFrame({'animal': {0: 'crocodile', 1: 'platpus', 2: 'pigeon', 3: 'crane', 4: 'tuna', 5: 'mullett', 6: 'tiger', 7: 'lion', 8: 'leopard', 9: 'bear'}, 'category': {0: 'amphibian', 1: 'amphibian', 2: 'bird', 3: 'bird', 4: 'fish', 5: 'fish', 6: 'mammal', 7: 'mammal', 8: 'mammal', 9: 'omnivore'}})


# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        matching_rows = mapping_df[mapping_df['animal'].eq(animal)]
        if not matching_rows.empty:
            category = matching_rows.iloc[0]['category']
            if category not in seen_categories:
                seen_categories.add(category)
                unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None


# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = (data_df['category'].isnull() & ~data_df['animals_in_zoo'].str.strip().eq('')).astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v8

import pandas as pd
import re

# Your data
data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'big'}, 'animals_in_zoo': {0: 'tigers + lion + leopard + bear', 1: 'leopard + platpus + pigeon + crocodile', 2: 'crocodile + tiger + bear + platpus', 3: 'tiger + bear + crocodile + crane', 4: 'tiger + bear + crocodile + crane + tuna', 5: 'lion', 6: 'tunas', 7: 'crane', 8: 'leopard + platpus', 9: 'leopard', 10: 'leopard + platpus + pigeon', 11: 'leopard + platpus + pigeon + mullett', 12: 'mullett', 13: 'tiger + bear + crocodile + crane + tuna + lion'}})

mapping_df = pd.DataFrame({'animal': {0: 'crocodile', 1: 'platpus', 2: 'pigeon', 3: 'crane', 4: 'tuna', 5: 'mullett', 6: 'tiger', 7: 'lion', 8: 'leopard', 9: 'bear'}, 'category': {0: 'amphibian', 1: 'amphibian', 2: 'bird', 3: 'bird', 4: 'fish', 5: 'fish', 6: 'mammal', 7: 'mammal', 8: 'mammal', 9: 'omnivore'}})

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        matching_rows = mapping_df[mapping_df['animal'].eq(animal)]
        if not matching_rows.empty:
            category = matching_rows.iloc[0]['category']
            if category not in seen_categories:
                seen_categories.add(category)
                unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', x)))

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['category'].isnull()]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = (data_df['category'].isnull() & ~data_df['animals_in_zoo'].str.strip().eq('')).astype(int)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v9: stable but with dataframe lookup

import pandas as pd
import numpy as np
import re

# Your data
data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}})

mapping_df = pd.DataFrame({'animal': {0: 'crocodile', 1: 'platpus', 2: 'pigeon', 3: 'crane', 4: 'tuna', 5: 'mullett', 6: 'tiger', 7: 'lion', 8: 'leopard', 9: 'bear'}, 'category': {0: 'amphibian', 1: 'amphibian', 2: 'bird', 3: 'bird', 4: 'fish', 5: 'fish', 6: 'mammal', 7: 'mammal', 8: 'mammal', 9: 'omnivore'}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_df['animal'].values for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if isinstance(x, str) and any(animal not in mapping_df['animal'].values for animal in re.split(r'\s*\+\s*', x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        matching_rows = mapping_df[mapping_df['animal'].eq(animal)]
        if not matching_rows.empty:
            category = matching_rows.iloc[0]['category']
            if category not in seen_categories:
                seen_categories.add(category)
                unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if pd.notna(x) else []))

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if pd.notna(x) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v10: stable with dictionary mapping

import pandas as pd
import numpy as np
import re

# Your data
data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if (isinstance(x, str)) else []))

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v11

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})




#%% v12

import pandas as pd
import numpy as np
import re

# Your data
data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if (isinstance(x, str)) else []))

# Perform the lookup against 'category_group' in mapping_df
def lookup_category_group(row):
    size = row['size']
    category = row['category']
    
    if pd.isna(category):
        return None
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        if set(re.split(r'\s*\+\s*', category)) == category_group:
            return mapping_row['category_group']
    
    return 'unknown'

# Apply the lookup to create a new 'category_group' column in the original data
data_df['category_group'] = data_df.apply(lookup_category_group, axis=1)

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v13

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if (isinstance(x, str)) else []))

# Function to look up the category_group_ordered for each row in data_df
def lookup_category_group(row):
    size_match = mapping_df['size'] == row['size']
    for idx, group in mapping_df[size_match].iterrows():
        categories = set(re.split(r'\s*\+\s*', str(row['category'])))
        group_categories = set(re.split(r'\s*\+\s*', group['category_group_ordered']))
        if categories.issubset(group_categories):
            return group['category_group_ordered'], group['category_order']
    return 'not found', np.nan

# Apply the function to create new 'category_group_ordered' and 'category_order' columns in the original data
data_df[['category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% V14

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if (isinstance(x, str)) else []))

# Function to look up the category_group_ordered for each row in data_df
def lookup_category_group(row):
    size_match = mapping_df['size'] == row['size']
    for idx, group in mapping_df[size_match].iterrows():
        categories = set(re.split(r'\s*\+\s*', str(row['category'])))
        group_categories = set(re.split(r'\s*\+\s*', group['category_group_ordered']))
        if categories.issubset(group_categories):
            return group['category_group'], group['category_group_ordered'], group['category_order']
    return 'not found', np.nan, 'not found'

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
data_df[['category_group', 'category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v15

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df['animals_in_zoo'].apply(lambda x: get_category(re.split(r'\s*\+\s*', str(x)) if (isinstance(x, str)) else []))

# Perform the lookup against 'category_group' in mapping_df
def lookup_category_group(row):
    size = row['size']
    category = row['category']
    
    if pd.isna(category):
        return None
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        if set(re.split(r'\s*\+\s*', category)) == category_group:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order']
    
    return 'unknown', np.nan, 'not found'

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
data_df[['category_group', 'category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v16

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['no_match_flag'] == 1]

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    size = row['size']
    category = row['category']
    
    if row['no_match_flag'] == 1 or pd.isna(category):
        return 'unknown', 'complete new', 7
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        if set(re.split(r'\s*\+\s*', category)) == category_group:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order']
    
    return 'unknown', 'complete new', 7

data_df[['category_group', 'category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v17

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    size = row['size']
    category = row['category']
    
    if row['no_match_flag'] == 1 or pd.isna(category):
        return None, None, None
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        if set(re.split(r'\s*\+\s*', category)) == category_group:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order']
    
    return None, None, None

data_df[['category_group', 'category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v18

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus + np.nan  + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan}, 'no_match_flag': {0: 1, 1: 0, 2: 1, 3: 1, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 1, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0, 16: 0, 17: 1, 18: 1}, 'category': {0: 'mammal', 1: 'mammal + amphibian + bird', 2: 'mammal + bird + amphibian', 3: 'mammal + amphibian', 4: 'amphibian', 5: 'amphibian + mammal + omnivore', 6: 'mammal + omnivore + amphibian + bird', 7: 'mammal + omnivore + amphibian + bird + fish', 8: 'mammal', 9: None, 10: 'bird', 11: 'mammal + amphibian', 12: 'mammal', 13: 'mammal + amphibian + bird', 14: 'mammal + amphibian + bird + fish', 15: 'fish', 16: 'mammal + omnivore + amphibian + bird + fish', 17: None, 18: None}, 'animals_in_zoo_word_count': {0: 4, 1: 4, 2: 3, 3: 5, 4: 4, 5: 4, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 6, 17: 0, 18: 0}, 'category_word_count': {0: 1, 1: 3, 2: 3, 3: 2, 4: 1, 5: 3, 6: 4, 7: 5, 8: 1, 9: 1, 10: 1, 11: 2, 12: 1, 13: 3, 14: 4, 15: 1, 16: 5, 17: 1, 18: 1}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'medium', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium'}, 'category_group': {0: 'fish + amphibian + mammal + bird', 1: 'mammal + bird + amphibian', 2: 'mammal + amphibian', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'unknown', 7: 'fish + amphibian + mammal + bird', 8: 'mammal + bird + amphibian', 9: 'mammal + amphibian', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'unknown'}, 'category_group_ordered': {0: 'fish + amphibian + mammal + bird', 1: 'amphibian + mammal + bird', 2: 'amphibian + mammal', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'complete new', 7: 'fish + amphibian + mammal + bird', 8: 'amphibian + mammal + bird', 9: 'amphibian + mammal', 10: 'mammal', 11: 'fish', 12: 'bird', 13: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 1, 8: 2, 9: 3, 10: 4, 11: 5, 12: 6, 13: 7}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    size = row['size']
    category = row['category']
    
    if row['no_match_flag'] == 1 or pd.isna(category):
        return 'unknown', 'complete new', 7
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        if set(re.split(r'\s*\+\s*', category)) == category_group:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order']
    
    return 'unknown', 'complete new', 7

data_df[['category_group', 'category_group_ordered', 'category_order']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v19: looks stable

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'category_group': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'real big one', 1: 'land or water', 2: 'land and water', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail family', 7: 'complete new', 8: 'fish + amphibian + mammal + bird', 9: 'amphibian + mammal + bird', 10: 'amphibian + mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fishes', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['size'] == size) & (mapping_df['category_group'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        if mapping_row['category_group'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        target = len(re.split(r'\s*\+\s*', mapping_row['category_group']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['category_group', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])


#%% v20: stable with added delimiters

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'category_group': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['size'] == size) & (mapping_df['category_group'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        if mapping_row['category_group'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        target = len(re.split(r'\s*\+\s*', mapping_row['category_group']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['category_group', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_ordered'
def lookup_category_group_ordered(row):
    category_group_ordered = row['category_group_ordered']
    
    if category_group_ordered == 'complete new':
        return np.nan

    animals_in_zoo = re.split(r'\s*\+\s*', row['animals_in_zoo'])

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*[-\+]\s*', category_group_ordered):  # Use both '-' and '+' as delimiters
        matching_values = next((animal for animal in animals_in_zoo if mapping_dict.get(animal) == word and word not in seen_words), np.nan)
        if matching_values is not np.nan:
            seen_words.add(word)
            result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_ordered, axis=1)

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])










#%% v21

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'category_group': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['size'] == size) & (mapping_df['category_group'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        if mapping_row['category_group'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        target = len(re.split(r'\s*\+\s*', mapping_row['category_group']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['category_group', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_ordered'
def lookup_category_group_ordered(row):
    category_group_ordered = row['category_group_ordered']
    
    if category_group_ordered == 'complete new':
        return np.nan

    animals_in_zoo = re.split(r'\s*\+\s*', row['animals_in_zoo'])

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*[-\+]\s*', category_group_ordered):  # Use both '-' and '+' as delimiters
        matching_values = next((animal for animal in animals_in_zoo if mapping_dict.get(animal) == word and word not in seen_words), np.nan)
        if matching_values is not np.nan:
            seen_words.add(word)
            result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_ordered, axis=1)

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))


def split_category_group(df, prefix):
    # Filter rows where 'category_group' is not 'unknown'
    filtered_df = df[df['category_group'] != 'unknown']

    # Split 'category_group' into a DataFrame of individual columns
    split_df = filtered_df['category_group'].str.split(r'\s*\+\s*', expand=True)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_category_group(data_df, 'cg')
print(result_df)


def split_new_columns_values(df, prefix):
    # Split 'new_columns_values' into a DataFrame of individual columns
    split_df = df['new_columns_values'].apply(pd.Series)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_new_columns_values(data_df, 'nc')
print(result_df)


def split_and_map_column(df, column, prefix, key):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame
    split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column(data_df, 'new_columns_values', 'nc', mapping_dict)
print(result_df)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])




#%% v22

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'size': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'category_group': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(animal not in mapping_dict for animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for animal in animal_list:
        category = mapping_dict.get(animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new 'category' column in the original data
data_df['category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'category_group' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['size'] == size) & (mapping_df['category_group'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['size'] == size].iterrows():
        if mapping_row['category_group'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['category_group']))
        target = len(re.split(r'\s*\+\s*', mapping_row['category_group']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['category_group'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['category_group', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_ordered'
def lookup_category_group_ordered(row):
    category_group_ordered = row['category_group']

    if pd.isna(category_group_ordered) or category_group_ordered == 'complete new':
        return np.nan

    animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*[-\+]\s*', category_group_ordered):  # Use both '-' and '+' as delimiters
        if not pd.isna(word):
            matching_values = next((animal for animal in animals_in_zoo if mapping_dict.get(animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_ordered, axis=1)

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for 'category' column
data_df['category_word_count'] = data_df['category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))


def split_category_group(df, prefix):
    # Filter rows where 'category_group' is not 'unknown'
    filtered_df = df[df['category_group'] != 'unknown']

    # Split 'category_group' into a DataFrame of individual columns
    split_df = filtered_df['category_group'].str.split(r'\s*\+\s*', expand=True)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_category_group(data_df, 'cg')



def split_new_columns_values(df, prefix):
    # Split 'new_columns_values' into a DataFrame of individual columns
    split_df = df['new_columns_values'].apply(pd.Series)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_new_columns_values(data_df, 'nc')



def split_and_map_column(df, column, prefix, key):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame
    split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column(data_df, 'new_columns_values', 'nc', mapping_dict)


# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', 'category', 'no_match_flag', 'category_group', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])




#%% v23: rename variables

rename_thru_dictionary = {  'data_df': 'x100',
                            'size': 'x101',
                            'animal_group': 'x102',
                            'animals_in_zoo': 'x103',
                            'mapping_dict': 'x104',
                            'mapping_df': 'x105',
                            'animals_combined': 'x106',
                            'category_group_ordered': 'x107',
                            'category_order': 'x108',
                            '_animal': 'x109',
                            '_category': 'x110',
                            'unknown': 'x111',
                            'complete new': 'x112'
                        }

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'animal_group': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'animals_combined': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each _animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for _animal in animal_list:
        category = mapping_dict.get(_animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new '_category' column in the original data
data_df['_category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'animals_combined' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['_category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['animal_group'] == size) & (mapping_df['animals_combined'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['animal_group'] == size].iterrows():
        if mapping_row['animals_combined'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        target = len(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['animals_combined'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_order'
def lookup_category_group_order(row):
    category_group_order = row['animals_combined']

    if pd.isna(category_group_order) or category_group_order == 'complete new':
        return np.nan

    _animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*\+\s*', category_group_order):
        if not pd.isna(word):
            matching_values = next((_animal for _animal in _animals_in_zoo if mapping_dict.get(_animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_order, axis=1)

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for '_category' column
data_df['category_word_count'] = data_df['_category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))


def split_category_group(df, prefix):
    # Filter rows where 'animals_combined' is not 'unknown'
    filtered_df = df[df['animals_combined'] != 'unknown']

    # Split 'animals_combined' into a DataFrame of individual columns
    split_df = filtered_df['animals_combined'].str.split(r'\s*\+\s*', expand=True)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_category_group(data_df, 'cg')



def split_new_columns_values(df, prefix):
    # Split 'new_columns_values' into a DataFrame of individual columns
    split_df = df['new_columns_values'].apply(pd.Series)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_new_columns_values(data_df, 'nc')



def split_and_map_column(df, column, prefix, key):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame
    split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column(data_df, 'new_columns_values', 'nc', mapping_dict)


# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', '_category', 'no_match_flag', 'animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])



#%% v24: last stable

rename_thru_dictionary = {  'data_df': 'x100',
                            'size': 'x101',
                            'animal_group': 'x102',
                            'animals_in_zoo': 'x103',
                            'mapping_dict': 'x104',
                            'mapping_df': 'x105',
                            'animals_combined': 'x106',
                            'category_group_ordered': 'x107',
                            'category_order': 'x108',
                            '_animal': 'x109',
                            '_category': 'x110',
                            'unknown': 'x111',
                            'complete new': 'x112'
                        }

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}, 'override': {0: 'no', 1: 'no', 2: 'no', 3: 'no', 4: 'yes', 5: 'no', 6: 'no', 7: 'no', 8: 'no', 9: 'no', 10: 'yes', 11: 'no', 12: 'no', 13: 'no', 14: 'no', 15: 'no', 16: 'yes', 17: 'no', 18: 'no', 19: 'no', 20: 'yes', 21: 'no', 22: 'no', 23: 'no'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'animal_group': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'animals_combined': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

override_dict = {'tuna': 'yes', 'crane': 'yes', 'lion': 'yes'}

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each _animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for _animal in animal_list:
        category = mapping_dict.get(_animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new '_category' column in the original data
data_df['_category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'animals_combined' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['_category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['animal_group'] == size) & (mapping_df['animals_combined'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['animal_group'] == size].iterrows():
        if mapping_row['animals_combined'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        target = len(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['animals_combined'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_order'
def lookup_category_group_order(row):
    category_group_order = row['animals_combined']

    if pd.isna(category_group_order) or category_group_order == 'complete new':
        return np.nan

    _animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*\+\s*', category_group_order):
        if not pd.isna(word):
            matching_values = next((_animal for _animal in _animals_in_zoo if mapping_dict.get(_animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Function to look up values for each word in 'category_group_order'
def lookup_category_group_order_addon(row):
    category_group_order = row['animals_combined']

    if pd.isna(category_group_order) or category_group_order == 'complete new':
        return np.nan

    _animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*\+\s*', category_group_order):
        if not pd.isna(word):
            matching_values = next((_animal for _animal in _animals_in_zoo if mapping_dict.get(_animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                if row['override'] != 'no' and override_dict.get(matching_values) == 'yes':
                    result_values.append('something overridden')
                else:
                    result_values.append(matching_values)

    # Apply mapping_dict to the result array
    result_values = [mapping_dict.get(value, value) for value in result_values]

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_order, axis=1)


def apply_custom_logic(row):
    result_values = []

    for value in row['new_columns_values']:
        if pd.notna(value):
            if row['override'] != 'no' and override_dict.get(value, 'no') == 'yes':
                result_values.append('custom substring')
            else:
                result_values.append(value)

    return result_values if result_values else ['missing']

# Apply the custom logic to create a new column 'new_columns_values_overridden'
data_df['new_columns_values_overridden'] = data_df.apply(lambda row: apply_custom_logic(row) if isinstance(row['new_columns_values'], list) else ['missing'], axis=1)

# Map the rest of the values using the mapping_dict
data_df['new_columns_values_overridden'] = data_df['new_columns_values_overridden'].apply(lambda values: [mapping_dict.get(value, value) for value in values])

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for '_category' column
data_df['category_word_count'] = data_df['_category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))


def split_category_group(df, prefix):
    # Filter rows where 'animals_combined' is not 'unknown'
    filtered_df = df[df['animals_combined'] != 'unknown']

    # Split 'animals_combined' into a DataFrame of individual columns
    split_df = filtered_df['animals_combined'].str.split(r'\s*\+\s*', expand=True)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_category_group(data_df, 'cg')



def split_new_columns_values(df, prefix):
    # Split 'new_columns_values' into a DataFrame of individual columns
    split_df = df['new_columns_values'].apply(pd.Series)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_new_columns_values(data_df, 'nc')


""" old
def split_and_map_column(df, column, prefix, key):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame
    split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df
 """

def split_and_map_column(df, column, prefix, key=None):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame if key is provided
    if key is not None:
        split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column(data_df, 'new_columns_values_overridden', 'nc')
result_df = split_and_map_column(data_df, 'new_columns_values', 'animals', key=mapping_dict)

# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', '_category', 'no_match_flag', 'animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])



#%% v25

rename_thru_dictionary = {  'data_df': 'x100',
                            'size': 'x101',
                            'animal_group': 'x102',
                            'animals_in_zoo': 'x103',
                            'mapping_dict': 'x104',
                            'mapping_df': 'x105',
                            'animals_combined': 'x106',
                            'category_group_ordered': 'x107',
                            'category_order': 'x108',
                            '_animal': 'x109',
                            '_category': 'x110',
                            'unknown': 'x111',
                            'complete new': 'x112'
                        }

import pandas as pd
import numpy as np
import re

data_df = pd.DataFrame({'size': {0: 'big', 1: 'medium', 2: 'medium', 3: 'medium', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'big', 9: 'big', 10: 'big', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'medium', 16: 'big', 17: 'medium', 18: 'big', 19: 'small', 20: 'small', 21: 'big', 22: 'small', 23: 'small'}, 'animals_in_zoo': {0: 'tiger + lion + leopard + bears', 1: 'leopard + platpus + pigeon + crocodile', 2: 'leopard + . + pigeon + crocodile', 3: 'leopard + platpus +   + crocodile', 4: 'crocodile + tigers + beard + platpuses', 5: 'crocodile + tiger + bear + platpus', 6: 'tiger + bear + crocodile + crane', 7: 'tiger + bear + crocodile + crane + tuna', 8: 'lion', 9: 'tunas', 10: 'crane', 11: 'leopard + platpus', 12: 'leopard', 13: 'leopard + platpus + pigeon', 14: 'leopard + platpus + pigeon + mullett', 15: 'mullett', 16: 'tiger + bear + crocodile + crane + tuna + lion', 17: ' ', 18: np.nan, 19: 'sardine + frog', 20: 'frog  +  sardine', 21: 'tiger + bear  + crane + tuna', 22: 'centipede', 23: 'snail'}, 'override': {0: 'no', 1: 'no', 2: 'no', 3: 'no', 4: 'yes', 5: 'no', 6: 'no', 7: 'no', 8: 'no', 9: 'no', 10: 'yes', 11: 'no', 12: 'no', 13: 'no', 14: 'no', 15: 'no', 16: 'yes', 17: 'no', 18: 'no', 19: 'no', 20: 'yes', 21: 'no', 22: 'no', 23: 'no'}})

mapping_dict = {'crocodile': 'amphibian', 'platpus': 'amphibian', 'pigeon': 'bird', 'crane': 'bird', 'tuna': 'fish', 'mullett': 'fish', 'tiger': 'mammal', 'lion': 'mammal', 'leopard': 'mammal', 'bear': 'omnivore', 'frog': 'amphibian', 'sardine': 'fish', 'centipede': 'insect', 'snail': 'mollusc'}

mapping_df = pd.DataFrame({'animal_group': {0: 'big', 1: 'big', 2: 'big', 3: 'big', 4: 'big', 5: 'big', 6: 'big', 7: 'big', 8: 'medium', 9: 'medium', 10: 'medium', 11: 'medium', 12: 'medium', 13: 'medium', 14: 'medium', 15: 'small', 16: 'small'}, 'animals_combined': {0: 'fish + amphibian + mammal', 1: 'mammal + amphibian', 2: 'mammal + fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'mollusc', 7: 'unknown', 8: 'fish + amphibian + mammal + bird', 9: 'mammal + bird + amphibian', 10: 'mammal + amphibian', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'unknown', 15: 'fish', 16: 'unknown'}, 'category_group_ordered': {0: 'fish+amphibian+mammal', 1: 'amphibian+mammal', 2: 'mammal-fish', 3: 'mammal', 4: 'fish', 5: 'bird', 6: 'snail', 7: 'complete new', 8: 'fish+amphibian+mammal+bird', 9: 'amphibian+mammal+bird', 10: 'amphibian+mammal', 11: 'mammal', 12: 'fish', 13: 'bird', 14: 'complete new', 15: 'fish', 16: 'complete new'}, 'category_order': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 1, 9: 2, 10: 3, 11: 4, 12: 5, 13: 6, 14: 7, 15: 1, 16: 2}})

override_dict = {'tuna': 'yes', 'crane': 'yes', 'lion': 'yes'}

# Create a new DataFrame for records with no match
no_match_df = data_df[data_df['animals_in_zoo'].apply(lambda x: isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))]

# Flag records with no match as 1 in the original DataFrame
data_df['no_match_flag'] = data_df['animals_in_zoo'].apply(lambda x: 1 if ((isinstance(x, str) and any(_animal not in mapping_dict for _animal in re.split(r'\s*\+\s*', x)))) or (pd.isna(x)) else 0)

# Function to look up the category for each _animal in the 'animals_in_zoo' column
def get_category(animal_list):
    unique_categories = []
    seen_categories = set()
    for _animal in animal_list:
        category = mapping_dict.get(_animal)
        if category and category not in seen_categories:
            seen_categories.add(category)
            unique_categories.append(category)
    return ' + '.join(unique_categories) if unique_categories else None

# Apply the function to create a new '_category' column in the original data
data_df['_category'] = data_df.apply(lambda row: get_category(re.split(r'\s*\+\s*', str(row['animals_in_zoo'])) if (isinstance(row['animals_in_zoo'], str)) else []), axis=1)

# Apply the function to create new 'category_group_ordered', 'category_order', and 'animals_combined' columns in the original data
def lookup_category_group(row):
    no_match_flag = row['no_match_flag']
    size = row['size']
    category = row['_category']

    if no_match_flag == 1 or pd.isna(category):
        unknown_row = mapping_df[(mapping_df['animal_group'] == size) & (mapping_df['animals_combined'] == 'unknown')].iloc[0]
        return 'unknown', 'complete new', unknown_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
    
    for _, mapping_row in mapping_df[mapping_df['animal_group'] == size].iterrows():
        if mapping_row['animals_combined'] == 'unknown':
            return 'unknown', 'complete new', mapping_row['category_order'], len(re.split(r'\s*\+\s*', 'complete new')), 0
        
        category_group = set(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        target = len(re.split(r'\s*\+\s*', mapping_row['animals_combined']))
        hit = len(set(re.split(r'\s*\+\s*', category)) & category_group)
        if target == hit:
            return mapping_row['animals_combined'], mapping_row['category_group_ordered'], mapping_row['category_order'], target, hit
    
    return 'unknown', 'complete new', 7, len(re.split(r'\s*\+\s*', 'complete new')), 0

data_df[['animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']] = data_df.apply(lookup_category_group, axis=1, result_type='expand')

# Function to look up values for each word in 'category_group_order'
def lookup_category_group_order(row):
    category_group_order = row['animals_combined']

    if pd.isna(category_group_order) or category_group_order == 'complete new':
        return np.nan

    _animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*\+\s*', category_group_order):
        if not pd.isna(word):
            matching_values = next((_animal for _animal in _animals_in_zoo if mapping_dict.get(_animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                result_values.append(matching_values)

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Function to look up values for each word in 'category_group_order'
def lookup_category_group_order_addon(row):
    category_group_order = row['animals_combined']

    if pd.isna(category_group_order) or category_group_order == 'complete new':
        return np.nan

    _animals_in_zoo = re.split(r'\s*\+\s*', str(row['animals_in_zoo']))  # Convert to string to handle NaN values

    result_values = []
    seen_words = set()

    for word in re.split(r'\s*\+\s*', category_group_order):
        if not pd.isna(word):
            matching_values = next((_animal for _animal in _animals_in_zoo if mapping_dict.get(_animal) == word and word not in seen_words), None)
            if matching_values is not None:
                seen_words.add(word)
                if row['override'] != 'no' and override_dict.get(matching_values) == 'yes':
                    result_values.append('something overridden')
                else:
                    result_values.append(matching_values)

    # Apply mapping_dict to the result array
    result_values = [mapping_dict.get(value, value) for value in result_values]

    # Ensure the result array has the same length as the expected columns
    return result_values if result_values else np.nan

# Apply the function to get a single list of values
data_df['new_columns_values'] = data_df.apply(lookup_category_group_order, axis=1)


def apply_custom_logic(row):
    result_values = []

    for value in row['new_columns_values']:
        if pd.notna(value):
            if row['override'] != 'no' and override_dict.get(value, 'no') == 'yes':
                result_values.append('custom substring')
            else:
                result_values.append(value)

    return result_values if result_values else ['missing']

# Apply the custom logic to create a new column 'new_columns_values_overridden'
data_df['new_columns_values_overridden'] = data_df.apply(lambda row: apply_custom_logic(row) if isinstance(row['new_columns_values'], list) else ['missing'], axis=1)

# Map the rest of the values using the mapping_dict
data_df['new_columns_values_overridden'] = data_df['new_columns_values_overridden'].apply(lambda values: [mapping_dict.get(value, value) for value in values])

# Calculate word count for 'animals_in_zoo' column
data_df['animals_in_zoo_word_count'] = data_df['animals_in_zoo'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))) if (isinstance(x, str)) else 0)

# Calculate word count for '_category' column
data_df['category_word_count'] = data_df['_category'].apply(lambda x: len(re.findall(r'\b\w+\b', str(x))))


def split_category_group(df, prefix):
    # Filter rows where 'animals_combined' is not 'unknown'
    filtered_df = df[df['animals_combined'] != 'unknown']

    # Split 'animals_combined' into a DataFrame of individual columns
    split_df = filtered_df['animals_combined'].str.split(r'\s*\+\s*', expand=True)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_category_group(data_df, 'cg')



def split_new_columns_values(df, prefix):
    # Split 'new_columns_values' into a DataFrame of individual columns
    split_df = df['new_columns_values'].apply(pd.Series)

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_new_columns_values(data_df, 'nc')


""" old
def split_and_map_column(df, column, prefix, key):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame
    split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df
 """

""" old
def split_and_map_column_old(df, column, prefix, key=None):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the mapping dictionary to the split DataFrame if key is provided
    if key is not None:
        split_df = split_df.map(lambda x: key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column_old(data_df, 'new_columns_values_overridden', 'nc')
result_df = split_and_map_column_old(data_df, 'new_columns_values', 'animals', key=mapping_dict)
 """


def split_and_map_column(df, column, prefix, key=None, secondary_key=None):
    # Split the specified column into a DataFrame of individual columns
    split_df = df[column].apply(pd.Series)

    # Apply the primary mapping dictionary to the split DataFrame if key is provided
    if key is not None:
        split_df = split_df.map(lambda x: key.get(x, x))

    # Apply the secondary mapping dictionary to the split DataFrame if secondary_key is provided
    if secondary_key is not None:
        split_df = split_df.map(lambda x: secondary_key.get(x, x))

    # Add prefix to column names
    split_df.columns = [f'{prefix}_{i+1}' for i in range(split_df.shape[1])]

    # Concatenate the split DataFrame with the original DataFrame
    result_df = pd.concat([df, split_df], axis=1)

    return result_df

result_df = split_and_map_column(data_df, 'new_columns_values_overridden', 'nc', key=mapping_dict, secondary_key=mapping_dict)











# Print the result
print("Original DataFrame:")
print(data_df[['size', 'animals_in_zoo', '_category', 'no_match_flag', 'animals_combined', 'category_group_ordered', 'category_order', 'target', 'hit']])
print("\nDataFrame with No Match:")
print(no_match_df[['size', 'animals_in_zoo']])



