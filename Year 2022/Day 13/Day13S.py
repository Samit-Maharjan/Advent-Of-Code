import functools as ft
def cmp(a, b):
    match a, b:
        case int(), int():
            return a - b
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            for x, y in zip(a, b):
                # if equal keep checking
                if cur := cmp(x, y):
                    return cur
    return len(a) - len(b)
to_add = [[[2]], [[6]]]
data = [list(map(eval, x.splitlines() ) ) for x in open("input.txt").read().split('\n\n')]
A = []
for x in data:
    for y in x:
        A.append(y)
A += to_add
A.sort(key = ft.cmp_to_key(cmp) )
a, b = A.index(to_add[0]) + 1, A.index(to_add[1]) + 1
print(a * b)


        








    
