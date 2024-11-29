n = int(input())
height = 0
while 1 << height <= n:
    height += 1
weight = [0] + list(map(int, input().split()))
# dp[d1][d2]는 현재 node를 마지막으로 하는 d1깊이~d2깊이의 직사각형의 최댓값
dp = [[-1000000001] * height for _ in range(height)]


def dfs(node, depth):
    lc = node << 1
    maximal = -1000000001
    if lc > n:
        for high in range(height):
            if dp[high][depth] < 0:
                dp[high][depth] = weight[node]
            else:
                dp[high][depth] += weight[node]
            if dp[high][depth] > maximal:
                maximal = dp[high][depth]
        return maximal
    lcm = dfs(lc, depth + 1)
    if lcm > maximal:
        maximal = lcm
    for high in range(depth + 1):
        for low in range(depth, height):
            if dp[high][low] < 0:
                dp[high][low] = weight[node]
            else:
                dp[high][low] += weight[node]
            if dp[high][low] > maximal:
                maximal = dp[high][low]
    rcm = dfs(lc | 1, depth + 1)
    if rcm > maximal:
        maximal = rcm
    return maximal


print(dfs(1, 0))
