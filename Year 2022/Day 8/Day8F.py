data = open("input.txt").read().splitlines()
res = 0
m, n = len(data), len(data[0])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        ok1 = ok2 = ok3 = ok4 = True
        for k in range(i + 1, m):
            if data[i][j] <= data[k][j]:
                ok1 = False
        for k in range(i):
            if data[i][j] <= data[k][j]:
                ok2 = False
        for k in range(j + 1, n):
            if data[i][j] <= data[i][k]:
                ok3 = False
        for k in range(j):
            if data[i][j] <= data[i][k]:
                ok4 = False
        res += ok1 or ok2 or ok3 or ok4

res += len(data) * 2 + (len(data[0]) - 2) * 2
print(res)
