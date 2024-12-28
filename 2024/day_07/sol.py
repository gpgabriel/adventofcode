
def check(target, current, numbers):
    if len(numbers) == 0:
        return target == current
    if current > target:
        return False
    return check(target, current * numbers[0], numbers[1:]) or check(target, current + numbers[0], numbers[1:]) or check(target, int(str(current) + str(numbers[0])), numbers[1:])

def sol(line):
    [left, right] = line.split(':')
    target = int(left)
    numbers = [int(x) for x in right.strip().split(' ')]
    
    if check(target, numbers[0], numbers[1:]):
        return target
    return 0

print(sum([sol(x.strip()) for x in open('input.txt').readlines()]))