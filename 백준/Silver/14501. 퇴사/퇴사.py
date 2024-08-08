n = int(input())
sangdam = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
for date in range(sangdam[0][0], n + 1):
    dp[date] = sangdam[0][1]
for date in range(1, n):
    ended = date + sangdam[date][0]
    for later_date in range(ended, n + 1):
        dp[later_date] = max(dp[later_date], dp[date] + sangdam[date][1])
print(dp[n])
