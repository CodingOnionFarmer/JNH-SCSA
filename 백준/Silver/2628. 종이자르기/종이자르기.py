w, h = map(int, input().split())
n = int(input())
yx = [[0, h], [0, w]]
for _ in range(n):
    d, cut = map(int, input().split())
    yx[d].append(cut)
yx[0].sort()
yx[1].sort()
print(max(yx[0][i + 1] - yx[0][i] for i in range(len(yx[0]) - 1)) * max(
    yx[1][j + 1] - yx[1][j] for j in range(len(yx[1]) - 1)))
