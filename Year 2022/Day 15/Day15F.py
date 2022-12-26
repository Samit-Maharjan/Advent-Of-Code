import re, time
start =  time.time()
data = open("input.txt").read().splitlines()
sensors = {}
vis = set()

for line in data:
    coords = re.findall(r'[-]?\d+', line)
    sy, sx, by, bx = [int(x) for x in coords]
    sensors[sx, sy] = (bx, by)

goal_row = 2000000 
for node, goal in sensors.items():
    x, y, nx, ny = *node, *goal
    dist = abs(nx - x) + abs(ny - y)
    if x - dist <= goal_row <= x + dist:
        dy = dist - abs(goal_row - x)
        for col in range(y - dy, y + dy + 1):
            vis.add(col)

for bx, by in sensors.values():
    if bx == goal_row and by in vis:
        vis.remove(by)

print(len(vis) )
print("Time taken:", time.time() - start, "seconds")
    
