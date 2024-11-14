# TASK: Create a program that asks a user in console for a year. Tell the user if the given year is a leap year or not.
"""
Rules:
    - If a year has already passed, print result in past tense
    - If the year hasn't yet passed or isn't a current year, print result in the future tense
    - If the year is a current year, print result in present tense
Examples:
    input -> 1998
    output -> The year 1998 was not a leap year

    input -> 2000
    output -> The year 2000 was a leap year

    input -> 2024
    The year 2024 is a leap year

    input -> 2060
    The year 2060 will be a leap year

    input -> 2081
    The year 2081 will not be a leap year
"""

import datetime 

while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid year!")

now = datetime.datetime.now()
current_year = now.year

# Present year
if year == current_year:
    if year % 4 == 0:
        print(f"The year {year} is a leap year")
    else:
        print(f"The year {year} is NOT a leap year")

# Past year
elif year < current_year:
    if year % 4 == 0:
        print(f"The year {year} was a leap year")
    else:
        print(f"The year {year} was NOT a leap year")

# Future year
else:
    if year % 4 == 0:
        print(f"The year {year} will be a leap year")
    else:
        print(f"The year {year} will NOT be a leap year")
