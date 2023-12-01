data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for line in data:
    A = []
    for x in line:
        if x.isnumeric():
            A.append(int(x) )
    ans += A[0] * 10 + A[-1]
print(ans)
