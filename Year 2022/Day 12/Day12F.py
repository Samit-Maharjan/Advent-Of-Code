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

res = 0
vis = set()
q = {start}
while end not in q:
    res += 1
    nq = set()
    for x, y in q: #type: ignore
        vis.add( (x, y) )
        for i in range(4):
            nx, ny = x + dir[i], y + dir[i + 1]
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in vis and grid[nx, ny] - grid[x, y] <= 1:
                nq.add( (nx, ny) )
    q = nq
print(res)


