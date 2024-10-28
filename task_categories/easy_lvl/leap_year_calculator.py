# TASK: Create a program that asks a user in console for a year. Tell the user if the given year is a leap year or not.

year = int(input())

if year % 4 == 0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is NOT a leap year")