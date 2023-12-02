data = open('input.txt', 'r').read().strip().split('\n')
dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
T = []
stars = []
for i, line in enumerate(data):
    A = []
    for j in range(len(line) ):
        if data[i][j] == '*':
            stars.append( (i, j) )
    j = 0
    while j < len(line):
        if line[j].isnumeric():
            cur = []
            while j < len(line) and line[j].isnumeric():
                cur.append( (i, j) )
                j += 1
            A.append(cur)
        else:
            j += 1
    for nums in A:
        ok = False
        for x, y in nums:
            for a, b in zip(dx, dy):
                nx, ny = x + a, y + b
                if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
                    ok |= data[nx][ny] == '*'
        cur = int(''.join(line[j] for _, j in nums) )
        if ok:
            T.append( (nums, cur) )
ans = 0
for x, y in stars:
    V = []
    for g, v in T:
        for a, b in zip(dx, dy):
            nx, ny = x + a, y + b
            if (nx, ny) in g:
                V.append(v)
                break
    if len(V) == 2:
        cur = 1
        for x in V:
            cur *= x
        ans += cur
print(ans)


