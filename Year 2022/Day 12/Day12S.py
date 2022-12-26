data = open("input.txt").read().splitlines()
m, n = len(data), len(data[0])
grid = {}
start = None
end = None
for i, x in enumerate(data):
    for j, y in enumerate(x):
        grid[i, j] = ord(y)
        if y == 'S':
            start = (i, j)
        if y == 'E':
            end = (i, j)

grid[start] = ord('a')
grid[end] = ord('z')
dir = [1, 0, -1, 0, 1]

vis = set()
res = 0
q = {end}

while not any(grid[x, y] == ord('a') for x, y in q): #type: ignore
    res += 1
    nq = set()
    for x, y in q: #type: ignore
        vis.add( (x, y) )
        for i in range(4):
            nx, ny = x + dir[i], y + dir[i + 1]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and grid[x, y] - grid[nx, ny] <= 1:
                nq.add( (nx, ny) )
    q = nq
print(res)
