import re

wf, parts = open('input.txt', 'r').read().strip().split('\n\n')

WF = {}
default = {}
for row in wf.split('\n'):
    name, checks = row[:-1].split('{')
    to_send = {}
    for check in checks.split(','):
        if len(check.split(':') ) == 1:
            default[name] = check
        else:
            c, to = check.split(':')
            to_send[c] = to
    WF[name] = to_send
    
ans = 0
for part in parts.split('\n'):
    val = {u:v for u, v in zip('xmas', re.findall(r'\d+', part) )}
    start = 'in'
    while start not in 'AR':
        nstart = start
        for k, to in WF[start].items():
            for v in 'xmas':
                if v not in k:
                    continue
                k = k.replace(v, val[v])
            if not any(x.isalpha() for x in k) and eval(k):
                nstart = to
                break
        if nstart == start:
            nstart = default[start]
        start = nstart
    if start == 'A':
        ans += sum(int(x) for x in val.values() )
print(ans)
