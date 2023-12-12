from functools import cache
data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for line in data:
    pattern, count = line.split()
    count = list(map(int, count.split(',') ) )
    @cache
    def backtrack(p_idx, c_idx):
        if c_idx == len(count):
            return '#' not in pattern[p_idx:]
        cnt = count[c_idx]
        occupied = sum(count[c_idx + 1:])
        occupied += len(count) - 1 - c_idx

        ans = 0
        rem = len(pattern) - p_idx
        for x in range(rem - occupied - cnt + 1):
            cur = '.' * x + '#' * cnt + '.'
            good = True
            for i, j in zip(cur, pattern[p_idx: p_idx + len(cur)]):
                good &= (i == j) or (j == '?')
            if good:
                ans += backtrack(p_idx + len(cur), c_idx + 1)
        return ans            
    npattern = pattern
    for x in range(4):
        npattern += '?' + pattern
    pattern, count = npattern, tuple(count * 5)
    ans += backtrack(0, 0)
print(ans)
