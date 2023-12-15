data = open('input.txt', 'r').read().strip().split(',')
def solve(string):
    ans = 0
    for x in string:
        ans += ord(x)
        ans *= 17
        ans %= 256
    return ans
print(sum(solve(x) for x in data) )

