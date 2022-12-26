data = open("input.txt").read().split('\n\n')
monke = [[] for _ in range(len(data) )]
op = [[] for _ in range(len(data))]
div =[0 for _ in range(len(data) ) ]
throw = [[] for _ in range(len(data) )]
for x in data:
    A = x.split('\n')
    index = int(A[0].split()[1][:-1])
    monke[index] += [int(x[:-1] if x[-1] == ',' else x) for x in A[1].split()[2:]]
    op[index] = [x for x in A[2].split()[-2:]]
    div[index] = int(A[3].split()[-1])
    throw[index] = list(int(A[i].split()[-1]) for i in [4, 5])

def operate(index, val):
    a = val if op[index][1] == 'old' else int(op[index][1])
    if op[index][0] == '*':
        return a * val
    else:
        return a + val

res = [0 for _ in range(len(data) )]
for i in range(20):
    for j in range(len(data) ):
        res[j] += len(monke[j])
        for x in monke[j]:
            val = (operate(j, x) ) // 3

            if val % div[j]:
                monke[throw[j][1]].append(val)
            else:
                monke[throw[j][0]].append(val)
        monke[j].clear()
res.sort()
print(res[-1] * res[-2])
            
            






