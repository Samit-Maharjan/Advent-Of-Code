data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
for line in data:
    _, cards = line.split(':')
    win, play = cards.split('|')
    win = win.strip().split()
    winning, cnt = set(win), 0
    for x in play.strip().split():
        cnt += x in winning
    if cnt:
        ans += 1 << (cnt - 1)
print(ans)

