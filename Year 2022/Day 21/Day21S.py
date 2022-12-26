monke = {}
data = open("input.txt").read().splitlines()
for line in data:
    X = line.split()
    X[0] = X[0][:-1]
    if len(X) > 2:
        monke[X[0]] = X[1:]
    else:
        monke[X[0]] = int(X[1])

def dfs(monkey):
    if isinstance(monke[monkey], int):
        return monke[monkey]
    a, op, b = monke[monkey]
    if op == '/':
        op += op
    return eval(str(dfs(a) ) + op + str(dfs(b) ) )

child1, child2 = monke['root'][::2]
l = 0
r = 10 ** 18
res = -1
while l <= r:
    mid = (l + r) >> 1
    monke['humn'] = mid
    left, right = dfs(child1), dfs(child2)
    if left == right:
        res = mid
        break
    # from observation -> less humn -> greater value of left child
    elif left > right:
        l = mid + 1
    else:
        r = mid - 1
print(res)

     
    
    
