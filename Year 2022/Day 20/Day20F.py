from collections import deque
data = open("input.txt").read().splitlines()
X = deque(list(enumerate([int(x) for x in data]) ) )
for i in range(len(X) ):
    while X[0][0] != i:
        X.append(X.popleft() ) 
    cur = X.popleft()
    moves = cur[1] % len(X)
    for _ in range(moves):
        X.append(X.popleft() )
    X.append(cur)
j = 0
for j in range(len(data) ):
    # can't move
    if X[j][1] == 0:
        break
print(X[(j + 1000) % len(X)][1] + X[(j + 2000) % len(X)][1] + X[(j + 3000) % len(X)][1])
