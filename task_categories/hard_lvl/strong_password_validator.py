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
    list_of_capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'O', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for char in user[1:]:
        if char in list_of_capital_letters:  # this should also be a list ## LIST
            capital_letters += 1

    if capital_letters == 0:
        print(
            "Password must contain at least one capital letter, but cannot begin with it.")
        errors += 1

    # Digit check
    digits = 0
    list_of_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for digit in user:
        if digit in list_of_digits:  # this should also be a list ## LIST
            digits += 1

    if digits == 0:
        print("Password must contain at least one digit.")
        errors += 1

    # Symbol check
    symbols = 0
    # set_of_symbols = set(r'!\"#$%&\'()*<=>?@[\]^`{|}') # How else do I fix this?
    symbols_list = ['!', "\\", '"', '#', '$', '%', '&', "'",
                    '(', ')', '*', '<', '=', '>', '?', '@', '[', ']', '^', '`', '{', '|', '}']
    for symbol in user:
        if symbol in symbols_list:
            symbols += 1

    if symbols == 0:
        print("Password must contain at least one symbol character.")
        errors += 1

    # Seperator check
    separators = 0
    # set_of_seperators = set(r'.,;:_+-/~ ')  # How else do I fix this?
    separators_list = ['.', ',', ';', ':', '_', '+', '-', '/', '~', ' ']
    for separator in user:
        if separator in separators_list:
            separators += 1

    if separators != 0:
        print("Password cannot contain separator characters (space . , ; : _ + - / ~).")
        errors += 1

    # Amount of errors
    print("# of errors = ", errors)

    if errors == 0:
        loop = False

    errors = 0


print("Password created successfully!")

# OBSERVATIONS
# SyntaxWarning: invalid escape sequence '\]' if symbol in '!\"#$%&\'()*<=>?@[\]^`{|}':
# Never use string as a list of chars
