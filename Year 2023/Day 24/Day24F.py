data = open('input.txt', 'r').read().strip().split('\n')
S, E = 200000000000000, 400000000000000

hail, vel = [], []
for line in data:
    h, v = line.split('@')
    f = lambda x: list(map(int, x.split(', ')))
    hail.append(f(h))
    vel.append(f(v))

def intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return None, None

    d = (det(*line1), det(*line2))
    return det(d, xdiff) / div, det(d, ydiff) / div

ans = 0
for i in range(len(hail)):
    for j in range(i + 1, len(hail)):
        (fx, fy, _), (sx, sy, _) = hail[i], hail[j]
        (vfx, vfy, _), (vsx, vsy, _) = vel[i], vel[j]
        nfx, nfy, nsx, nsy = fx + vfx, fy + vfy, sx + vsx, sy + vsy
        x, y  = intersection(((fx, fy), (nfx, nfy)), ((sx, sy), (nsx, nsy)))
        if not x or not y:
            continue
        dfx, dfy, dsx, dsy = x - fx, y - fy, x - sx, y - sy
        if dfx * vfx < 0 or dfy * vfy < 0 or dsx * vsx < 0 or dsy * vsy < 0:
            continue
        ans +=  S <= x <= E and S <= y <= E
print(ans)

