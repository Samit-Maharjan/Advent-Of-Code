import re, functools
rate = {}
open_to = {}
valves = []
data = open("input.txt").read().splitlines()
n = len(data)
pattern = r"Valve ([A-Z]+) has flow rate=(\d+); tunnel[s]* lead[s]* to valve[s]* (.*)"
for line in data:
    par, r, ch = re.findall(pattern, line)[0]
    valves.append(par)
    open_to[par] = list(map(lambda x: x.strip(), ch.split(',')))
    rate[par] = int(r)

TIME = 30

@functools.lru_cache(None)
def solve(time, src, vis):
    if time >= TIME:
        return 0
    p = 0
    for nei in open_to[src]:
        p = max(p, solve(time + 1, nei, vis) )
    if src not in vis and rate[src] > 0:
        vis = tuple([*vis, src])
        t = time + 1
        p = max(p, solve(t, src, vis) + rate[src] * (TIME - t) )
    return p

print(solve(0, "AA", () ) )


