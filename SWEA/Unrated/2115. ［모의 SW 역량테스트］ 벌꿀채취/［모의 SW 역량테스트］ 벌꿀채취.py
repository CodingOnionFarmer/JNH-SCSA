def dfs(depth, left, money):
    if depth == m:
        global most
        if money > most:
            most = money
        return
    honey = honeycomb[i][j + depth]
    if left >= honey:
        dfs(depth + 1, left - honey, money + honey * honey)
    dfs(depth + 1, left, money)


T = int(input())
for tc in range(1, T + 1):
    n, m, c = map(int, input().split())
    h = n + 1 - m
    honeycomb = [list(map(int, input().split())) for _ in range(n)]
    profit = [[0] * h for _ in range(n)]
    for i in range(n):
        for j in range(n + 1 - m):
            most = 0
            dfs(0, c, 0)
            profit[i][j] = most
    maximal_profit = 0
    for first in range(n * h - 1):
        i1, j1 = first // h, first % h
        first_profit = profit[i1][j1]
        for second in range(first + 1, n * h):
            i2, j2 = second // h, second % h
            if i1 == i2 and i2 - i1 < m:
                continue
            if first_profit + profit[i2][j2] > maximal_profit:
                maximal_profit = first_profit + profit[i2][j2]
    print(f'#{tc} {maximal_profit}')
