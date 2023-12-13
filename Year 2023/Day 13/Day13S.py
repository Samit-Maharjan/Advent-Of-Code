data = open('input.txt', 'r').read().strip().split('\n\n')
left = up = 0
def check(line, idx, length):
    l, r = idx, idx + 1
    while l >= 0 and r < length:
        if line[l] != line[r]:
            break
        l, r = l - 1, r + 1
    return (l < 0 or r == length)

def solve(pattern):
    m, n = len(pattern), len(pattern[0])
    h_m = [set() for _ in range(m)]
    for i, x in enumerate(pattern):
        for j in range(n):
            if check(x, j, n):
                h_m[i].add(j)
    v_m = [set() for _ in range(n)]
    T = list(zip(*pattern) )
    for i, x in enumerate(T):
        for j in range(m):
            if check(x, j, m):
                v_m[i].add(j)
    mx, my = {*range(n - 1)}, {*range(m - 1)}
    for x in h_m:
        mx = mx.intersection(x)
    for x in v_m:
        my = my.intersection(x)
    return mx, my
    
for pattern in data:
    pattern = [list(x) for x in pattern.split('\n')]
    m, n = len(pattern), len(pattern[0])
    mx, my = solve(pattern)
    l, u = set(), set()
    for i in range(m):
        for j in range(n):
            cur = pattern[i][j]
            if pattern[i][j] == '#':
                pattern[i][j] = '.'
            else:
                pattern[i][j] = '#'
            mmx, mmy = solve(pattern)
            if mmy and my != mmy:
                u.add(sum(mmy - my) + 1)
            if mmx and mx != mmx:
                l.add(sum(mmx - mx) + 1)
            pattern[i][j] = cur
    up, left = up + sum(u), left + sum(l)
print(left + 100 * up)
