from heapq import heappush, heappop

data = open('input.txt', 'r').read().strip().split('\n')
data = [[int(y) for y in x] for x in data]
m, n = len(data), len(data[0])
pq, costs = [(0, 0, 0, '.')], {}
rev = {'r': 'l', 'l': 'r', 'u': 'd', 'd': 'u'}
move = {'r': (0, 1), 'l': (0, -1), 'u': (-1, 0), 'd': (1, 0)}
while pq:
    cost, x, y, d = heappop(pq)
    if x == m - 1 and y == n - 1:
        print(cost)
        break
    for dd in 'rlud':
        if dd == d or rev.get(d, '.') == dd:
            continue
        dc = 0
        for i in range(1, 4):
            nx, ny = x + i * move[dd][0], y + i * move[dd][1]
            if 0 <= nx < m and 0 <= ny < n:
                dc += data[nx][ny]
                if costs.get( (nx, ny, dd), float('inf') ) > cost + dc:
                    costs[(nx, ny, dd)] = cost + dc
                    heappush(pq, (cost + dc, nx, ny, dd) )
