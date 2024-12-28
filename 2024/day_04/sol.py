
xmas = "XMAS"
directions = [
    (1, 0),
    (0, 1),
    (1, 1),
    (-1, -1),
    (-1, 0),
    (0, -1),
    (1, -1),
    (-1, 1),
]

def legal_move(data, x, y):
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return False
    return True

def explore_direction(data, x, y, xx, yy, step):
    if step >= len(xmas):
        return 1
    if not legal_move(data, x, y):
        return 0
    if data[x][y] == xmas[step]:
        return explore_direction(data, x+xx, y+yy, xx, yy, step+1)
    return 0

def get_char(data, x, y):
    if not legal_move(data, x, y):
        return ''
    return data[x][y]

def sol(data):
    count = 0
    for idx, x in enumerate(data):
        for idy, y in enumerate(x):
            # for d in directions:
            #     count += explore_direction(data, idx, idy, d[0], d[1], 0)
            if y == 'A' and (sorted([
                    get_char(data, idx + 1, idy + 1),
                    get_char(data, idx - 1, idy - 1),
                ]) == ['M', 'S']) and (sorted([
                    get_char(data, idx + 1, idy - 1),
                    get_char(data, idx - 1, idy + 1),
                ]) == ['M', 'S']):
                count += 1

    return count

print(sol(open('input.txt').readlines()))
