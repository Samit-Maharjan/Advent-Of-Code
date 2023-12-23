import sys
sys.setrecursionlimit(10000)

data = open('input.txt', 'r').read().strip().split('\n')
moves = [1, 0, -1, 0, 1]
m, n, ans = len(data), len(data[0]), 0
slopes = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}

def backtrack(x, y, vis):
    global ans
    if x == m - 1 and y == n - 2:
        ans = max(ans, len(vis))
        return
    if data[x][y] in slopes:
        dx, dy = slopes[data[x][y]]
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
            if (nx, ny) in vis:
                return
            vis.add((nx, ny))
            backtrack(nx, ny, vis)
            vis.remove((nx, ny))
    else:
        for i in range(4):
            nx, ny = x + moves[i], y + moves[i + 1]
            if 0 <= nx < m and 0 <= ny < n and data[nx][ny] != '#':
                if (nx, ny) in vis:
                    continue
                vis.add((nx, ny))
                backtrack(nx, ny, vis)
                vis.remove((nx, ny))


backtrack(0, 1, set())
print(ans)
