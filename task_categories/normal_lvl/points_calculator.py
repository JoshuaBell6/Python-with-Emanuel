# TASK: Write the code to calculate the soccer match points based on the given scores.

"""
Rules:
    X = team 1 score
    Y = team 2 score
    [X:Y, X:Y]
    X > Y = 3 points
    X == Y = 1 point
    X < Y = 0 points
    Calculate score only for team X
"""

scores = ["1:2", "0:0", "3:2", "1:0", "0:1", "4:1"]

# Don't change the code above this line


def calculate_points(scores):  # Only works when both scores are single digit
    # TODO: fix the function so that both tests work
    # points = 0
    # for i in scores:
    #     if int(i[0]) > int(i[-1]):
    #         points += 3
    #     elif int(i[0]) == int(i[-1]):
    #         points += 1
    # return points

    points = 0
    for score in scores:        
        x, y = map(int, score.split(':'))
        
        if x > y:
            points +=3
        elif x == y:
            points += 1
        
    return points 


# Don't change the code below this line
scores2 = ["11:2", "0:13", "11:19", "10:0", "13:13", "12:11"]

if calculate_points(scores) == 10 and calculate_points(scores2) == 10:
    print('TASK IS COMPLETE!')
else:
    print("Task failed! Try again.")
