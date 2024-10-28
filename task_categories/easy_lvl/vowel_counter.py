# TASK: Write a program that takes a string input from the user and counts the number of vowels (a, e, i, o, u) in the string.

user = input()

vowels = 0
for i in user:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels += 1

print(vowels)