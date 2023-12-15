data = open('input.txt', 'r').read().strip().split(',')
boxes = [[] for _ in range(256)]
def solve(string):
    ans = 0
    for x in string:
        ans += ord(x)
        ans *= 17
        ans %= 256
    return ans

def process(string):
    if '-' in string:
        string = string[:-1]
        cur = solve(string)
        for i, x in enumerate(boxes[cur]):
            if x[0] != string:
                continue
            boxes[cur].pop(i)
            break
    else:
        string, f = string.split('=')
        cur = solve(string)
        found = False
        for i, x in enumerate(boxes[cur]):
            if x[0] != string:
                continue
            boxes[cur][i] = [string, int(f)]
            found = True
            break
        if not found:
            boxes[cur].append([string, int(f)])

for x in data:  
    process(x)

ans = 0
for x in range(256):
    for i, box in enumerate(boxes[x]):
        ans += (x + 1) * (i + 1) * box[1]
print(ans)

    

