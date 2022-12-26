data = open("input.txt").read().splitlines()
res = 0
for i in range(0, len(data), 3):
    a, b, c = set(data[i]), set(data[i + 1]), set(data[i + 2])
    val = next(iter(a.intersection(b).intersection(c)))
    res += ord(val) - (ord('a') - 1 if val >= 'a' else ord('A') - 27)
print(res)


