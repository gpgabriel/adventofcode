import math

input = "input.txt"

def correct_diff(a, b):
    return abs(a-b) >= 1 and abs(a-b) <= 3

def correct_order(a, b, ascending):
    if ascending:
        return a < b
    return a > b

def check_line(prev, line, ascending, budget):
    if len(line) == 0:
        return True
    x = line[0]

    # when the current element is not correct
    if not (correct_order(prev, x, ascending) and correct_diff(prev, x)):
        if budget == 0:
            return False
        return check_line(prev, line[1:], ascending, 0)
    
    # if the element is correct and we have budget, try to skip it anyways
    still_safe = False
    if budget > 0:
        still_safe |= check_line(prev, line[1:], ascending, 0)
    if not still_safe:
        still_safe |= check_line(line[0], line[1:], ascending, budget)
    return still_safe


    # for x in line:
    #     if correct_order(prev, x, ascending) and correct_diff(prev, x):
    #         prev = x
    #         continue
    #     if budget > 0:
    #         budget -= 1
    #         continue
    #     else:
    #         return False
    # return True

def is_safe(line):
    line = [int(x) for x in line.split(' ')]

    if check_line(line[0], line[1:], line[0] < line[1], 1):
        return True
    elif check_line(line[1], line[2:], line[1] < line[2], 0):
        return True
    elif check_line(line[0], line[2:], line[0] < line[2], 0):
        return True
    return False


with open(input) as f:
    print("solution:", sum([1 for line in f.readlines() if is_safe(line)]))
