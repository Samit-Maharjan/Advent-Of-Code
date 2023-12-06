time, distance = open('input.txt', 'r').read().strip().split('\n')
tt = list(map(int, time.split(':')[-1].split() ) )
dd = list(map(int, distance.split(':')[-1].split() ) )
print(eval('*'.join(str(sum(d < i * (t - i) for i in range(1, t))) for t, d in zip(tt, dd))))
