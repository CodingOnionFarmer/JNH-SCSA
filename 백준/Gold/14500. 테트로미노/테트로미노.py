import sys

n, m = map(int, input().split())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
score = 0
for i in range(n):
    s = paper[i][0] + paper[i][1] + paper[i][2]
    for j in range(3, m):
        s += paper[i][j]
        if s > score:
            score = s
        s -= paper[i][j - 3]
for i in range(m):
    t = paper[0][i] + paper[1][i] + paper[2][i]
    for j in range(3, n):
        t += paper[j][i]
        if t > score:
            score = t
        t -= paper[j - 3][i]
for i in range(n - 1):
    for j in range(m - 1):
        s = paper[i][j] + paper[i][j + 1] + paper[i + 1][j] + paper[i + 1][j + 1]
        if s > score:
            score = s
for i in range(n - 1):
    for j in range(m - 2):
        r = [paper[i][j], paper[i][j + 1], paper[i][j + 2], paper[i + 1][j], paper[i + 1][j + 1], paper[i + 1][j + 2]]
        s = r[0] + r[1] + r[2] + r[3]
        if s > score:
            score = s
        s += r[4] - r[3]
        if s > score:
            score = s
        s += r[5] - r[4]
        if s > score:
            score = s
        s += r[4] - r[2]
        if s > score:
            score = s
        s += r[3] - r[1]
        if s > score:
            score = s
        s += r[1] - r[0]
        if s > score:
            score = s
        s += r[2] - r[1]
        if s > score:
            score = s
        s += r[1] - r[5]
        if s > score:
            score = s
for i in range(m - 1):
    for j in range(n - 2):
        r = [paper[j][i], paper[j + 1][i], paper[j + 2][i], paper[j][i + 1], paper[j + 1][i + 1], paper[j + 2][i + 1]]
        s = r[0] + r[1] + r[2] + r[3]
        if s > score:
            score = s
        s += r[4] - r[3]
        if s > score:
            score = s
        s += r[5] - r[4]
        if s > score:
            score = s
        s += r[4] - r[2]
        if s > score:
            score = s
        s += r[3] - r[1]
        if s > score:
            score = s
        s += r[1] - r[0]
        if s > score:
            score = s
        s += r[2] - r[1]
        if s > score:
            score = s
        s += r[1] - r[5]
        if s > score:
            score = s
print(score)
