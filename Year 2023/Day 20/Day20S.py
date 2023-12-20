from collections import deque, defaultdict
data = open('input.txt', 'r').read().strip().split('\n')

config, module = {}, {}
for line in data:
    fro, to = [x.strip() for x in line.split('->')]
    if fro == 'broadcaster':
        fro = '%' + fro
    typ, fro = fro[0], fro[1:]
    module[fro], config[fro] = typ, to.split(', ')
pulses = {'high': 0, 'low': 0}

last_conj = {}
state, last = defaultdict(int), defaultdict(dict)
for k, v in config.items():
    for x in v:
        if x in module and module[x] == '&':
            last[x][k] = 'low'
        if x == 'lb':
            last_conj[k] = 0
cnt = 1
while not all(x for x in last_conj.values() ):
    q = deque([ ['broadcaster', 'low'] ])
    while q:
        pulse, node = q[0][-1], q.popleft()
        pulses[pulse] += len(node) - 1;
        for fro in node[:-1]:
            cur, npulse = [], pulse
            if module[fro] == '%':
                npulse = 'high' if state[fro] else 'low'
            else:
                npulse = 'low' if all(x == 'high' for x in last[fro].values() ) else 'high'
            for to in config[fro]:
                if to not in module:
                    pulses[npulse] += 1
                    continue
                if module[to] == '%':
                    if npulse == 'high':
                        pulses['high'] += 1
                        continue
                    state[to] = state[to] ^ 1
                    if to in last_conj and state[to]:
                        last_conj[to] = cnt
                else:
                    last[to][fro] = npulse
                    if to in last_conj and npulse == 'low':
                        last_conj[to] = cnt
                cur.append(to)
            if not cur:
                continue
            q.append(cur + [npulse])
    cnt += 1

ans = 1
from math import gcd
for x in last_conj.values():
    ans = ans * x // gcd(ans, x)
print(ans)
