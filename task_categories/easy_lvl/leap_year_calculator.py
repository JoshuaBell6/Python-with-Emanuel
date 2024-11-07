# TASK: Create a program that asks a user in console for a year. Tell the user if the given year is a leap year or not.

while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid year!")

if year % 4 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")

# TASK OBSERVATIONS:
# Always explain to user what is expected to input
# If you input string, the program breaks
# OPTIONAL: Try to fix the string input problem
