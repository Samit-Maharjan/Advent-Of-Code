data = open('input.txt', 'r').read().strip().split('\n')
m, n, ans = len(data), len(data[0]), 0
moves = [1, 0, -1, 0, 1]

for i in range(m):
    for j in range(n):
        if data[i][j] == 'S':
            q = [(i, j)]
            for _ in range(64):
                nq, vis = [], set()
                for x, y in q:
                    for k in range(4):
                        nx, ny = x + moves[k], y + moves[k + 1]
                        if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
                            if (nx, ny) in vis:
                                continue
                            vis.add((nx, ny))
                            nq.append((nx, ny))
                q = nq
                ans = len(vis)
print(ans)
