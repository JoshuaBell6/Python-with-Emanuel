# TASK: Create a program that asks the user in console for two numbers and an operation (+, -, *, or /). Perform the chosen operation on the two numbers and print the result.

"""
Example:
    input -> 5
    input -> 5
    input -> +
    output -> 10
"""

x = int(input())
y = int(input())
operation = input()

if operation == '+':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '*':
    print(x * y)
elif operation == '/':
    print(x / y)

# TASK OBSERVATIONS:
# Always explain to user what is expected to input
# This is the simplest version of calculator with many flaws (simple_calculator_2 will have harder requirements)
