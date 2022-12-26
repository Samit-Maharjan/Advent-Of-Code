monke = {}
data = open("input.txt").read().splitlines()
for line in data:
    X = line.split()
    X[0] = X[0][:-1]
    if len(X) > 2:
        monke[X[0]] = X[1:]
    else:
        monke[X[0]] = int(X[1])

def dfs(node):
    if isinstance(monke[node], int):
        return str(monke[node])
    a, op, b = monke[node]
    if op == '/':
        op += op
    return str(eval(dfs(a) + op + dfs(b) ) )
print(dfs('root'))
