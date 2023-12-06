from collections import defaultdict
data = open('input.txt', 'r').read().strip().split('\n')
ans = 0
mp = defaultdict(int)
for line in data:
    card_no, cards = line.split(':')
    card_no = int(card_no.split()[-1])
    win, play = cards.split('|')
    win = win.strip().split()
    winning, cnt = set(win), 0
    for x in play.strip().split():
        cnt += x in winning
    for i in range(cnt):
        mp[card_no + i + 1] += mp[card_no] + 1
    ans += 1 + mp[card_no]
print(ans)

