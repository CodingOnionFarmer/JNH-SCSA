n = int(input())
paper = [[0] * 100 for _ in range(100)]
for p in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1
ans = 0
for i in range(100):
    ans += paper[i][0] + paper[i][99] + paper[0][i] + paper[99][i]
    for j in range(99):
        ans += paper[i][j] ^ paper[i][j + 1]
        ans += paper[j][i] ^ paper[j + 1][i]
print(ans)
