# Dynamic Programming

n = int(input())
dp = [1000000] * (n + 1)
dp[1] = 0
for i in range(2, n + 1):
    min_try = dp[i - 1] + 1
    if not i % 2:
        min_try = min(min_try, dp[i // 2] + 1)
    if not i % 3:
        min_try = min(min_try, dp[i // 3] + 1)
    dp[i] = min_try
print(dp[n])
