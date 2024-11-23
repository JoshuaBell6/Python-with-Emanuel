import re

# checks if list has only one element, if it does, it returns the element
def one_list_element(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return False
    
# check if word has only alphanumeric or '_' characters
def valid_characters(word):       
    return not all(char.isalnum() or char == '_' for char in word)    
    

# returns True if the word ends with a valid extension
def ends_with_extension(word):
    valid_extensions = {'.txt', '.text', '.md'}  # set of allowed extensions
    return any(word.lower().endswith(ext) for ext in valid_extensions)

# returns string until dot, even without dot
def remove_after_dot(string):
    parts = string.split('.', 1)  # Split at most once
    return parts[0] if len(parts) > 1 else string

# return list of strings until dot, even without dot
def remove_after_dot_list(input_data):
    def process_string(s):
        parts = s.split('.', 1)  # Split at most once
        return parts[0] if len(parts) > 1 else s

    if isinstance(input_data, str):
        return process_string(input_data)
    elif isinstance(input_data, list):
        return [process_string(item) for item in input_data]
    else:
        raise TypeError("Input must be a string or a list of strings")

# removes extension from first file and adds it to the second one
def add_clean_extension(dirty_extension, filename):
    # Extract everything after the last dot in the dirty_extension
    clean_extension = dirty_extension.split('.')[-1]
    
    # Remove any existing extension from the filename
    base_filename = filename.split('.')[0]
    
    # Combine the base filename and clean extension
    return f"{base_filename}.{clean_extension}"

import pickle
# loading data/directory from file
def load_variable(filename):
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        pass
        #print(f"Error: The file '{filename}' was not found.")
    except pickle.UnpicklingError:
        pass
        #print(f"Error: Unable to unpickle the file '{filename}'. It may be corrupted or in an incompatible format.")
    except Exception as e:
        pass
        #print(f"An unexpected error occurred while trying to load '{filename}': {str(e)}")
    
    return False  # Return False if any exception occurred