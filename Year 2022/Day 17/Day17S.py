data = open("input.txt").read()[:-1]
moves = [(0, 1) if x == '>' else (0, -1) for x in data]

rocks = [[(0, 2), (0, 3), (0, 4), (0, 5)],
        [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
        [(0, 2), (0, 3), (0, 4), (1, 4), (2, 4)],
        [(0, 2), (1, 2), (2, 2), (3, 2)],
        [(0, 2), (0, 3), (1, 2), (1, 3)]]

tower = {(0, x) for x in range(7)}
TIMES = 1_000_000_000_000
dp = {}
move_idx = 0
max_h = 0

for index in range(TIMES):
    state = index % len(rocks), move_idx
    if state in dp:
        s, h = dp[state]
        left = TIMES - index
        delta = max_h - h
        d, m = divmod(left, index - s)
        if not m:
            print(max_h + d * delta)
            break
    else:
        dp[state] = index, max_h
    offset = max(x for x, _ in tower) + 4
    rock = [(x + offset, y) for x, y in rocks[index % len(rocks)]]
    rest = False
    while True:
        dx, dy = moves[move_idx]
        move_idx = (move_idx + 1) % len(moves)
        new_rock = [(x + dx, y + dy) for x, y in rock]
        if any(y < 0 or y >= 7 for _, y in new_rock):
            new_rock = rock
        elif any(pos in tower for pos in new_rock):
            new_rock = rock
        rock = new_rock
        dx, dy = -1, 0
        new_rock = [(x + dx, y + dy) for x, y in new_rock]
        if any(pos in tower for pos in new_rock):
            break
        rock = new_rock
    tower.update(rock)
    max_h = max(x for x, _ in tower)

