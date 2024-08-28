"""
BOJ : 미세먼지 안녕!
코드트리 : 시공의 돌풍

시작 시간 : 3시 20분
제출 시간 : 3시 19분
소요 시간 : 18분
"""

n, m, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
for i in range(2, n - 1):
    if room[i][0] == -1:
        wind_up = i
        break
wind_down = wind_up + 1
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
adj = [[[] for _ in range(m)] for __ in range(n)]
for i in range(n):
    for j in range(m):
        if not j and i in (wind_down, wind_up):
            continue
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in ((wind_up, 0), (wind_down, 0)):
                adj[i][j].append((ni, nj))

for second in range(t):
    change = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            spread = room[i][j] // 5
            if spread:
                change[i][j] -= spread * len(adj[i][j])
                for ni, nj in adj[i][j]:
                    change[ni][nj] += spread
    for i in range(n):
        for j in range(m):
            room[i][j] += change[i][j]

    for i in range(wind_up - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    for j in range(m - 1):
        room[0][j] = room[0][j + 1]
    for i in range(wind_up):
        room[i][-1] = room[i + 1][-1]
    for j in range(m - 1, 1, -1):
        room[wind_up][j] = room[wind_up][j - 1]
    room[wind_up][1] = 0

    for i in range(wind_down + 1, n - 1):
        room[i][0] = room[i + 1][0]
    for j in range(m - 1):
        room[-1][j] = room[-1][j + 1]
    for i in range(n - 1, wind_down, -1):
        room[i][-1] = room[i - 1][-1]
    for j in range(m - 1, 1, -1):
        room[wind_down][j] = room[wind_down][j - 1]
    room[wind_down][1] = 0

print(sum(sum(line) for line in room) + 2)
