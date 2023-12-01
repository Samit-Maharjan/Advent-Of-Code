data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
digits = {'one': 1, 'two': 2, 'three': 3,
          'four': 4, 'five': 5, 'six': 6,
          'seven': 7, 'eight': 8, 'nine': 9}
for line in data:
    A = []
    for i, x in enumerate(line):
        if x.isnumeric():
            A.append(int(x) )
        for k, v in digits.items():
            if line[i:].startswith(k):
                A.append(v)
                break
    ans += A[0] * 10 + A[-1]
print(ans)

