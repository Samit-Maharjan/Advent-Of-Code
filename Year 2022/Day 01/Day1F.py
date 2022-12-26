data = open('input.txt', 'r').read().split('\n')
res = cur = 0
for x in data:
    if not len(x):
        res = max(res, cur)
        cur = 0
    else:
        cur += int(x)
res = max(res, cur)
print(res)
