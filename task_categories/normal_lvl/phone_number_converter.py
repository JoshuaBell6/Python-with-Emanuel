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

def is_convertible_to_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def convert_phone_number(num):
    num = str(num)

    # Testing if input is valid //DOESN'T WORK  
    if not is_convertible_to_int(num):
        return "Invalid input"

    if len(num) != 10:
        return "Input must be exactly 10 digits long."
        

    num = '(' + str(num[:3]) + ') ' + num[3:6] + '-' + num[6:]

    return num

# Don't change the code below this line


print('Testing code')
if convert_phone_number(5253203443) == "(525) 320-3443":
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
