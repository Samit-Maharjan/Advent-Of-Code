data, idx = open('input.txt', 'r').read().split('\n'), 0
seeds = list(map(int, data[idx].split(':')[-1].strip().split() ) )
idx += 3
maps = [{} for _ in range(7)]
for i in range(7):
    while data[idx]:
        d, s, r = map(int, data[idx].split() )
        maps[i][(s, s + r - 1)] = (d, d + r - 1)
        idx += 1
    idx += 2
ans = float('inf')
for x in seeds:
    for i in range(7):
        for (s, e), (ss, ee) in maps[i].items():
            if s <= x <= e:
                x = ss + (x - s)
                break
    ans = min(ans, x)
print(ans)
