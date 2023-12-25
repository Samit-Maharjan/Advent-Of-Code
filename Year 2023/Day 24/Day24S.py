import sympy
data = open('input.txt', 'r').read().strip().split('\n')

hail, vel = [], []
for line in data:
    h, v = line.split('@')
    f = lambda x: list(map(int, x.split(', ')))
    hail.append(f(h))
    vel.append(f(v))

x = sympy.var('x')
y = sympy.var('y')
z = sympy.var('z')

vx = sympy.var('vx')
vy = sympy.var('vy')
vz = sympy.var('vz')

t1 = sympy.var('t1')
t2 = sympy.var('t2')
t3 = sympy.var('t3')

(ax, ay, az), (vax, vay, vaz) = hail[0], vel[0]
(bx, by, bz), (vbx, vby, vbz) = hail[1], vel[1]
(cx, cy, cz), (vcx, vcy, vcz) = hail[2], vel[2]


equations = []

equations.append(sympy.Eq(x + t1 * vx, ax + t1 * vax))
equations.append(sympy.Eq(y + t1 * vy, ay + t1 * vay))
equations.append(sympy.Eq(z + t1 * vz, az + t1 * vaz))

equations.append(sympy.Eq(x + t2 * vx, bx + t2 * vbx))
equations.append(sympy.Eq(y + t2 * vy, by + t2 * vby))
equations.append(sympy.Eq(z + t2 * vz, bz + t2 * vbz))

equations.append(sympy.Eq(x + t3 * vx, cx + t3 * vcx))
equations.append(sympy.Eq(y + t3 * vy, cy + t3 * vcy))
equations.append(sympy.Eq(z + t3 * vz, cz + t3 * vcz))

ans = sympy.solve(equations)[0]
print(sum(ans[i] for i in [x, y, z]))
