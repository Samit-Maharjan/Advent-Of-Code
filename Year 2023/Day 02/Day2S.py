data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for idx, line in enumerate(data, start = 1):
    sets = line.split(':')[1].split(';')
    d = {'red': 0, 'green': 0, 'blue': 0}
    for each_set in sets:
        each_set = each_set.split(',')
        for each_color in each_set:
            v, c = each_color.strip().split()
            d[c] = max(d[c], int(v) )
    ans += d['red'] * d['green'] * d['blue']
print(ans)
