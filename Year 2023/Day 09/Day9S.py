data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for line in data:
    line = list(map(int, line.split() ) )
    st = [line[::-1]]
    while not all(x == 0 for x in line):
        new = []
        for i in range(1, len(line) ):
            new.append(line[i] - line[i - 1])
        line = new
        st.append(new[::-1])
    last = 0
    while st:
        st[-1].append(st[-1][-1] - last)
        last = st[-1][-1]
        st.pop()
    ans += last
print(ans)
