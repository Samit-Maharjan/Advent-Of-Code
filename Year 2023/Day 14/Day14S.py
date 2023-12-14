data = open('input.txt', 'r').read().strip().split('\n')
data = list(list(x) for x in data)
m, n = len(data), len(data[0])
TIMES = 10 ** 9
def spin(data):
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
    data = ndata[:]
    ndata = [['.'] * n for _ in range(m)]
    for i in range(m):
        to_place = 0
        for j in range(n):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = j + 1
            elif data[i][j] == 'O':
                ndata[i][to_place] = 'O'
                to_place += 1
    data = ndata[:]
    ndata = [['.'] * n for _ in range(m)]
    for j in range(n):
        to_place = m - 1
        for i in reversed(range(m) ):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = i - 1
            elif data[i][j] == 'O':
                ndata[to_place][j] = 'O'
                to_place -= 1
    data = ndata[:]
    ndata = [['.'] * n for _ in range(m)]
    for i in range(m):
        to_place = n - 1
        for j in reversed(range(n) ):
            if data[i][j] == '#':
                ndata[i][j] = '#'
                to_place = j - 1
            elif data[i][j] == 'O':
                ndata[i][to_place] = 'O'
                to_place -= 1
    return ndata
recur, ndata = {}, data
for x in range(TIMES):
    ndata = spin(ndata)
    t_data = tuple(tuple(x) for x in ndata)
    if t_data in recur:
        diff = x - recur[t_data]
        TIMES = (TIMES - x) % diff - 1
        break
    recur[t_data] = x
for x in range(TIMES):
    ndata = spin(ndata)
print(sum(m - i for i in range(m) for j in range(n) if ndata[i][j] == 'O') )
