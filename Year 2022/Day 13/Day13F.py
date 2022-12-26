data = open("input.txt").read().split('\n\n')
res = 0
def cmp(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int:
        a = [a]
    if type(b) == int:
        b = [b]
    for x, y in zip(a, b):
        if res := cmp(x, y):
            return res
    return cmp(len(a), len(b) )

res = 0
for i, x in enumerate(data, 1):
    a, b = (eval(i) for i in x.splitlines() )
    if cmp(a, b) < 0:
        res += i
print(res)


