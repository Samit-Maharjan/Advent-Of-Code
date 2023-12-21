data = open('input.txt', 'r').read().strip().split('\n')
m, n, ans = len(data), len(data[0]), 0
moves = [1, 0, -1, 0, 1]
TIMES = 26501365


def solve(times):
    for i in range(m):
        for j in range(n):
            if data[i][j] == 'S':
                q = [(i, j)]
                for _ in range(times):
                    nq, vis = [], set()
                    for x, y in q:
                        for k in range(4):
                            nx, ny = x + moves[k], y + moves[k + 1]
                            px, py = (nx % m + m) % m, (ny % n + n) % n
                            if data[px][py] != '#':
                                if (nx, ny) in vis:
                                    continue
                                vis.add((nx, ny))
                                nq.append((nx, ny))
                        q = nq
                    ans = len(vis)
    return ans


v1 = solve(65)
v2 = solve(65 + 131 * 1)
v3 = solve(65 + 131 * 2)

x = TIMES // n
d1, d2, d3 = v1, v2 - v1, v3 - v2

# Newton's Polynomial Interpolation
print(d1 + d2 * x + x * (x - 1) * (d3 - d2) // 2)
