from collections import defaultdict

data = open('input.txt', 'r').read().strip().split('\n')
moves = [1, 0, -1, 0, 1]
m, n = len(data), len(data[0])
for i in range(m):
    for x in '<>^v':
        data[i] = data[i].replace(x, '.')

vertices = set([(0, 1), (m - 1, n - 2)])
for i in range(m):
    for j in range(n):
        if data[i][j] == '#':
            continue
        cnt = 0
        for k in range(4):
            ni, nj = i + moves[k], j + moves[k + 1]
            if 0 <= ni < m and 0 <= nj < n and data[ni][nj] != '#':
                cnt += 1
        if cnt > 2:
            vertices.add((i, j))

graph = defaultdict(list)
for x, y in vertices:
    q = [(x, y)]
    vis = set(q)
    dist = 0
    while q:
        nq = []
        dist += 1
        for xx, yy in q:
            for i in range(4):
                nx, ny = xx + moves[i], yy + moves[i + 1]
                if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
                    if (nx, ny) in vis:
                        continue
                    vis.add((nx, ny))
                    if (nx, ny) in vertices:
                        graph[(x, y)].append((dist, (nx, ny)))
                    else:
                        nq.append((nx, ny))
        q = nq          
ans = 0
def backtrack(x, y, dist, vis):
    global ans
    if x == m - 1 and y == n - 2:
        ans = max(ans, dist)
        return
    for d, (nx, ny) in graph[(x, y)]:
        if (nx, ny) in vis:
            continue
        vis.add((nx, ny))
        backtrack(nx, ny, dist + d, vis)
        vis.remove((nx, ny))
        
backtrack(0, 1, 0, set())
print(ans)
