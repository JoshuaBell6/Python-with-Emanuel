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
    decimal = [0, 0, 0]
    start, end, position = 1, 3, 2
    for k in range(3):
        for digit in range(start, end):
            #print("DIGIT", digit)
            if hex[digit].lower() == 'a':
                decimal[k] += 10 * 16 ** (position - int(digit))
            elif hex[digit].lower() == 'b':
                decimal[k] += 11 * 16 ** (position - int(digit))
            elif hex[digit].lower() == 'c':
                decimal[k] += 12 * 16 ** (position - int(digit))
            elif hex[digit].lower() == 'd':
                decimal[k] += 13 * 16 ** (position - int(digit))
            elif hex[digit].lower() == 'e':
                decimal[k] += 14 * 16 ** (position - int(digit))
            elif hex[digit].lower() == 'f':
                decimal[k] += 15 * 16 ** (position - int(digit))
            else:
                decimal[k] += int(hex[digit]) * 16 ** (position - int(digit))
        
        start += 2
        end += 2
        position += 2
           
    result = {
        'r' : decimal[0],
        'g' : decimal[1],
        'b' : decimal[2]
    }

    return result

# Don't change the code below this line


hex1 = "#ff9933"
hex2 = "#43934a"
if hex_to_rgb(hex1) == {"r": 255, "g": 153, "b": 51} and hex_to_rgb(hex2) == {"r": 67, "g": 147, "b": 74}:
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
