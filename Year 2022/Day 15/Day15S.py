import re, time
start = time.time()
data = open("input.txt").read().splitlines()
sensors = {}

for line in data:
    coords = re.findall(r'[-]?\d+', line)
    sy, sx, by, bx = [int(x) for x in coords]
    sensors[sx, sy] = (bx, by)

n = 4000000
res = 0
for row in range(n + 1):
    vis = []
    for node, goal in sensors.items():
        x, y, nx, ny = *node, *goal
        dist = abs(nx - x) + abs(ny - y)
        if x - dist <= row <= x + dist:
            dy = dist - abs(row - x)
            gap = [max(0, y - dy), min(n, y + dy)]
            vis.append(gap)
    vis.sort()
    st = []
    st.append(vis[0])
    for gaps in vis[1:]:
        if st[-1][0] <= gaps[0] <= st[-1][-1]:
            st[-1][-1] = max(st[-1][-1], gaps[-1])
        else:
            st.append(gaps)
    if len(st) > 1:
        index = st[0][-1] + 1
        print(index * n + row)
        break
print("Time taken:", time.time() - start, "seconds")
