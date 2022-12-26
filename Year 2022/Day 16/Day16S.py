import re, collections
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

masks = {x : 1 << i  for i, x in enumerate(rate) if rate[x] > 0}
dist = {x : {y : 1 if y in open_to[x] else float('inf') for y in valves} for x in valves}

# Floyd-Warshall for Pairwise distance
for k in dist:
    for i in dist:
        for j in dist:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

TIME = 26
# bitmask_state : pressure
dp = collections.defaultdict(int)

def solve(node, time, mask, p):
    dp[mask] = max(dp[mask], p)
    for valve in valves:
        t = time + dist[node][valve] + 1
        # already checked or time overflow or no pressure
        if not rate[valve] or t >= TIME or (masks[valve] & mask):
            continue
        solve(valve, t , mask | masks[valve], p + rate[valve] * (TIME - t) )

solve('AA', 0, 0, 0)
print(max(v1 + v2 for human, v1 in dp.items() for elephant, v2 in dp.items() if not human & elephant) )


    

