data = open('input.txt', 'r').read().strip().split('\n')
dx = [0, 1, 0, -1, 1, -1, 1, -1]
dy = [1, 0, -1, 0, 1, -1, -1, 1]
ans = 0
for i, line in enumerate(data):
    A = []
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
                    ok |= data[nx][ny] != '.' and not data[nx][ny].isnumeric()
        ans += int(''.join(line[j] for _, j in nums) ) * ok
print(ans)
