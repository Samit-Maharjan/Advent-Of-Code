data = open('input.txt', 'r').read().strip().split('\n')
bricks, n = [], len(data)
for line in data:
    f, s = line.split('~')
    x, y, z = map(int, f.split(','))
    nx, ny, nz = map(int, s.split(','))
    brick = set()
    for xx in range(x, nx + 1):
        brick.add((xx, y, z))
    for yy in range(y, ny + 1):
        brick.add((x, yy, z))
    for zz in range(z, nz + 1):
        brick.add((x, y, zz))
    bricks.append(sorted(tuple(brick), key = lambda x: x[2]))
bricks.sort(lambda x: x[-1][2])

def simulate(bricks):
    final_state = []
    world, dropped = set(), set()
    for i, brick in enumerate(bricks):
        while True:
            z = brick[0][2]
            if any((xx, yy, zz - 1) in world for xx, yy, zz in brick) or z == 1:
                final_state.append(brick)
                for cell in brick:
                    world.add(cell)
                break
            else:
                brick = tuple((x, y, z - 1) for x, y, z in brick)
                dropped.add(i)
    return final_state, len(dropped)

bricks, _ = simulate(bricks)
ans = 0
for i in range(n):
    new_bricks = bricks[:i] + bricks[i + 1:]
    _, cnt = simulate(new_bricks)
    ans += cnt
print(ans)
