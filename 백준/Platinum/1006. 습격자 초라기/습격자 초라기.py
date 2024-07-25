t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    INF = 20001
    inner = list(map(int, input().split()))
    outer = list(map(int, input().split()))
    if n == 1:
        if inner[0] + outer[0] <= w:
            print(1)
        else:
            print(2)
        continue
    # dp[ㄱㄴ][ㄷㄹ]는 (ㄱㄴ와 ㄷㄹ는 이진수)
    # ㄱ:내부 서클에서 마지막 요소 침범했는지
    # ㄴ:외부 서클에서 마지막 요소 침범했는지
    # ㄷ:내부 서클에서 다음 요소 침범했는지
    # ㄹ:외부 서클에서 다음 요소 침범했는지
    dp = [[INF] * 4 for _ in range(4)]
    dp[0][0] = 2
    if inner[0] + outer[0] <= w:
        dp[0][0] = 1
    last_inner = inner[0] + inner[-1] <= w
    last_outer = outer[0] + outer[-1] <= w
    if last_inner:
        if last_outer:
            dp[3][0] = 2
            if inner[0] + inner[1] <= w:
                dp[1][2] = 2
                if outer[0] + outer[1] <= w:
                    dp[0][3] = 2
            if outer[0] + outer[1] <= w:
                dp[2][1] = 2
        else:
            dp[2][0] = 2
            if inner[0] + inner[1] <= w:
                dp[0][2] = 2
                if outer[0] + outer[1] <= w:
                    dp[0][3] = 2
            if outer[0] + outer[1] <= w:
                dp[2][1] = 2
    else:
        if last_outer:
            dp[1][0] = 2
            if inner[0] + inner[1] <= w:
                dp[1][2] = 2
                if outer[0] + outer[1] <= w:
                    dp[0][3] = 2
            if outer[0] + outer[1] <= w:
                dp[0][1] = 2
        else:
            if inner[0] + inner[1] <= w:
                dp[0][2] = 2
                if outer[0] + outer[1] <= w:
                    dp[0][3] = 2
            if outer[0] + outer[1] <= w:
                dp[0][1] = 2
    for i in range(1, n - 1):
        if inner[i] + outer[i] <= w:
            if inner[i] + inner[i + 1] <= w:
                if outer[i] + outer[i + 1] <= w:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 1, oo), min(xx + 2, ox + 1), min(xx + 2, xo + 1), xx + 2]
                else:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 1, oo), INF, min(xx + 2, xo + 1), INF]
            else:
                if outer[i] + outer[i + 1] <= w:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 1, oo), min(xx + 2, ox + 1), INF, INF]
                else:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 1, oo), INF, INF, INF]
        else:
            if inner[i] + inner[i + 1] <= w:
                if outer[i] + outer[i + 1] <= w:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 2, xo + 1, ox + 1, oo), min(xx + 2, ox + 1), min(xx + 2, xo + 1), xx + 2]
                else:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 2, xo + 1, ox + 1, oo), INF, min(xx + 2, xo + 1), INF]
            else:
                if outer[i] + outer[i + 1] <= w:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 2, xo + 1, ox + 1, oo), min(xx + 2, ox + 1), INF, INF]
                else:
                    for last in range(4):
                        xx, xo, ox, oo = dp[last]
                        dp[last] = [min(xx + 2, xo + 1, ox + 1, oo), INF, INF, INF]

    dp[0][0] += 1
    dp[0][1] += 1
    dp[0][2] += 1
    dp[1][0] += 1
    dp[2][0] += 1
    if inner[n - 1] + outer[n - 1] > w:
        dp[0][0] += 1
    print(min(min(dp[i][j] for j in range(4) if not i & j) for i in range(4)))
