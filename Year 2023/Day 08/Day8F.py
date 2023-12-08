data = open('input.txt', 'r').read().strip().split('\n')
inst, graph = data[0], {}
for line in data[2:]:
    node, child = line.split(' =')
    left, right = child.strip()[1:-1].split(', ')
    graph[node] = (left, right)
node = 'AAA'
ans = idx = 0
while node != 'ZZZ':
    l, r = graph[node]
    if inst[idx] == 'L':
        node = l
    else:
        node = r
    idx = (idx + 1) % len(inst)
    ans += 1
print(ans)


