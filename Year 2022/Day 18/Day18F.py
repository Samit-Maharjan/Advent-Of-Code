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

res = 0
for point in points:
    sides = 6
    for nei in neighbors(*point):
        sides -= nei in points
    res += sides
print(res)
