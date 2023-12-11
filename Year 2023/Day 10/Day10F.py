data = open('input.txt', 'r').read().strip().split('\n')
m, n = len(data), len(data[0])
sym = {'|', '-', 'L', 'J', '7', 'F'}
x, y = 0, 0
for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == 'S':
            x, y = i, j
px, py, dx, dy = x + 1, y, 1, 0
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
ans = 1
while data[px][py] != 'S':
    px, py, dx, dy = move(px, py, dx, dy)
    ans += 1
print(ans // 2)
