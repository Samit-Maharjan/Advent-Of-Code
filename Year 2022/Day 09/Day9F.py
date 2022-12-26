data = open("input.txt").read().splitlines()
moves = {'L' : (0, -1), 'R': (0, 1), 'D': (1, 0), 'U' : (-1, 0)}
vis = [(0, 0)]
hx = hy = tx = ty = 0

def diagonal(x, y, nx, ny):
    g = [1, 1, -1, -1, 1]
    for i in range(4):
        if (x + g[i], y + g[i + 1]) == (nx, ny):
            return True
    return False

def adjacent(x, y, nx, ny):
    g = [1, 0, -1, 0, 1]
    for i in range(4):
        if (x + g[i], y + g[i + 1]) == (nx, ny):
            return True
    return False

for x in data:
    d, m = x.split()
    nx, ny = moves[d]
    for i in range(int(m) ):
        hx += nx; hy += ny
        if (tx, ty) == (hx, hy) or adjacent(tx, ty, hx, hy) or diagonal(tx, ty, hx, hy):
            continue
        tx, ty = hx - nx, hy - ny
        vis.append( (tx, ty) )
print(len(set(vis) ) )


