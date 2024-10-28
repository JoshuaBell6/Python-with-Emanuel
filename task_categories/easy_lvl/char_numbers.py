# TASK: Write a program that asks the user for a string in the console and prints how many characters it has.

"""
Example:
    input -> Test sentence
    output -> 12
"""

user = input()

# Sum of characters in string without spaces (' ')
chars = 0
for i in user:
    if i != ' ':
        chars += 1

print(chars)

# OBSERVATIONS:
# Always explain to user what is expected to input
# This is the simplest solution with many flaws (char_numbers_2 will have harder requirements)
