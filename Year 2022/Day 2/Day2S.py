data = open("input.txt").read().splitlines()
res = 0
points = {'X': 1, 'Y': 2, 'Z':3}
lose = {'A':'Z', 'B': 'X', 'C': 'Y'}
win = {'A':'Y', 'B':'Z', 'C':'X'}
draw = {'A':'X', 'B': 'Y', 'C':'Z'}

for x in data:
    elf, us = x.split() 
    if us == 'X':
        res += points[lose[elf]] + 0
    elif us == 'Y':
        res += points[draw[elf]] + 3
    else:
        res += points[win[elf]] + 6

print(res)
