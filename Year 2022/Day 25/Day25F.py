data = open("input.txt").read().splitlines()
values = {'1': 1, '2': 2, '0': 0, '-': -1, '=': -2}
reverse = {3: '=', 4: '-'}

res = 0
for snafu in data:
    for i, x in enumerate(snafu[::-1]):
        res += values[x] * int(5 ** i)
ans = str()
while res > 0:
    cur = int(res % 5)
    if cur > 2:
        ans += reverse.get(cur, '0')
    else:
        ans += str(cur)
    res = res / 5 + (cur > 2)
print(ans[::-1])


