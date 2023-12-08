from math import gcd
data = open('input.txt', 'r').read().strip().split('\n')
inst, graph, start = data[0], {}, []
for line in data[2:]:
    node, child = line.split(' =')
    left, right = child.strip()[1:-1].split(', ')
    graph[node] = (left, right)
    if node[-1] == 'A':
        start.append(node)
values = []
for x in start:
    node, cnt, idx = x, 0, 0
    while node[-1] != 'Z':
        l, r = graph[node]
        if inst[idx] == 'L':
            node = l
        else:
            node = r
        idx = (idx + 1) % len(inst)
        cnt += 1
    values.append(cnt)
ans = 1
for x in values:
    ans = ans * x // gcd(ans, x)
print(ans)
