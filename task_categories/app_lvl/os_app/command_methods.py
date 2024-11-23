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
def display_directories(key, directories):
    directory_folder = directories[key]
    for item in directory_folder:
        if "." in item:
            print(f"{item}")
        else:
            print(f"/{item}")
    print(".")

# COMMAND cd
def cd(key, directories, rest, one_word):
    if len(rest) == 0 or one_word == '.':
        pass

    # cd ..
    elif one_word == '..':
        for keyz in directories.keys():
            if keyz[0] == key[1]:
                key = keyz
                break
        return key
    
    # cd {directory name}
    else:           
        if (one_word in directories[key] and not ends_with_extension(one_word)):
            key = (one_word, key[0])

        # cd {dirname that doesn't exist}
        else:
            print(f"'{one_word}' does not exist in this directory")
    
    return key

# COMMAND mkdir
from methods import valid_characters # alphanumeric and '_'
from methods import remove_after_dot
from methods import remove_after_dot_list

# print statements for mkdir errors
def valid_mkdir(rest, one_word):
    if len(rest) == 0:
        print("'mkdir' requires an argument {dirname}; usage: mkdir {dirname}")
        return False

    elif valid_characters(one_word):
        print(f"'{one_word}' is an invalid directory name")
        return False

    else:
        return True
    
def add_to_directory(directories, key, new_dir):
    if remove_after_dot(new_dir) in remove_after_dot_list(directories[key]):
        print(f"Name '{remove_after_dot(new_dir)}' already exists in current directory")

    else:
        directories[(new_dir, key[0])] = [] #directories += (new_dir, index), []
        directories[(key[0], key[1])] += [new_dir]
        if remove_after_dot(new_dir) == new_dir:
            print(f"'{new_dir}' directory created successfuly")
        else:
            print(f"'{new_dir}' file created successfuly")
    
        return directories

# COMMAND touch
from methods import ends_with_extension # True if ends with extension

def valid_touch(rest, one_word):
    if len(rest) == 0:
        print("'touch' requires an argument {filename}; usage: touch {filename}.{extension}")
        return False

    elif not ends_with_extension(one_word):
        print("'touch' argument {filename} requires an extension; usage: touch {filename}.{extension}")
        return False

    else:
        return True


# COMMAND mv
from methods import ends_with_extension
from methods import remove_after_dot
from methods import remove_after_dot_list
from methods import add_clean_extension

# main function of mv
def mv(key, directories, rest):
    
    if len(rest) == 0:
        print("'mv' requires an argument {existing_name}; usage: mv {existing_name} {new_name}")

    elif len(rest) == 1:
        print("'mv' requires an argument {new_name}; usage: mv {existing_name} {new_name}")

    else:
        holder = rest
        existing_name = holder[0]
        new_name = holder[1]

        if existing_name not in remove_after_dot_list(directories[key]):
            print(f"'{existing_name}' does not exist in this directory")

        elif new_name  in remove_after_dot_list(directories[key]):
            print(f"'{new_name}' already exists in this directory")

        else:
            isFile = False
            # Change file name
            for value in directories[key]:
                if value != existing_name and remove_after_dot(value) == existing_name:
                    directories[key].remove(value) # removes old name from list
                    directories[(add_clean_extension(value, new_name), key[0])] = [] # adds dict item with new name
                    directories.pop((value, key[1]))
                    directories[key] += [(add_clean_extension(value, new_name))]
                    print(f"'{existing_name}' renamed to '{new_name}'")
                    isFile = True
                    break

            # Change directory name
            if not isFile:
                for value in directories[key]:
                    if value == existing_name and remove_after_dot(value) == existing_name:
                        values = directories[(existing_name, key[0])] # values from named directory
                        directories[new_name, key[1]] = values # values is a list
                        directories[key].remove(existing_name) # delete old directory name in current directory
                        directories[key].append(new_name) # add new directory name in current directory's list
                        directories.pop((existing_name, key[1])) # delete old directory name in the dictionary
                        
                        if len(values) == 1:
                            undervalues = directories[values[0], existing_name] #'m111'
                            directories.pop((values[0], existing_name)) # no more m11, m2 : m111
                            directories.update({(values[0], new_name) : undervalues}) # ('m11', 'm1'): ['m111'] --> ('m11', 'm2'): ['m111']

                        else:
                            for i in range(len(values)):
                                undervalues = directories[values[i], existing_name] #'m111'
                                directories.pop((values[i], existing_name)) # no more m11, m2 : m111
                                directories.update({(values[i], new_name) : undervalues}) # ('m11', 'm1'): ['m111'] --> ('m11', 'm2'): ['m111']
                                
                        print(f"'{existing_name}' renamed to '{new_name}'")
                        
                        break


# COMMAND rmdir
def rmdir(key, directories, rest, one_word):
    if len(rest) == 0:
        print("'rmdir' requires an argument {dirname}; usage: rmdir {dirname}")

    elif ends_with_extension(one_word):
        print(f"'{one_word}' is not a directory")

    else:
        if (one_word, key[0]) in directories.keys():
            if len(directories[(one_word, key[0])]) != 0:
                print(f"'{one_word}' is not an empty directory")
            else:
                for keyz, value in directories.items():
                    directories[keyz] = [word for word in value if word != one_word] ##
                directories.pop((one_word, key[0]))
                print(f"'{one_word}' is deleted successfully")
                
        else:
            print(f"'{one_word}' does not exist in this directory")
  

# Command rm
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

def valid_rm(key, directories, rest, one_word):
    if len(rest) == 0:
        print("'rm' requires an argument {name}; usage: rm {name}")
        return False

    elif key[0] == one_word:
        print("'mydir' is a current directory, navigate to the parent directory to delete it")
        return False

    elif one_word not in directories[key]:
        print(f"'{one_word}' does not exist in this directory")
        return False
    
    else:
        return True