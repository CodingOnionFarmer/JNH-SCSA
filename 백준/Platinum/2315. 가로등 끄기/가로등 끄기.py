n, m = map(int, input().split())
m -= 1
lights = [list(map(int, input().split())) for _ in range(n)]
big = 10 ** 9
dp = [[[big, big, 0] for _ in range(n - m)] for __ in range(m + 1)]
# dp[a][b][0,1] = 왼a 오b번 움직였을때 낭비된 전력 최소값, 왼쪽이면0 오른쪽이면1, dp[a][b][2]:남은가로등 초당전력
dp[0][0][0] = 0
dp[0][0][1] = 0
dp[0][0][2] = sum(lights[i][1] for i in range(n)) - lights[m][1]
for i in range(m):
    dp[i + 1][0][0] = dp[i][0][0] + dp[i][0][2] * (lights[m - i][0] - lights[m - i - 1][0])
    dp[i + 1][0][2] = dp[i][0][2] - lights[m - i - 1][1]
for j in range(n - m - 1):
    dp[0][j + 1][1] = dp[0][j][1] + dp[0][j][2] * (lights[m + j + 1][0] - lights[m + j][0])
    dp[0][j + 1][2] = dp[0][j][2] - lights[m + j + 1][1]
for i in range(m):
    for j in range(n - m - 1):
        dp[i + 1][j + 1][0] = min(dp[i][j + 1][0] + dp[i][j + 1][2] * (lights[m - i][0] - lights[m - i - 1][0]),
                                  dp[i][j + 1][1] + dp[i][j + 1][2] * (lights[m + j + 1][0] - lights[m - i - 1][0]))
        dp[i + 1][j + 1][1] = min(dp[i + 1][j][0] + dp[i + 1][j][2] * (lights[m + j + 1][0] - lights[m - i - 1][0]),
                                  dp[i + 1][j][1] + dp[i + 1][j][2] * (lights[m + j + 1][0] - lights[m + j][0]))
        dp[i + 1][j + 1][2] = dp[i + 1][j][2] - lights[m + j + 1][1]
print(min(dp[m][n - m - 1][k] for k in range(2)))
