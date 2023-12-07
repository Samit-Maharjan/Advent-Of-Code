data = open('input.txt', 'r').read().strip().split('\n')
values = {'J': 0}
for i in range(1, 10):
    values[str(i)] = i
for i, x in enumerate(['T', 'Q', 'K', 'A']):
    values[x] = i + 10
n, cards = len(data), [card.split() for card in data]
def check(card1, card2):
    cnt1, j = {0 : 0}, 0
    for x in card1:
        if x == 'J':    j += 1
        else:   cnt1[x] = cnt1.get(x, 0) + 1
    c1 = sorted(cnt1.values(), reverse = True)
    c1[0] += j
    cnt2, j = {0 : 0}, 0
    for x in card2:
        if x == 'J':    j += 1
        else: cnt2[x] = cnt2.get(x, 0) + 1
    c2 = sorted(cnt2.values(), reverse = True)
    c2[0] += j
    if c1 != c2:
        return c1 > c2
    for i, j in zip(card1, card2):
        if i == j:
            continue
        return values[i] > values[j]        

for i in range(n - 1):
    for j in range(n - i - 1):
        if check(cards[j][0], cards[j + 1][0]):
            cards[j], cards[j + 1] = cards[j + 1], cards[j]
print(sum(int(x[1]) * (i + 1) for i, x in enumerate(cards) ) )


