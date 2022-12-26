from collections import defaultdict
MAX = 10 ** 5
data = open("input.txt").read().splitlines()
graph = defaultdict(list)
mp = defaultdict(int)
st = []
for cmd in data:
    cmd = cmd.split()
    if cmd[0] == '$':
        if cmd[1] == 'ls':
            continue
        elif cmd[2] == '..':
            st.pop(-1)
        else:
            st.append('/'.join(st + [cmd[2]]))
    else:
        if cmd[0] == 'dir':
            graph[st[-1]].append('/'.join(st + [cmd[1]]))
        else:
            mp[st[-1]] += int(cmd[0])

def dfs(node):
    for x in graph[node]:
        mp[node] += dfs(x)
    return mp[node]

dfs('/')
res = sum(x for x in mp.values() if x <= MAX)
print(res)
    


