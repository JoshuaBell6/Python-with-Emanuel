# This is your first task. Yay!
# TASK: Create 3 variables with string values to match the print statement

"""
Don't change the code above this line
"""

# Write missing code here
var1 = 'Hello world,'
var2 = 'I am a'
var3 = 'programmer'

"""
Don't change the code below this line
"""
print(var1, var2, var3)

# Expected console result: Hello world, I am a programmer


def check_hello_world_task(v1, v2, v3):
    print('--------------------')
    if (f"{v1} {v2} {v3}" == "Hello world, I am a programmer"):
        print('TASK IS COMPLETE!')
    else:
        print("Task failed! Try again.")


check_hello_world_task(var1, var2, var3)
