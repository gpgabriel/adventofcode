def legal(data, x, y):
    if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]):
        return False
    return True

def calc_antinodes(data, x, y):
    absx = abs(x[0] - y[0])
    absy = abs(x[1] - y[1])

    antinodes = []
    while legal(data, x[0], y[0]):
        if x[0] < y[0]:
            if x[1] < y[1]:
                x = (x[0] - absx, x[1] - absy)
            else:
                x = (x[0] - absx, x[1] + absy)
        else:
            if x[1] < y[1]:
                x = (x[0] + absx, x[1] - absy)
            else:
                x = (x[0] + absx, x[1] + absy)
        if legal(data, x[0], x[1]):
            antinodes += [x]

    return antinodes

def sol(data):
    h = {}
    for idx, x in enumerate(data):
        for idy, y in enumerate(x):
            if y != '.':
                h.update({y: h.get(y, []) + [(idx, idy)]})
    
    total = {}
    total_valid = 0
    for elem in h:
        if len(h[elem]) > 1:
            for x in h[elem]:
                total[f"{x[0]}.{x[1]}"] = 1

        for i in range(len(h[elem]) - 1):
            for j in range(i+1, len(h[elem])):
                for a in calc_antinodes(data, h[elem][i], h[elem][j]) + calc_antinodes(data, h[elem][j], h[elem][i]):
                    total[f"{a[0]}.{a[1]}"] = 1
                    data[a[0]][a[1]] = '#'

    print('\n'.join([''.join(x) for x in data]))
    return len(total) + total_valid

data = [list(x.strip()) for x in open('input.txt').readlines()]
print(sol(data))