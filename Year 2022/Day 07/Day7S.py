from collections import defaultdict
MAX, need = 7 * 10 ** 7, 3 * 10 ** 7
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
            st.append('.'.join(st + [cmd[2]]))
    else:
        if cmd[0] == 'dir':
            graph[st[-1]].append('.'.join(st + [cmd[1]]))
        else:
            mp[st[-1]] += int(cmd[0])

def dfs(node):
    for x in graph[node]:
        mp[node] += dfs(x)
    return mp[node]

dfs('/')
tot = mp['/']
res = min(x for x in mp.values() if MAX - tot + x >= need)
print(res)
    


