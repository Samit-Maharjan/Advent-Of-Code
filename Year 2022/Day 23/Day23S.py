from collections import defaultdict
grid = open("input.txt").read().splitlines()
elves = set( (i, j) for i, x in enumerate(grid) for j in range(len(x) ) if grid[i][j] == '#')
dir = [[(-1, 0), (-1, -1), (-1, 1)],
        [(1, 0), (1, -1), (1, 1)],
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)], ]

dirs = sum(dir, start = [])
doff = cnt = 0
someone_moved = True

while someone_moved:
    cnt += 1
    ndir = dir[doff:] + dir[:doff]
    stay_put = []
    propose = defaultdict(list)
    for elf in elves:
        x, y = elf
        if all( (x + dx, y + dy) not in elves for dx, dy in dirs):
            stay_put.append(elf)
            continue
        moved = False
        for move in ndir:
            if all ( (x + dx, y + dy) not in elves for dx, dy in move):
                dx, dy = move[0]     
                propose[x + dx, y + dy].append(elf)
                moved = True
                break
        if not moved:
            stay_put.append(elf)
    new_elves = set()
    new_elves.update(stay_put)
    for new, prev in propose.items():
        if len(prev) > 1:
            new_elves.update(prev)
        else:
            new_elves.add(new)
    doff = (doff + 1) % 4
    assert len(elves) == len(new_elves)
    someone_moved = len(elves - new_elves)
    elves = new_elves

print(cnt)

