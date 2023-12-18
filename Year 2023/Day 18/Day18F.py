data = open('input.txt', 'r').read().strip().split('\n')
move = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}
x, y, borders = 0, 0, []
for row in data:
    d, m, _ = row.split()
    dx, dy = move[d]
    for _ in range(int(m) ):
        borders.append( (x, y) )
        x, y = x + dx, y + dy

# Shoelace formula
area = 0
for i in range(len(borders) - 1):
    x1, y1 = borders[i]
    x2, y2 = borders[i + 1]
    area += x1 * y2 - x2 * y1
area = abs(area) // 2

# Pick's theorem
perimeter = len(borders)
interior_area = area - perimeter // 2 + 1
print(interior_area + perimeter)
