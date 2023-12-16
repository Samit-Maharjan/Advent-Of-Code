data = [list(x) for x in open('input.txt', 'r').read().strip().split('\n')]
m, n = len(data), len(data[0])
move = {'l': (0, -1), 'r': (0, 1), 'u': (-1, 0), 'd': (1, 0)}
front = {'r': 'u', 'l': 'd', 'u': 'r', 'd': 'l'}
back  = {'r': 'd', 'l': 'u', 'u': 'l', 'd': 'r'}
def solve(x, y, d):
    q = [(x - move[d][0], y - move[d][1], d)]
    vis, mat = set(), [[0] * n for _ in range(m)]
    while q:
        nq = []
        for x, y, d in q:
            if 0 <= x < m and 0 <= y < n:
                mat[x][y] = 1
            nx, ny = x + move[d][0], y + move[d][1]
            if 0 <= nx < m and 0 <= ny < n:
                tiles = []
                if data[nx][ny] == '|':
                    if d in 'ud':
                        tiles.append( (nx, ny, d) )
                    else:
                        tiles.append( (nx, ny, 'u') )
                        tiles.append( (nx, ny, 'd') )
                elif data[nx][ny] == '-':
                    if d in 'lr':
                        tiles.append( (nx, ny, d) )
                    else:
                        tiles.append( (nx, ny, 'l') )
                        tiles.append( (nx, ny, 'r') )
                elif data[nx][ny] == '/':
                    tiles.append( (nx, ny, front[d] ) )
                elif data[nx][ny] == '\\':
                    tiles.append( (nx, ny, back[d] ) )
                else:
                    tiles.append( (nx, ny, d) )
                for tile in tiles:
                    if tile in vis:
                        continue
                    nq.append(tile)
                    vis.add(tile)
        q = nq
    return sum(sum(x) for x in mat)
ans = []
for i in range(m):
    ans += [solve(i, 0, 'r'), solve(i, n - 1, 'l')]
for i in range(n):
    ans += [solve(0, i, 'd'), solve(m - 1, 0, 'u')]
print(max(ans) )


