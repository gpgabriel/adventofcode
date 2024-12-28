import functools

data = [x.strip() for x in  open('input.txt').readlines()]
split = data.index("")

page_ordering = data[:split]
updates = data[split+1:]

h = {}
for x in page_ordering:
    [a, b] = x.split('|')
    h.update({a: h.get(a, []) + [b]})

res = 0

def compare(a, b):
    global h
    for x in h.get(a, []):
        if x == b:
            return -1
    return 1

for line in updates:
    found = {}
    items = line.split(',')
    correct = True
    for x in items:
        for y in h.get(x, []):
            if found.get(y, False):
                correct = False
                break
        found[x] = True
    if not correct:
        # res += int(items[int(len(items)/2)])
        items = sorted(items, key=functools.cmp_to_key(compare))
        print(items)
        res += int(items[int(len(items)/2)])
print(res)
