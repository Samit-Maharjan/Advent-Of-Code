time, distance = open('input.txt', 'r').read().strip().split('\n')
time = int(''.join(time.split(':')[-1].split() ) )
distance = int(''.join(distance.split(':')[-1].split() ) )
l, r = 0, time
while l < r:
    mid = (l + r) >> 1
    if mid * (time - mid) > distance:
        r = mid
    else:
        l = mid + 1
ll, rr = time // 2, time
while ll < rr:
    mid = (ll + rr + 1) >> 1
    if mid * (time - mid) > distance:
        ll = mid
    else:
        rr = mid - 1
print(ll - l + 1)
