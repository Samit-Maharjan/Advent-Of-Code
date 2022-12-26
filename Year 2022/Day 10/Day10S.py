data = open("input.txt").read().splitlines()
st = [1]
sprite = 0
res = [str() for _ in range(6)]
for x in data:
    k = x.split()
    if len(k) > 1:
        st.append(0)
        st.append(int(k[1]) )
    else:
        st.append(0)

for i in range(0, 240, 40):
    for j in range(40):
        sprite = sum(st[:i + j + 1])
        res[i // 40] += ['.', '#'][j in range(sprite - 1, sprite + 2)]

for x in res:
    print(x)
    
