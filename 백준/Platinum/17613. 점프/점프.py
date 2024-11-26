def shrink(x, y):
    ans = 0
    lx = len(bin(x + 1))
    ly = len(bin(y + 1))
    while lx == ly and x:
        x -= 2 ** (lx - 3) - 1
        y -= 2 ** (lx - 3) - 1
        ans += lx - 3
        lx = len(bin(x + 1))
        ly = len(bin(y + 1))
    if y < 3:
        return ans + y
    cut = 2 ** (ly - 3) - 1
    lc = cut - ly + 5
    if lc >= x:
        return ans + max((ly - 4) * (ly - 3) // 2 + 1, shrink(cut, y))
    return ans + max(shrink(x, cut - 1), shrink(cut, y))


for t in range(int(input())):
    x, y = map(int, input().split())
    print(shrink(x, y))
