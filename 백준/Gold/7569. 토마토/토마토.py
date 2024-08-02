import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

m, n, h = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
directions = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
great_tomatoes = []
bad_tomatoes = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                great_tomatoes.append((i, j, k))
            elif not box[i][j][k]:
                bad_tomatoes += 1
date = 0
while great_tomatoes and bad_tomatoes:
    will_be_great = []
    for ci, cj, ck in great_tomatoes:
        for di, dj, dk in directions:
            ni, nj, nk = ci + di, cj + dj, ck + dk
            if 0 <= ni < h and 0 <= nj < n and 0 <= nk < m and not box[ni][nj][nk]:
                will_be_great.append((ni, nj, nk))
                box[ni][nj][nk] = 1
                bad_tomatoes -= 1
    great_tomatoes = will_be_great
    date += 1
if bad_tomatoes:
    date = -1
print(date)
