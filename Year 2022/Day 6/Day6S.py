x = open("input.txt").read()
s = set()
l = 0
for r in range(len(x) ):
    while x[r] in s:
        s.remove(x[l])
        l += 1
    s.add(x[r])
    if len(s) == 14:
        l = r
        break
print(l + 1)
