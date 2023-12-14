data = open('input.txt', 'r').read().strip().split('\n')
m, n = len(data), len(data[0])
ndata = [['.'] * n for _ in range(m)]
for j in range(n):
    to_place = 0
    for i in range(m):
        if data[i][j] == '#':
            ndata[i][j] = '#'
            to_place = i + 1
        elif data[i][j] == 'O':
            ndata[to_place][j] = 'O'
            to_place += 1
print(sum(m - i for i in range(m) for j in range(n) if ndata[i][j] == 'O') )
