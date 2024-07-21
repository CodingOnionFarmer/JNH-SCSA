import sys

input = sys.stdin.readline

n = int(input())
piles = [int(input()) for _ in range(n)]

if n == 1:
    print(0)
else:
    piles.sort()
    ans = piles[0] + piles[1]
    new_piles = [ans]
    p1 = 2
    p2 = 0
    while p1 < n:
        compared = 0
        if piles[p1] < new_piles[p2]:
            compared += piles[p1]
            p1 += 1
        else:
            compared += new_piles[p2]
            p2 += 1
        if p1 == n:
            compared += new_piles[p2]
            p2 += 1
        elif p2 == len(new_piles):
            compared += piles[p1]
            p1 += 1
        elif piles[p1] < new_piles[p2]:
            compared += piles[p1]
            p1 += 1
        else:
            compared += new_piles[p2]
            p2 += 1
        ans += compared
        new_piles.append(compared)
    for i in range(len(new_piles) - p2 - 1):
        compared = new_piles[p2 + 2 * i] + new_piles[p2 + 2 * i + 1]
        ans += compared
        new_piles.append(compared)
    print(ans)
