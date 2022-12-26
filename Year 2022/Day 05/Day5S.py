crate, moves = open("input.txt").read().split("\n\n")
crates = list(zip(*(x[1::4] for x in crate.splitlines()[:-1][::-1] ) ) )
stack  = [[x for x in cur if x != ' '] for cur in crates]
moves  = [[int(x) for x in cur.split() if x.isdigit()] for cur in moves.splitlines()]
for n, l, r in moves:
    for x in stack[l -  1][-n:]:
        stack[r - 1].append(x)
    stack[l - 1] = stack[l - 1][:-n]
print(''.join(x[-1] for x in stack) )
