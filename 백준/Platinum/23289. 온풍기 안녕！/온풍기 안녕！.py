"""
BOJ : 온풍기 안녕!

시작 시간 : 2시 29분
구상 완료 : 2시 44분
제출 시간 : 3시 21분
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른 밑 왼 위
heater_direction = (0, 0, 2, 3, 1)  # 1오른 2왼 3위 4아래

r, c, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
# 조사할 칸의 좌표 i,j
spectate = []
# 히터의 좌표 i,j와 방향 d
heaters = []
for i in range(r):
    for j in range(c):
        if board[i][j] == 5:
            spectate.append((i, j))
            board[i][j] = 0
        elif board[i][j]:
            heaters.append((i, j, heater_direction[board[i][j]]))
            board[i][j] = 0

wall = [[[False] * 4 for __ in range(c)] for _ in range(r)]  # 해당 칸에서 우하좌상으로 막혀있는지 아닌지
# out of bound 대신 테두리를 벽으로 막기
for i in range(r):
    wall[i][0][2] = True
    wall[i][c - 1][0] = True
for j in range(c):
    wall[0][j][3] = True
    wall[r - 1][j][1] = True

w = int(input())
for _ in range(w):
    x, y, t = map(int, input().split())
    # 인덱스 주의!
    x -= 1
    y -= 1
    if t:
        wall[x][y][0] = True
        wall[x][y + 1][2] = True
    else:
        wall[x][y][3] = True
        wall[x - 1][y][1] = True

# 히터 한번 틀면 오르는 온도
heated = [[0] * c for _ in range(r)]
for hx, hy, d in heaters:
    dx, dy = directions[d]
    left = (d - 1) % 4
    lx, ly = directions[left]
    right = (d + 1) % 4
    rx, ry = directions[right]
    # set으로 온풍이 겹치는 경우도 예외처리 없이 쉽게 구현하기
    heated[hx + dx][hy + dy] += 5
    line = {(hx + dx, hy + dy)}
    heat = 4
    while line and heat:
        next_line = set()
        for cx, cy in line:
            if not wall[cx][cy][left] and not wall[cx + lx][cy + ly][d]:
                nlx, nly = cx + lx + dx, cy + ly + dy
                if (nlx, nly) not in next_line:
                    next_line.add((nlx, nly))
                    heated[nlx][nly] += heat

            if not wall[cx][cy][d]:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in next_line:
                    next_line.add((nx, ny))
                    heated[nx][ny] += heat

            if not wall[cx][cy][right] and not wall[cx + rx][cy + ry][d]:
                nrx, nry = cx + rx + dx, cy + ry + dy
                if (nrx, nry) not in next_line:
                    next_line.add((nrx, nry))
                    heated[nrx][nry] += heat

        line = next_line
        heat -= 1

chocolate = 0
# 테스트 101번 이상이면 답 101로 낼 거니까 for문 101번
for test in range(101):
    # 1. 히터 틀기 (미리 계산해 둠)
    for i in range(r):
        for j in range(c):
            board[i][j] += heated[i][j]

    # 2. 온도 교환 (오른쪽,밑으로만 비교해서 중복 방지, 벽 활용)
    temp_change = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            # 오른쪽 뚫려있으면 오른쪽과 온도 교환
            if not wall[i][j][0]:
                diff = board[i][j] - board[i][j + 1]
                if diff > 3:
                    diff //= 4
                    temp_change[i][j] -= diff
                    temp_change[i][j + 1] += diff
                elif diff < -3:
                    diff = -diff // 4
                    temp_change[i][j] += diff
                    temp_change[i][j + 1] -= diff
            # 아래쪽 뚫려있으면 온도 교환
            if not wall[i][j][1]:
                diff = board[i][j] - board[i + 1][j]
                if diff > 3:
                    diff //= 4
                    temp_change[i][j] -= diff
                    temp_change[i + 1][j] += diff
                elif diff < -3:
                    diff = -diff // 4
                    temp_change[i][j] += diff
                    temp_change[i + 1][j] -= diff

    for i in range(r):
        for j in range(c):
            board[i][j] += temp_change[i][j]

    # 3. 테두리 온도 있으면 -1
    for i in range(r):
        if board[i][0]:
            board[i][0] -= 1
        if board[i][c - 1]:
            board[i][c - 1] -= 1
    for j in range(1, c - 1):
        if board[0][j]:
            board[0][j] -= 1
        if board[r - 1][j]:
            board[r - 1][j] -= 1

    # 4. 초콜릿먹기
    chocolate += 1

    # 5. 조사하는 칸 조사
    if all(board[x][y] >= k for x, y in spectate):
        break

print(chocolate)
