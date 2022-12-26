data = open("input.txt").read().split('\n')
res = 0
for x in data:
    a, b = x.split(',')
    a1, a2 = [int(y) for y in a.split('-')]
    b1, b2 = [int(y) for y in b.split('-')]
    if a1 <= b1 and a2 >= b2:
        res += 1
    elif a1 >= b1 and a2 <= b2:
        res += 1
print(res)
    
