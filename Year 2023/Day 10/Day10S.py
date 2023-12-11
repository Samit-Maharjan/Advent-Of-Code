from collections import deque
data = open('input.txt', 'r').read().strip().split('\n')
m, n = len(data), len(data[0])
sym = {'|', '-', 'L', 'J', '7', 'F'}
x, y, border = 0, 0, []
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'S':
            x, y = i, j
            border.append( (x, y) )
px, py, dx, dy = x + 1, y, 1, 0
border.append( (px, py) )
def move(x, y, dx, dy):
    if data[x][y] == '|':
        x += dx
        dy = 0
    elif data[x][y] == '-':
        y += dy
        dx = 0
    elif data[x][y] == 'L':
        if dx == 1:
            y += 1
            dx, dy = 0, 1
        else:
            x -= 1
            dx, dy = -1, 0
    elif data[x][y] == 'J':
        if dx == 1:
            y -=1
            dx, dy = 0, -1
        else:
            x -= 1
            dx, dy = -1, 0
    elif data[x][y] == '7':
        if dx == -1:
            y -= 1
            dx, dy = 0, -1
        else:
            x += 1
            dx, dy = 1, 0
    elif data[x][y] == 'F':
        if dx == -1:
            y += 1
            dx, dy = 0, 1
        else:
            x += 1
            dx, dy = 1, 0
    return x, y, dx, dy
while data[px][py] != 'S':
    px, py, dx, dy = move(px, py, dx, dy)
    border.append( (px, py) )

# Shoelace formula
lattice_points_area = 0
for i in range(len(border) - 1):
    x1, y1 = border[i]
    x2, y2 = border[i + 1]
    lattice_points_area += x1 * y2 - x2 * y1
lattice_points_area >>= 1

# Pick's Theorem
lattice_points_perimeter = len(border) - 1
print(lattice_points_area - lattice_points_perimeter // 2 + 1)
