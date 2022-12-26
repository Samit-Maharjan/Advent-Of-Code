data = open("input.txt").read().splitlines()
res = 0
st = [1]
for x in data:
    k = x.split()
    if len(k) > 1:
        st.append(0)
        st.append(int(k[1]) )
    else:
        st.append(0)
for x in [20, 60, 100, 140, 180, 220]:
    res += sum(st[:x]) * x
print(res)
