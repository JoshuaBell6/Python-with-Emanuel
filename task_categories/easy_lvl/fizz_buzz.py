# TASK: Write a program which takes a number input from a user and prints 3 outcomes.
"""
Outcome 1: If number is divisible by 3, print "FIZZ"
Outcome 2: If number is divisible by 5, print "BUZZ"
Outcome 3: If number is divisible by both 3 and 5, print "FIZZBUZZ"
"""

while True:
    try:
        user = int(input("Enter a number: "))
        break  # Exit the loop if successful conversion to int
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if user % 3 == 0 and user % 5 == 0:
    print("FIZZBUZZ")

elif user % 3 == 0:
    print("FIZZ")

elif user % 5 == 0:
    print("BUZZ")

else:
    print("None of the above")

# TASK OBSERVATIONS:
# Always explain to user what is expected to input
# If you input string, the program breaks
# OPTIONAL: Try to fix the string input problem
