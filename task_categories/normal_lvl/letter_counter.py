# TASK: Write a program that asks the user for a string in the console and prints how many letters it has.

"""
Rules:
    - Make sure you handle errors
        - Numbers are not letters
        - Separators are not letters
        - Symbols are not letters

        Hint: Regex helps here a lot (not mandatory)
Example:
    input -> Test sentence
    output ->  12
"""

import re

user = input("Enter a string: ")

def count_letters(word):
    unvalid = r'[^A-Za-z]' # negation of valid characters
    clean_word = re.sub(unvalid, '', word)
    return len(clean_word)

print(f"The string has {count_letters(user)} letters in it.") # For example: 'I c@n say anyth1ng!' has 13 letters
    
