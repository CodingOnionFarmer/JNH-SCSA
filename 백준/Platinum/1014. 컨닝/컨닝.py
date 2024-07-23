for tc in range(int(input())):
    n, m = map(int, input().split())
    table = [input() for _ in range(n)]
    can_sit = [[j for j in range(1 << n) if not i & j] for i in range(1 << n)]
    dp = [[-1] * (1 << n) for _ in range(m)]  # dp[c][100101]은 c번째 열에 100101로 앉았을때 최대로 앉은 수 (왼쪽 열부터 앉음)
    broken = [0] * m
    for c in range(m):
        for r in range(n):
            broken[c] <<= 1
            if table[r][c] == 'x':
                broken[c] += 1
    column = -1
    right_break = [0] * (1 << n)
    sit_cnt = [0] * (1 << n)
    for sit in range(1 << n):
        one = False
        right = 0
        for r in range(n - 1, 0, -1):
            if sit & (1 << r):
                right += 1
                sit_cnt[sit] += 1
                one = True
            elif one:
                right += 1
                one = False
            elif sit & (1 << (r - 1)):
                right += 1
            right <<= 1
        if sit & 1:
            right += 1
            sit_cnt[sit] += 1
        elif one:
            right += 1
        right_break[sit] = right
    for sit in can_sit[broken[0]]:
        dp[0][sit] = sit_cnt[sit]
    for c in range(1, m):
        for left in range(1 << n):
            if dp[c - 1][left] > -1:
                for sit in can_sit[right_break[left] | broken[c]]:
                    if dp[c][sit] < dp[c - 1][left] + sit_cnt[sit]:
                        dp[c][sit] = dp[c - 1][left] + sit_cnt[sit]
    print(max(dp[m - 1]))
