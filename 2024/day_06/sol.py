directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def legal(data, x, y):
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return False
    return True

def find_cursor(data):
    for idx, x in enumerate(data):
        for idy, y in enumerate(x):
            if y == '^':
                return (idx, idy)

def forms_loop(data, x, y, d):
    global directions
    visited = {}

    while True:
        visited.update({f"{x}.{y}": visited.get(f"{x}.{y}", []) + [d]})

        cx = x + directions[d][0]
        cy = y + directions[d][1]

        if not legal(data, cx, cy):
            return False

        if data[cx][cy] == '#':
            d = (d + 1) % len(directions)
            continue

        if d in visited.get(f"{cx}.{cy}", []):
            return True

        x = cx
        y = cy


def sol(data):
    global directions
    (originalX, originalY) = find_cursor(data)
    
    d = 0
    # total_visited = 0
    # while legal(data, x, y):
    #     if data[x][y] in ['.', '^']:
    #         total_visited += 1
    #     data[x][y] = 'X'

    #     cx = x + directions[d][0]
    #     cy = y + directions[d][1]

    #     if not legal(data, cx, cy):
    #         break

    #     if data[cx][cy] == '#':
    #         d = (d + 1) % len(directions)
    #         continue

    #     x = cx
    #     y = cy

    total_loops = 0
    for idx, x in enumerate(data):
        for idy, y in enumerate(x):
            if y == '.':
                print(f"trying {idx},{idy}")
                data[idx][idy] = '#'
                if forms_loop(data, originalX, originalY, 0):
                    total_loops += 1
                data[idx][idy] = '.'

    print('\n'.join([''.join(x) for x in data]))
    return total_loops

print(sol([list(x.strip()) for x in open('input.txt').readlines()]))