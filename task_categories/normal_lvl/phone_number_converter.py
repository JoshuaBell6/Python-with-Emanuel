# TASK: Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
"""
Rules:
    - Detect invalid input and let the user know it's incorrect before exiting the program
    - Make sure there are always 10 digits
    - Return result should be in string format
Example:
    input -> 1234567890
    output -> (123) 456-7890
"""


def convert_phone_number(num):
    return num

# Don't change the code below this line


print('Testing code')
if convert_phone_number(5253203443) == "(525) 320-3443":
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
