def find_next_i(data):
    i = int(len(data) / 2) * 2
    while i > 0 and data[i] == 0:
        i -= 2
    return int(i)

def sol(data):
    res = 0
    idx = 0

    for i in range(len(data)):
        while data[i]:
            if i % 2 == 0:
                res += (idx * (i/2))
            if i % 2 == 1:
                # nit: find_next_i could be optimised
                k = find_next_i(data)
                if k <= i:
                    break
                res += (idx * (k/2))
                data[k] -= 1
            data[i] -= 1
            idx += 1

    return int(res)

print(sol([int(x) for x in list(open('input.txt').readline())]))
