import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lab = [list(map(int, input().split())) for _ in range(n)]
for line in lab:
    line.append(5)
lab.append([5] * m)

# 0:우, 1:하, 2:좌, 3:상 순서대로
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)
# 0이나 9이면 방향 그대로, 1,2,3,4면 방향 전환
turnabout = ((0, 1, 2, 3), (2, 1, 0, 3), (0, 3, 2, 1), (3, 2, 1, 0), (1, 0, 3, 2), (), (), (), (), (0, 1, 2, 3))
# visited[i][j][d]는 i행 j열 d방향을 방문했는지 여부
visited = [[[False] * 4 for _ in range(m)] for __ in range(n)]

for i in range(n):
    for j in range(m):
        if lab[i][j] == 9:
            for d in range(4):
                ci = i
                cj = j
                cd = d
                while True:
                    num = lab[ci][cj]
                    if num == 5:
                        break
                    if visited[ci][cj][cd]:
                        break
                    visited[ci][cj][cd] = True
                    cd = turnabout[num][cd]
                    ci += di[cd]
                    cj += dj[cd]

ans = 0
for i in range(n):
    for j in range(m):
        for d in range(4):
            if visited[i][j][d]:
                ans += 1
                break
print(ans)
