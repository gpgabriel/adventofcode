import re

# 79037122

bypass = False

def sol(line):
    global bypass
    x = 0
    for res in re.findall(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(don't\(\))|(do\(\))", line):
        if res[2] == "don't()":
            bypass = True
        elif res[3] == "do()":
            bypass = False
        elif not bypass:
            x += int(res[0]) * int(res[1])
    return x

with open('test.txt') as f:
    print(sum([sol(x) for x in f.readlines()]))
