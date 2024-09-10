# Dynamic Programming

n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0, 0, 0] for __ in range(n)] for _ in range(n)]  # 가로 대각 세로
dp[0][1][0] = 1

for j in range(2, n):
    if house[0][j]:
        break
    dp[0][j][0] = 1

for i in range(1, n):
    for j in range(2, n):
        if not house[i][j]:
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][1]
            dp[i][j][2] = dp[i - 1][j][1] + dp[i - 1][j][2]
            if not house[i - 1][j] and not house[i][j - 1]:
                dp[i][j][1] = sum(dp[i - 1][j - 1])

print(sum(dp[n - 1][n - 1]))
