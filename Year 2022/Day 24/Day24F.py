dir = {'>': (0, +1), '<': (0, -1), 'v': (+1, 0), '^': (-1, 0)}
g = [1, 0, -1, 0, 1]
data = open("input.txt").read().splitlines()
m, n = len(data), len(data[0])
walls = set()
bliz = []
grid = []
for i, x in enumerate(data):
    for j, y in enumerate(x):
        if y == '#':
            walls.add( (i, j) )
        elif y in dir:
            bliz.append( (i, j, dir[y]) )
        else:
            grid.append( (i, j) )

start = (0, min(y for _, y in grid) )
goal = (m - 1, max(y for _, y in grid) )

walls.add( (-1, start[1]) )
walls.add( (m, goal[1]) )

q = {start}
res = 0
while goal not in q:
    res += 1
    nq = set()
    nbliz = []
    blizzes = set()
    for x, y, (dx, dy) in bliz:
        nx, ny = x + dx, y + dy
        if (nx, ny) in walls:
            while (nx - dx, ny - dy) not in walls:
                nx -= dx
                ny -= dy
        blizzes.add( (nx, ny) )
        nbliz.append( (nx, ny, (dx, dy) ) )
    bliz = nbliz
    for x, y in q:
        for i in range(4):
            nx, ny = x + g[i], y + g[i + 1]
            if (nx, ny) not in walls and (nx, ny) not in blizzes:
                nq.add( (nx, ny) )
        if (x, y) not in blizzes:
            nq.add( (x, y) )
    q = nq

print(res)
