data = open("input.txt").read().split('\n')
res = 0
for x in data:
    mp = set()
    for i in range(len(x) // 2):
        mp.add(x[i])
    for i in range(len(x) // 2, len(x) ):
        if x[i] in mp:
            if ord(x[i]) < ord('a'):
                res += 27 + ord(x[i]) - ord('A')
            else:
                res += 1 + ord(x[i]) - ord('a')
            break
print(res)
