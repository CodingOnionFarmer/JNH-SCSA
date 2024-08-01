import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
height = [list(map(int, input().split())) for _ in range(n)]
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

MIN = MAX = height[0][0]
for i in range(n):
    for j in range(n):
        if MIN > height[i][j]:
            MIN = height[i][j]
        elif MAX < height[i][j]:
            MAX = height[i][j]


def dfs(ci, cj, depth):
    visited[ci][cj] = True
    for di, dj in direction:
        ni = ci + di
        nj = cj + dj
        if 0 <= ni < n and 0 <= nj < n and height[ni][nj] > depth and not visited[ni][nj]:
            dfs(ni, nj, depth)


ans = 1
for rain in range(MIN, MAX):
    island = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if height[i][j] > rain and not visited[i][j]:
                island += 1
                dfs(i, j, rain)
    if island > ans:
        ans = island
print(ans)
