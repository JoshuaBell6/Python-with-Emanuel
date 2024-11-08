# TASK: Write a program that takes a string input from the user and counts the number of vowels (a, e, i, o, u) in the string.

user = input("Enter a string: ")

vowels = 0
for i in user:
    if i.lower() in 'aeiou':
        vowels += 1

print(vowels)

# TASK OBSERVATIONS:
# Always explain to user what is expected to input (fixed)
# If user types capital vowels, the counter doesn't work (fixed)
