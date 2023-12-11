data = open('input.txt', 'r').read().strip().split('\n')
empty_rows = []
for i, line in enumerate(data):
    if '#' not in line:
        empty_rows.append(i)
empty_cols = []
for j in range(len(data[0]) ):
    cur = str()
    for i in range(len(data) ):
        cur += data[i][j]
    if '#' not in cur:
        empty_cols.append(j)
points = []
for i in range(len(data) ):
    for j in range(len(data[0]) ):
        if data[i][j] == '#':
            points.append( (i, j) )
ans, offset = 0, 999999
for i in range(len(points) - 1):
    for j in range(i + 1, len(points) ):
        (x, y), (xx, yy) = points[i], points[j]
        for row in empty_rows:
            if min(x, xx) < row < max(x, xx):
                ans += offset
        for col in empty_cols:
            if min(y, yy) < col < max(y, yy):
                ans += offset
        ans += abs(xx - x) + abs(yy - y)
print(ans)


