# TASK: Write a function that extracts the individual red, green, and blue (RGB) component values for a color.
"""
Rules:
    - The function should accept case insensitive hexadecimal color string
    - Return value of the function is a dictionary (see example)
    - 
Example:
    input -> #ffffff
    output -> {'r': 255, 'g': 255, 'b': 255}
"""


def hex_to_rgb(hex):
    return {}

# Don't change the code below this line


hex1 = "#ff9933"
hex2 = "#43934a"
if hex_to_rgb(hex1) == {"r": 255, "g": 153, "b": 51} and hex_to_rgb(hex2) == {"r": 67, "g": 147, "b": 74}:
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
