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

ranges = {}
for x in 'xmas':
    ranges[x] = (1, 4000)

def get(ranges):
    ans = 1
    for u, v in ranges.values():
        ans *= (v - u + 1)
    return ans

def solve(ranges, wf):
    ans = 0
    for cond, dest in WF[wf].items():
        letter, value = cond[0], int(re.findall(r'\d+', cond)[0])
        if '<' in cond:
            if ranges[letter][0] < value:
                nranges = ranges.copy()
                nranges[letter] = (ranges[letter][0], min(value - 1, ranges[letter][1]) )
                if dest == 'A':
                    ans += get(nranges)
                elif dest != 'R':
                    ans += solve(nranges, dest)
            ranges[letter] = (value, ranges[letter][1])
        else:
            if ranges[letter][1] > value:
                nranges = ranges.copy()
                nranges[letter] = (max(value + 1, ranges[letter][0]), ranges[letter][1])
                if dest == 'A':
                    ans += get(nranges)
                elif dest != 'R':
                    ans +=  solve(nranges, dest)
            ranges[letter] = (ranges[letter][0], value)
    if default[wf] == 'A':
        ans += get(ranges)
    elif default[wf] != 'R':
        ans += solve(ranges, default[wf])
    return ans

print(solve(ranges, 'in') )
