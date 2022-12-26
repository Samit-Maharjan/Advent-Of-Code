from collections import deque
import re
res = 1
data = open("input.txt").read().splitlines()[:3]
for i, line in enumerate(data, start = 1):
    pattern = r"(\d+)"
    values = list(map(int, re.findall(pattern, line)[1:] ) )
    orero, clayro, obsro, obsrc, georo, georob = values
    mx = 0
    print(values)
    # ore, clay, obsidian, geode, orer, clayr, obsr, geor
    q = deque([(0, 0, 0, 0, 1, 0, 0, 0)])
    for t in range(32):
        nq = set()
        while q:
            ore, clay, obs, geode, orer, clayr, obsr, geor =  q.popleft()
            nore = ore + orer
            nclay = clay + clayr
            nobs = obs + obsr
            ngeode = geode + geor
            mx = max(mx, ngeode + geor * (32 - t - 1) )
            # make nothing
            nq.add( (nore, nclay, nobs, ngeode, orer, clayr, obsr, geor) )
            if ore >= orero:
                nq.add( (nore - orero, nclay, nobs, ngeode, orer + 1, clayr, obsr, geor) )
            if ore >= clayro:
                nq.add( (nore - clayro, nclay, nobs, ngeode, orer, clayr + 1, obsr, geor) )
            if ore >= obsro and clay >= obsrc:
                nq.add( (nore - obsro, nclay - obsrc, nobs, ngeode, orer, clayr, obsr + 1, geor) )
            if ore >= georo and obs >= georob:
                nq.add( (nore - georo, nclay, nobs - georob, ngeode, orer, clayr, obsr, geor + 1) )
        
        for state in nq:
            ore, clay, obs, geode, orer, clayr, obsr, geor =  state
            if geode + 2 *  (32 - t - 1) * geor >= mx:
                q.append(state)
    res *= mx
print(res)



