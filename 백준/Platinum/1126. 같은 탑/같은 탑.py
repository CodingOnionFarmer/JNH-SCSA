n = int(input())
blocks = list(map(int, input().split()))
highest = sum(blocks) // 2

# dp[i][h]는 i번째 블록까지 탐색했을 때 높이 차가 h인 경우를 만들 수 있는 경우, 더 높은 탑의 높이의 최댓값 (처음엔 불가능한 상태로 표시)
dp = [[-highest] * (highest + 1) for _ in range(n)]
dp[0][0] = 0
hd = {0}  # height difference
if blocks[0] <= highest:
    dp[0][blocks[0]] = blocks[0]
    hd.add(blocks[0])
for i in range(1, n):
    block = blocks[i]
    new_hd = set()
    for diff in hd:
        high = dp[i - 1][diff]
        low = high - diff
        dp[i][diff] = max(dp[i][diff], high)
        new_hd.add(diff)
        if high + block <= highest:
            dp[i][diff + block] = max(dp[i][diff + block], high + block)
            new_hd.add(diff + block)
        if low + block <= highest:
            if low + block <= high:
                dp[i][diff - block] = max(dp[i][diff - block], high)
                new_hd.add(diff - block)
            else:
                dp[i][block - diff] = max(dp[i][block - diff], low + block)
                new_hd.add(block - diff)
    hd = new_hd
ans = dp[n - 1][0]
if not ans:
    ans = -1
print(ans)
