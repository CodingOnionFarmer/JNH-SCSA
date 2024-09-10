"""
BOJ : 주사위 굴리기 2

시작 시간 : 2시 4분
구상 완료 : 2시 6분
제출 시간 : 2시 27분
"""

# BFS, 구현, 시뮬레이션
# 메모이제이션(또는 dp) <- 선택 : 일단 없이 브루트포스

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른 밑 왼 위, 시계방향+1, 반시계방향-1

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
score = [[0] * m for _ in range(n)]
head = [[None] * m for _ in range(n)]  # visited 대신 대표 위치 저장
oob = [[False] * m + [True] for _ in range(n)] + [[True] * m]

for i in range(n):
    for j in range(m):
        if not head[i][j]:
            head[i][j] = (i, j)
            num = board[i][j]
            q = [(i, j)]
            cnt = 1
            while q:
                nq = []
                for x, y in q:
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if not oob[nx][ny] and not head[nx][ny] and board[nx][ny] == num:
                            head[nx][ny] = (i, j)
                            cnt += 1
                            nq.append((nx, ny))
                q = nq
            score[i][j] = num * cnt
        else:
            hi, hj = head[i][j]
            score[i][j] = score[hi][hj]

d = 0
cx, cy = 0, 0

top = 1
bottom = 6
east = 3
west = 4
north = 2
south = 5

ans = 0

for roll in range(k):
    dx, dy = directions[d]
    nx, ny = cx + dx, cy + dy

    # 밖으로 나가려고하면 반대방향
    if oob[nx][ny]:
        d = (d + 2) % 4
        dx, dy = directions[d]
        nx, ny = cx + dx, cy + dy
    cx, cy = nx, ny

    # 미리 구해둔 점수
    ans += score[cx][cy]

    # 동쪽
    if not d:
        top, east, bottom, west = west, top, east, bottom
    # 남쪽
    elif d == 1:
        top, south, bottom, north = north, top, south, bottom
    # 서쪽
    elif d == 2:
        top, west, bottom, east = east, top, west, bottom
    # 북쪽
    else:
        top, north, bottom, south = south, top, north, bottom

    # 밑면과 판의 숫자 비교 후 방향 전환
    num = board[cx][cy]
    if bottom > num:
        d = (d + 1) % 4
    elif bottom < num:
        d = (d - 1) % 4

print(ans)
