data = open("input.txt").read().split('\n')
res = 0
for x in data:
    a, b = x.split(',')
    a1, a2 = [int(y) for y in a.split('-')]
    b1, b2 = [int(y) for y in b.split('-')]
    if a2 < b1 or b2 < a1:
        continue
    res += 1
print(res)
    
