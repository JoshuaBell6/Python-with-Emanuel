# TASK: Write a console program that will ask for a number and then print the result like in example.

"""
Example:
    input -> 3
    output -> 1 sheep... 2 sheep... 3 sheep... zzz
"""

user = int(input())

for i in range(user):
    print(f"{i+1} sheep... ", end='')

print("zzz")

# TASK OBSERVATIONS:
# Always explain to user what is expected to input
# If you input string, the program breaks
# OPTIONAL: Try to fix the string input problem
