# TASK: Create a program that, given a list of numbers, finds the most frequent element value and outputs how many times it ocurrs

"""
Rules:
    - Input the numbers separated by a comma (no need to take care of the edge cases here)
    - Store the most frequent number and how many times it occurs in a list: ['most frequent', 'times occured'] (required for the tests to pass)
    - Make sure the negative numbers are not the same as positive (-1 is not 1)
    - Print the output despite returning a result from a function (tip: use the function's return value to write said print statement)
Example:
    input -> 5, 7, 4, 3, 2, 4, 3, 6, 3, 2
    output -> Number 3 is the most frequent number and occurs 3 times
"""


def calculate_frequency(input):
    list_of_numbers = list(map(int, input.split(", ")))
    dct = {}

    # Initalize dictionary with given keys
    for char in list_of_numbers:
        dct[char] = 0

    # Updates dictionary values with each recurrence of a number
    for char in list_of_numbers:
        dct[char] += 1

    max_key = max(dct, key = dct.get)
    max_value = dct[max_key]
    result = [max_key, max_value]

    return result

# Don't change the code below this line


print("Testing scenarios...")
scenario1 = "5, 7, 4, 3, 2, 4, 3, 6, 3, 2"
scenario2 = "1, 2, 5, 3, -3, 4, -4, 5, 5, -5"
if calculate_frequency(scenario1) == [3, 3] and calculate_frequency(scenario2) == [5, 3]:
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
