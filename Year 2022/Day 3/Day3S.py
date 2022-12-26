data = open("input.txt").read().split('\n')
res = 0
for i in range(0, len(data), 3):
    mp = set(list(data[i]) ) 
    mp = set(x if x in mp else '' for x in data[i + 1])
    mp = set(x if x in mp else '' for x in data[i + 2])
    mp.remove('')
    mp = list(mp)
    if mp[0] < 'a':
        res += 27 + ord(mp[0]) - ord('A')
    else:
        res += 1 + ord(mp[0]) - ord('a')
print(res)






