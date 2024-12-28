def sol(data):
    res = 0
    idx = 0
    k = int(len(data) / 2) * 2

    for i in range(len(data)):
        while data[i]:
            if i % 2 == 0:
                res += (idx * (i/2))
            if i % 2 == 1:
                while data[k] == 0 and k > 0:
                    k -= 2
                if k <= i:
                    break
                res += (idx * (k/2))
                data[k] -= 1
            data[i] -= 1
            idx += 1

    return int(res)

print(sol([int(x) for x in list(open('input.txt').readline())]))
