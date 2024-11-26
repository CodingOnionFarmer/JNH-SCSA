n, L, R = map(int, input().split())
dp = [{}, {(1, 1): 1}]
for i in range(2, n + 1):
    ith = {}
    for l, r in dp[i - 1]:
        c = dp[i - 1][l, r]
        if (l, r) in ith:
            ith[l, r] += c * (i - 2)
        else:
            ith[l, r] = c * (i - 2)
        ith[l, r] %= 1000000007
        if (l + 1, r) in ith:
            ith[l + 1, r] += c
        else:
            ith[l + 1, r] = c
        ith[l + 1, r] %= 1000000007
        if (l, r + 1) in ith:
            ith[l, r + 1] += c
        else:
            ith[l, r + 1] = c
        ith[l, r + 1] %= 1000000007
    dp.append(ith)
if (L, R) in dp[n]:
    print(dp[n][L, R])
else:
    print(0)
