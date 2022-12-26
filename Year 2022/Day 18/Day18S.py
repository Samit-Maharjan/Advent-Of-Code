from collections import deque
data = open("input.txt").read().splitlines()
points = set()
for line in data:
    x, y, z = map(int, line.split(',') )
    points.add( (x, y, z) )

def neighbors(x, y, z):
    yield (x + 1, y, z)
    yield (x, y + 1, z)
    yield (x, y, z + 1)
    yield (x - 1, y, z)
    yield (x, y - 1, z)
    yield (x, y, z - 1)

x_range = range(min(x for x, _, _ in points), max(x for x, _, _ in points) + 1)
y_range = range(min(y for _, y, _ in points), max(y for _, y, _ in points) + 1)
z_range = range(min(z for _, _, z in points), max(z for _, _, z in points) + 1)


exterior = set()
def bfs(x, y, z):
    if (x, y, z) in points:
        return False
    q = deque([(x, y, z)])
    vis = set()
    while q:
        node = q.popleft()
        if node in points or node in vis:
            continue
        vis.add(node)
        for x, y, z in neighbors(*node):
            if x not in x_range or y not in y_range or z not in z_range or (x, y, z) in exterior:
                exterior.update(vis)
                return True
            q.append( (x, y, z) )        
    return False


res = 0
for point in points:
    for nei in neighbors(*point):
        if bfs(*nei):
            res += 1
print(res)


