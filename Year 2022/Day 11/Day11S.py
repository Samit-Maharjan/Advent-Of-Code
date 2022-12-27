import re
MOD = 1
class monkey:
    def __init__(self, s):
        s = s.splitlines()
        self.values = list(map(int, re.findall(r'\d+', s[1]) ) )
        op1, op, op2 = s[2].split('=')[-1].split()
        self.operands = [op1, op2]
        self.operation = op
        self.test = int(re.findall(r'\d+', s[3])[0])
        self.true_throw = int(re.findall(r'\d+', s[4])[0])
        self.false_throw = int(re.findall(r'\d+', s[5])[0])
        self.inspected = 0

    def operate(self, index):
        op1, op2 = self.operands
        a = (str(self.values[index]) if op1 == 'old' else op1)
        b = (str(self.values[index]) if op2 == 'old' else op2)
        value = (eval(a + self.operation + b) % MOD)
        if not value % self.test:
            return value, self.true_throw
        else:
            return value, self.false_throw

data = open("input.txt").read().split('\n\n')
monkeys = [monkey(x) for x in data]
for x in monkeys:   MOD *= x.test

for _ in range(10000):
    for x in monkeys:
        x.inspected += len(x.values)
        for i, val in enumerate(x.values):
            value, to = x.operate(i)
            monkeys[to].values.append(value)
        x.values.clear()

res = [x.inspected for x in monkeys]
res.sort()
print(res[-1] * res[-2])


    
