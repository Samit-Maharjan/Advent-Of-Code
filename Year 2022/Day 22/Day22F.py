import re
data, moves = open("input.txt").read().split('\n\n')
data = data.splitlines()

start = (-1, -1)
grid = {}
for i, x in enumerate(data, start = 1):
    for j, y in enumerate(x, start = 1):
        if y in '.#':
            if start == (-1, -1):
                start = (i, j)
            grid[i, j] = y
moves = re.findall(r'(\d+)(L|R)*', moves)

dir = {(0, 1) : 0, (1, 0) : 1, (0, -1) : 2, (-1, 0) : 3}

# facing right
dx, dy = 0, 1
for move in moves:
    for _ in range(int(move[0]) ):
        x, y = start
        nx, ny = x + dx, y + dy
        if (nx, ny) not in grid:
            nnx, nny = x, y
            while (nnx, nny) in grid:
                nx, ny = nnx, nny
                nnx -= dx
                nny -= dy
        if grid[nx, ny] == '#':
            break
        start = (nx, ny)
    if move[1] == 'L':
        dx, dy = -dy, dx
    elif move[1] == 'R':
        dx, dy = dy, -dx

x, y = start
print(1000 * x + 4 * y + dir[dx, dy]) # type: ignore

