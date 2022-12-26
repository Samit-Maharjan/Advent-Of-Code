N = 600
grid = [['.' for _ in range(N + 1)] for _ in range(N + 1)]
data = [ x.split('->') for x in open("input.txt").read().splitlines()]
for x in data:
    A = [list(map(int, i.split(',') ) ) for i in x]
    y, x = A[0]
    for j, i in A[1:]:
        if x == i:
            a, b = min(y, j), max(y, j) + 1
            for k in range(a, b):
                grid[x][k] = '#'
        elif y == j:
            a, b = min(x, i), max(x, i) + 1
            for k in range(a, b):
                grid[k][y] = '#'
        x, y = i, j

def dfs(x, y):
    if x == N or y == N:
        return True
    if grid[x + 1][y] == '.':
        return dfs(x + 1, y)
    elif y > 0 and grid[x + 1][y - 1] == '.':
        return dfs(x + 1, y - 1)
    elif y < N and grid[x + 1][y + 1] == '.':
        return dfs(x + 1, y + 1)
    else:
        grid[x][y] = 'o'
    return False


cnt = 0
while not dfs(0, 500):
    cnt += 1

for i in range(100):
    for j in range(450, 550):
        print(grid[i][j], end = '')
    print()
print(cnt)  
