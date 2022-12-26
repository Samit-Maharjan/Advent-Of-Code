import heapq as hq
data = open('input.txt', 'r').read().split('\n')
pq = []
cur = 0
for x in data:
    if not len(x):
        hq.heappush(pq, cur)
        if len(pq) > 3:
            hq.heappop(pq)
        cur = 0
    else:
        cur += int(x)
res = sum(pq)
print(res)
