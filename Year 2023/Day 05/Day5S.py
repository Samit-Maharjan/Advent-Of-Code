data, idx = open('input.txt', 'r').read().split('\n'), 0
seeds = list(map(int, data[idx].split(':')[-1].strip().split() ) )
seed_ranges = [(x, x + y - 1) for x, y in zip(seeds[::2], seeds[1::2])]
idx += 3
maps = [{} for _ in range(7)]
for i in range(7):
    while data[idx]:
        d, s, r = map(int, data[idx].split() )
        maps[i][(s, s + r - 1)] = (d, d + r - 1)
        idx += 1
    idx += 2
n = ans = 1
while True:
    ans = n
    for i in reversed(range(7) ):
        for (s, e), (ss, ee) in maps[i].items():
            if ss <= n <= ee:
                n = s + (n - ss)
                break
    if any(x <= n <= y for x, y in seed_ranges):
        break
    n = ans + 1
print(ans)
