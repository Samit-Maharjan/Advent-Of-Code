crate, moves = open("input5.txt").read().split('\n\n')
crates = list(zip(*(x[1::4] for x in crate.splitlines()[:-1][::-1]) ) )
stack = [ [x for x in cur if x != ' '] for cur in crates]
moves = [ [int(x) - 1 for x in cur.split() if x.isdigit() ] for cur in moves.splitlines()]
for n, l, r in moves:
    for i in range(n + 1):
        stack[r].append(stack[l].pop())
print(''.join(x[-1] for x in stack) )




