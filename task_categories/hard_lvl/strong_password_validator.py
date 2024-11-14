# TASK: Create a program that asks a user to input a string which is acting as a password.
"""
Rules:
    - A password must be at least 8 characters long
    - A password must contain at least one capital letter, but cannot begin with it
    - A password must contain at least one digit
    - A password must contain at least one symbol character
    - A password cannot contain separator characters (space . , ; : _ + - / ~)

    - Explain to user which validation is missing in the order of laid rules
"""

loop = True

errors = 0

while loop:

    user = input("Enter a password: ")

    # Password length check
    if len(user) < 8:
        print("Password must be at least 8 characters long.")
        errors += 1

    # Capital letter check
    capital_letters = 0
    for char in user[1:]:
        if char in 'ABCDEFGHIJKLOMNPQRSTUVWXYZ':
            capital_letters += 1

    if capital_letters == 0:
        print("Password must contain at least one capital letter, but cannot begin with it.")
        errors += 1

    # Digit check
    digits = 0
    for digit in user:
        if digit in '0123456789':
            digits += 1

    if digits == 0:
        print("Password must contain at least one digit.")
        errors += 1

    # Symbol check
    symbols = 0
    for symbol in user:
        if symbol in '!\"#$%&\'()*<=>?@[\]^`{|}':
            symbols += 1

    if symbols == 0:
        print("Password must contain at least one symbol character.")
        errors += 1

    # Seperator check
    seperators = 0
    for seperator in user:
        if seperator in '.,;:_+-/~ ':
            seperators += 1

    if seperators != 0:
        print("Password cannot contain separator characters (space . , ; : _ + - / ~).")
        errors += 1

    # Amount of errors
    print("# of errors = ", errors)

    if errors == 0:
        loop = False

    errors = 0


print("Password created successfully!")