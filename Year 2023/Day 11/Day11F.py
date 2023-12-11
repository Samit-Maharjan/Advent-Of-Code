data = open('input.txt', 'r').read().strip().split('\n')
ndata = []
for line in data:
    ndata.append(line)
    if '#' not in line:
        ndata.append(line)
j = 0
while j < len(ndata[0]):
    cur = str()
    for i in range(len(ndata) ):
        cur += ndata[i][j]
    if '#' not in cur:
        for i in range(len(ndata) ):
            row = str()
            for k in range(len(ndata[i]) ):
                row += ndata[i][k]
                if j == k:
                    row += '.'
            ndata[i] = row
        j += 1
    j += 1
points = []
for i in range(len(ndata) ):
    for j in range(len(ndata[0]) ):
        if ndata[i][j] == '#':
            points.append( (i, j) )
ans = 0
for x, y in points:
    for xx, yy in points:
        ans += abs(x - xx) + abs(y - yy)
print(ans // 2)




