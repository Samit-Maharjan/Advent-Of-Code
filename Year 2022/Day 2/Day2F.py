data = open("input.txt").read().splitlines()
res = 0
points = {'X': 1, 'Y': 2, 'Z':3}
win = {'A' : 'Y', 'B': 'Z', 'C': 'X'}
equal = {'A':'X', 'B': 'Y', 'C':'Z'}
for x in data:
    elf, us = x.split()
    if win[elf] == us:
        res += points[us] + 6
    elif equal[elf] == us:
        res += points[us] + 3
    else:
        res += points[us] + 0
print(res)
