from collections import deque
import re
res = 0
data = open("input.txt").read().splitlines()
for i, line in enumerate(data, start = 1):
    pattern = r"(\d+)"
    values = list(map(int, re.findall(pattern, line)[1:] ) )
    orero, clayro, obsro, obsrc, georo, georob = values
    max_geode  = 0
    # ore, clay, obsidian, geode, orer, clayr, obsr, geor
    q = deque([(0, 0, 0, 0, 1, 0, 0, 0)])
    for t in range(24):
        nq = set()
        while q:
            ore, clay, obs, geode, orer, clayr, obsr, geor =  q.popleft()
            nore = ore + orer
            nclay = clay + clayr
            nobs = obs + obsr
            ngeode = geode + geor
            max_geode = max(max_geode, ngeode)
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
            if geode + (23 - t) >= max_geode:
                q.append(state)
    res += i * max_geode
print(res)



