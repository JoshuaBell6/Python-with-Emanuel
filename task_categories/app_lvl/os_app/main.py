## MAIN PROGRAM ##

from methods import one_list_element
from command_methods import print_help
from command_methods import display_directories
from command_methods import cd
from command_methods import valid_mkdir
from command_methods import add_to_directory
from command_methods import valid_touch
from command_methods import valid_rm
from command_methods import recursive_delete
from command_methods import rmdir
from command_methods import mv

from methods import load_variable
import pickle

# start of initial 
key = ('main', 'main')
filename = 'latest_directory.pkl'
loaded_data = load_variable(filename)
if loaded_data:
    directories = loaded_data
else:
    directories = {key: []}
loop = True
# end of initial

while loop:
    user_input = input(f"{key[0]}> ")
    list_user_input = user_input.split()
    command = list_user_input[0] # first word of input
    rest = list_user_input[1:] # a list of all other words after 'command' 
    one_word = one_list_element(rest)

    if len(rest) > 2:
        print(f"No current command allows '{len(rest)}' arguments")

    elif command == "?":
        print("Directories = ", directories)

    elif command == "key":
        print("key = ", key)
   
    elif command == 'q':
        variable_to_save = directories
        with open(filename, 'wb') as file:
            pickle.dump(variable_to_save, file)
        loop = False # exits the app

    elif command == 'help':
        print_help()
        
    elif command == 'ls':
        display_directories(key, directories)

    elif command == 'cd':
        key = cd(key, directories, rest, one_word)
       
    elif command == 'mkdir':
        if valid_mkdir(rest, one_word):
            add_to_directory(directories, key, new_dir = one_word)

    elif command == 'touch':
        if valid_touch(rest, one_word):
            add_to_directory(directories, key, new_dir = one_word)

    elif command == 'mv':
        mv(key, directories, rest)

    elif command == 'rmdir':
        rmdir(key, directories, rest, one_word)

    elif command == 'rm':
        if valid_rm(key, directories, rest, one_word):
            recursive_delete(directories, one_word)
            print(f"'{one_word}' is deleted successfully")

    else:
        print(f"'{command}' is not a command, use 'help' to see the list of available commands")