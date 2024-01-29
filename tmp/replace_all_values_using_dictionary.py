# replace all values of a text file using a dictionary
def replace_values_in_file(file_path, dictionary):
    # Read the content of the text file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace keys with values
    for key, value in dictionary.items():
        content = content.replace(key, str(value))

    # Write the modified content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

# Example usage:
file_path = r"C:\Users\Ashut\Downloads\new 1.py"
replacement_dict = {  'data_df': 'x100',
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

replace_values_in_file(file_path, replacement_dict)

