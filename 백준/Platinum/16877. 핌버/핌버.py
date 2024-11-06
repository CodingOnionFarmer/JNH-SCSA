fib = [1, 2]
while fib[-1] < 3000000:
    fib.append(fib[-1] + fib[-2])
bfi = [0] * 3000001
i = 0
for num in range(1, 3000001):
    if fib[i + 1] <= num:
        i += 1
    bfi[num] = i

grundy = [-1] * 3000001
grundy[0] = 0


def find_g(number):
    if grundy[number] >= 0:
        return grundy[number]
    move = set()
    for i in range(bfi[number], -1, -1):
        move.add(find_g(number - fib[i]))
    g = 0
    while g in move:
        g += 1
    grundy[number] = g
    return g


n = int(input())
stone_piles = list(map(int, input().split()))
g_num = 0
for size in stone_piles:
    g_num ^= find_g(size)
if g_num:
    print('koosaga')
else:
    print('cubelover')
