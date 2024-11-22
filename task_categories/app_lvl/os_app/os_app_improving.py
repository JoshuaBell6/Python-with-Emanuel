# Code the app here

import re

# COMMAND help
def print_help():
    print('''Here is the list of commands you can use:
ls - displays all directories and files on the current directory level
cd - changes a current directory (syntax: cd {dirname})
mkdir - creates a new directory (syntax: mkdir {dirname})
touch - creates a new file (syntax: touch {filename})
mv - renames a file or a directory (syntax: mv {existing_name} {new_name})
rmdir - deletes an empty directory (syntax: rmdir {dirname})
rm - deletes a file or a directory along with its contents
q - exits the app''')
     

# COMMAND ls
def display_directories(index, directories):
    directory_folder = directories[index + 1]
    if len(directory_folder) == 0:
        print (".")
    else:
        for item in directory_folder:
            if "." in item:
                print(f"{item}")
            else:
                print(f"/{item}")
        print(".")


# COMMAND mkdir
# check if word has only valid characters
def valid_characters(word):       
    return not all(char.isalnum() or char == '_' for char in word)    

# print statements for mkdir
def mkdir(dir_name):
    if len(dir_name) == 0:
        print("'mkdir' requires an argument {dirname}; usage: mkdir {dirname}")
        return False

    elif valid_characters(dir_name[0]):
        print(f"'{dir_name[0]}' is an invalid directory name")
        return False

    else:
        return True

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

def add_to_directory(directory_names, directories, index, new_dir):
    if remove_after_dot(new_dir) in remove_after_dot_list(directories[index + 1]):
        print(f"Name '{remove_after_dot(new_dir)}' already exists in current directory")
        return False

    else:
        directories.append((new_dir, index)) #directories += (new_dir, index), []
        directories.append([]) #directories += (new_dir, index), []
        directories[index + 1] += [new_dir]
        directory_names.append(new_dir)
        if remove_after_dot(new_dir) == new_dir:
            print(f"'{new_dir}' directory created successfuly")
        else:
            print(f"'{new_dir}' file created successfuly")
    
        return directories


# COMMAND touch
def ends_with_extension(word):
    valid_extensions = {'.txt', '.text', '.md'}  # set of allowed extensions
    return any(word.lower().endswith(ext) for ext in valid_extensions)

def touch(filename_ext):
    if len(filename_ext) == 0:
        print("'touch' requires an argument {filename}; usage: touch {filename}.{extension}")
        return False

    elif not ends_with_extension(filename_ext[0]):
        print("'touch' argument {filename} requires an extension; usage: touch {filename}.{extension}")
        return False

    else:
        return True
    
# COMMAND mv
# string + space + string
def validate_input(text):
    pattern = r'^\S+\s\S+$'
    return bool(re.match(pattern, text))

# string + nothing
def one_string(text):
    pattern = r'^(?!$)(?!(\S+\s\S+)$).*$'
    return bool(re.match(pattern, text))

def remove_after_dot(string):
    parts = string.split('.', 1)  # Split at most once
    return parts[0] if len(parts) > 1 else string

def get_extension(string):
    parts = string.split('.', 1)  # Split at most once
    if len(parts) > 1:
        return parts[1].lower()  # Return the part after the dot, converted to lowercase
    return ""  # Return an empty string if there's no dot

def add_clean_extension(dirty_extension, filename):
    # Extract everything after the last dot in the dirty_extension
    clean_extension = dirty_extension.split('.')[-1]
    
    # Remove any existing extension from the filename
    base_filename = filename.split('.')[0]
    
    # Combine the base filename and clean extension
    return f"{base_filename}.{clean_extension}"

# main function of mv
def mv(index, directories, name):
    
    if len(name) == 0:
        print("'mv' requires an argument {existing_name}; usage: mv {existing_name} {new_name}")

    elif len(name) == 1:
        print("'mv' requires an argument {new_name}; usage: mv {existing_name} {new_name}")

    elif len(name) == 2:
        holder = name
        existing_name = holder[0]
        new_name = holder[1]

        index_of_tup = -2
        exists = False
        for dir_name, dir_idx in directories[::2]:
            index_of_tup += 2
            # Change directory name
            if dir_name == existing_name and dir_idx == index and existing_name == remove_after_dot(existing_name):
                exists = True
                directories[index_of_tup] = (new_name, dir_idx)
                directories[dir_idx + 1].remove(dir_name)
                directories[dir_idx + 1].append(new_name)
                print(f"'{existing_name}' renamed to '{new_name}'")
                break
            
            # Change file name
            elif remove_after_dot(dir_name) == existing_name and dir_idx == index:
                exists = True
                directories[index_of_tup] = (add_clean_extension(dir_name, new_name), dir_idx)
                directories[dir_idx + 1].remove(dir_name)
                directories[dir_idx + 1].append(add_clean_extension(dir_name, new_name))
                print(f"'{existing_name}' renamed to '{new_name}'")
                break
  
        if not exists:
            print(f"'{existing_name}' does not exist in this directory")
    
# COMMAND rmdir
def rmdir(index, directories, name):
    if len(name) == 0:
        print("'rmdir' requires an argument {dirname}; usage: rmdir {dirname}")

    elif ends_with_extension(name[0]):
        print(f"'{name[0]}' is not a directory")

    else:
        name = name[0]
        index_of_tup = -2
        exists = False
        for dir_name, dir_idx in directories[::2]:
            index_of_tup += 2
            if dir_name == name and dir_idx == index:
                exists = True
                if len(directories[index_of_tup + 1]) == 0:
                    ##print(f"Directory '{name}' can be deleted as its empty")
                    directories.pop(index_of_tup)
                    directories.pop(index_of_tup)
                    directories[dir_idx + 1].remove(name)
                    ##print("Directories after delete ", directories)
                    print(f"'{name}' is deleted successfully")
                    break
                else:
                    print(f"'{name}' is not an empty directory")
                    break
  
        if not exists:
            print(f"'{name}' does not exist in this directory")

