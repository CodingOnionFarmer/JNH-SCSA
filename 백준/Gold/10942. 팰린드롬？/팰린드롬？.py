import sys

n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
pal = [[1] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n - i):
        if not pal[j + 1][j + i - 1] or nums[j] != nums[j + i]:
            pal[j][j + i] = 0
m = int(input())
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(pal[s - 1][e - 1])
