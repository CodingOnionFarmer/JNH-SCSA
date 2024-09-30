"""
24.09.30 (월)

BOJ : 새벽의 탐정 게임

1회차 (현재)
목표 풀이 시간 : 40분 이내

시작 시간 : 5시 32분
구상 완료 : 5시 38분
제출 완료 : 5시 53분
"""

# 바닥0 오른1 앞2 왼3 뒤4 위5

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상
roll_blank = ((3, 0, 2, 5, 4, 1), (4, 1, 0, 3, 5, 2), (1, 5, 2, 0, 4, 3), (2, 1, 5, 3, 0, 4))

n, m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for j, char in enumerate(line):
        if char == '#':
            board[i].append(1)
        else:
            board[i].append(0)
            if char == 'D':
                sx, sy = i, j
            elif char == 'R':
                ex, ey = i, j


def bfs():
    visited = [[[False] * m for _ in range(n)] for _ in range(6)]
    visited[0][sx][sy] = True
    q = [(0, sx, sy)]
    step = 0
    while q:
        step += 1
        nq = []
        for cbd, cx, cy in q:  # current blank direction
            for d, (dx, dy) in enumerate(directions):
                nx, ny = cx + dx, cy + dy
                if board[nx][ny]:
                    continue
                nbd = roll_blank[d][cbd]
                if visited[nbd][nx][ny]:
                    continue
                if nx == ex and ny == ey:
                    if nbd:
                        continue
                    print(step)
                    return
                visited[nbd][nx][ny] = True
                nq.append((nbd, nx, ny))
        q = nq
    print(-1)
    return


bfs()
