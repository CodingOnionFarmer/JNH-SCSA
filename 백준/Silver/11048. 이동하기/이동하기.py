import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
dp = list(map(int, input().split()))
for j in range(1, m):
    dp[j] += dp[j - 1]
for i in range(n - 1):
    candies = list(map(int, input().split()))
    dp[0] += candies[0]
    for j in range(1, m):
        dp[j] = max(dp[j], dp[j - 1]) + candies[j]
print(dp[m - 1])
