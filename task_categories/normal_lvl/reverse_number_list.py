# TASK: Write a function that takes a random non-negative number and returns the digits of this number within a list in reverse order.
"""
Example:
    12345 -> [5, 4, 3, 2, 1]
"""


def reverse_number_list(num):
    num = str(num)
    lst = []
    for digit in num:
        lst.append(int(digit))
        reversed = reverse_list(lst)
    return reversed

def reverse_list(lst):
    return lst[::-1]

# Don't change the code below this line


if reverse_number_list(345234) == [4, 3, 2, 5, 4, 3]:
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
