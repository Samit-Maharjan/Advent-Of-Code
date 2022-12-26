data = open("input.txt").read().splitlines()
moves = {'L' : (0, -1), 'R': (0, 1), 'D': (1, 0), 'U' : (-1, 0)}
vis = set()
hx = hy = 0
t = [[0, 0] for _ in range(9)]
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
        hx, hy = hx + nx, hy + ny
        px, py = hx, hy
        for j in range(9):
            tx, ty = t[j]
            if (tx, ty) == (px, py)  or diagonal(tx, ty, px, py) or adjacent(tx, ty, px, py):
                break
            if abs(tx - px) > 1 and ty == py:
                tx += [-1, 1][tx < px]
            elif abs(ty - py) > 1 and tx == px:
                ty += [-1, 1][ty < py]
            else:
                tx += [-1, 1][tx < px]
                ty += [-1, 1][ty < py]
            t[j] = [tx, ty]
            px, py = tx, ty
        vis.add(tuple(t[-1]))
print(len(vis))

                



