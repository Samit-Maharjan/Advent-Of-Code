data = open("input.txt").read().splitlines()
res = 0
m, n = len(data), len(data[0])
for i in range(1, m - 1):
    for j in range(1, n - 1):
        ok1 = ok2 = ok3 = ok4 = 0
        for k in range(i + 1, m):
            ok1 += 1
            if data[i][j] <= data[k][j]:
                break
        for k in range(i - 1, -1, -1):
            ok2 += 1
            if data[i][j] <= data[k][j]:
                break
        for k in range(j + 1, n):
            ok3 += 1
            if data[i][j] <= data[i][k]:
                break
        for k in range(j - 1, -1, -1):
            ok4 += 1
            if data[i][j] <= data[i][k]:
                break 
        res = max(res, ok1 * ok2 * ok3 * ok4)
print(res)
