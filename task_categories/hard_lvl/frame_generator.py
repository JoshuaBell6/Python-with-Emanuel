# TASK: Create a program that, given an array of strings and a character to be used as border, outputs the frame with the content inside.
"""
Rules:
    - Keep a space between the input string and the left and right borders
    - Let the user know what they need to input
    - Handle errors, prevent the program from crashing if an invalid input is entered
Example:
    text input -> HELLO WORLD
    border input -> #
    output ->
                ###############
                # HELLO WORLD #
                ###############
"""

# Write your code below this line

user_string = input("Enter a string: ")

character = input("Enter a character to be used as border: ")
if len(character) != 1:
    print("Enter exactly one character.")
    character = input("Enter a character to be used as border: ")

print((len(user_string) + 4) * character)
print(character + " " + user_string + " " + character)
print((len(user_string) + 4) * character)