# COMMAND rm

# list --> dictionary
def list_to_dict(lst):
    # Create an empty dictionary
    result_dict = {}
    
    # Iterate over the list in steps of 2
    for i in range(0, len(lst) - 1, 2):
        # Use the odd indexed element as the key and the next even indexed element as the value
        result_dict[lst[i]] = lst[i + 1]
    
    return result_dict

# dictionary --> list
def dict_to_list(dct):
    # Create an empty list to hold the result
    result_list = []
    
    # Iterate over the dictionary items
    for (dir_name, parent_index), contents in dct.items():
        # Append the directory tuple and its contents to the result list
        result_list.append((dir_name, parent_index))
        result_list.append(contents)
    
    return result_list

# list with keys
def list_to_key(item):
    # Convert tuples to lists
    for i in range(0, len(item), 2):
        if isinstance(item[i], tuple):
            item[i] = list(item[i])
    
    # Process parent-child relationships
    for i in range(2, len(item), 2):
        parent_index = item[i][1] 
        item[i][1] = item[parent_index][0]
    
    # Convert lists back to tuples for odd-indexed items
    for i in range(0, len(item), 2):
        if isinstance(item[i], list):
            item[i] = tuple(item[i])
    
    return item

# list of list to tuples
def transform_list(input_list):
    # Create a dictionary to store the positions of words
    positions = {}
    
    # First pass: collect positions of all words
    for index, item in enumerate(input_list):
        if isinstance(item, tuple) and len(item) == 2:
            positions[item[0]] = index
        elif isinstance(item, list) and len(item) == 1:
            positions[item[0]] = index
    
    # Second pass: update the tuples
    result = []
    for item in input_list:
        if isinstance(item, tuple) and len(item) == 2:
            if item[1] in positions:
                result.append((item[0], positions[item[1]]))
            else:
                result.append(item)
        else:
            result.append(item)
    
    return result

# delete function
def recursive_delete(dictionary, delete_words):
    if isinstance(delete_words, str):
        delete_words = [delete_words]
    
    new_delete_words = []
    keys_to_delete = []

    # First pass: identify keys to delete and new words to add to delete_words
    for key, value in dictionary.items():
        if key[0] in delete_words:
            keys_to_delete.append(key)
            new_delete_words.extend(value)
        else:
            # Remove delete_words from the value list
            dictionary[key] = [word for word in value if word not in delete_words]

    # Delete identified keys
    for key in keys_to_delete:
        del dictionary[key]

    # If new words were added to delete_words, recurse
    if new_delete_words:
        delete_words.extend(new_delete_words)
        return recursive_delete(dictionary, delete_words)
    
    return dictionary

def rm(index, directories, name):
    if len(name) == 0:
        print("'rm' requires an argument {name}; usage: rm {name}")
        return False

    elif directories[index][0] == name[0]:
        print("'mydir' is a current directory, navigate to the parent directory to delete it")
        return False

    elif name[0] not in directories[index + 1]:
        print(f"'{name[0]}' does not exist in this directory")
        return False
    
    else:
        return True





## MAIN PROGRAM ##

# start of initial 
directory_names = ['main']
index = 0
directories = [(directory_names[index], 0),[]]

loop = True
former_index = 0
# end of initial

while loop:
    user_input = input(f"{directories[index][0]}> ")
    list_user_input = user_input.split()
    command = list_user_input[0]
    rest = list_user_input[1:]

    if command == "?":
        print("Directories = ", directories)

    elif command == "index":
        print("index = ", index)

    elif command == "rest":
        print("rest = ", rest)

    elif command == "names":
        print("names = ", directory_names)
    
    elif command == 'q':
        loop = False # exits the app

    elif command == 'help':
        print_help()
        
    elif command == 'ls':
        display_directories(index, directories)

    elif command == 'cd':
        # cd or cd .
        if len(rest) == 0 or rest[0] == '.':
            continue

        # cd ..
        elif rest[0] == '..':
            index = directories[index][1]
            continue
        
        # cd {directory name}
        else:           
            val = 0
            exists = False
            for dir_name, dir_idx in directories[2::2]:
                val += 2
                if rest[0] == dir_name and index == dir_idx:
                    former_index = index
                    index = val
                    exists = True

            # cd {dirname that doesn't exist}
            if not exists:
                print(f"'{rest[0]}' does not exist in this directory")
       
    elif command == 'mkdir':
        if mkdir(rest):
            add_to_directory(directory_names, directories, index, new_dir = rest[0])

    elif command == 'touch':
        if touch(rest):
            add_to_directory(directory_names, directories, index, new_dir = rest[0])

    elif command == 'mv':
        mv(index, directories, name = rest)

    elif command == 'rmdir':
        rmdir(index, directories, name = rest)

    elif command == 'rm':
        if rm(index, directories, name = rest):
            keyz = list_to_key(directories)
            dct = list_to_dict(keyz)
            deleted = recursive_delete(dct, rest[0])
            something = dict_to_list(deleted)
            directories = transform_list(something)
            print(f"'{rest[0]}' is deleted successfully")

    else:
        print(f"'{command}' is not a command, use 'help' to see the list of available commands")
    
    
    

##################### end #################

