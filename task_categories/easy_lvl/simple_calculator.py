# TASK: Create a program that asks the user in console for two numbers and an operation (+, -, *, or /). Perform the chosen operation on the two numbers and print the result.

"""
Example:
    input -> 5
    input -> 5
    input -> +
    output -> 10
"""

while True:
    try:
        x = int(input("Enter number 1: "))
        y = int(input("Enter number 2: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")


operation = input("Enter an operation (+, -, *, or /): ")
while operation not in '+-*/':
    print("Invalid operation!")
    operation = input("Enter an operation (+, -, *, or /): ")


if operation == '+':
    print(f"{x} + {y} = {x + y}")
elif operation == '-':
    print(f"{x} - {y} = {x - y}")
elif operation == '*':
    print(f"{x} * {y} = {x * y}")
elif operation == '/':
    print(f"{x} / {y} = {x / y}")

# TASK OBSERVATIONS:
# Always explain to user what is expected to input (fixed)
# This is the simplest version of calculator with many flaws (simple_calculator_2 will have harder requirements)
