"""
BOJ : 낚시왕

시작 시간 : 9시 01분
구상 완료 : 9시 03분
제출 시간 : 9시 38분
"""

# 1위 2아래 3오른 4왼
directions = (0, -1, 1, 1, -1)

r, c, m = map(int, input().split())
board = [[0] * c for _ in range(r)]
where_shark = set()
sharks = [[0, 0] for _ in range(10001)]
for i in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = z
    if d < 3:
        s %= 2 * r - 2
    else:
        s %= 2 * c - 2
    sharks[z] = [s, d]
    where_shark.add(x * c + y)

ans = 0
for column in range(c):
    # print('-------------------------')
    # for line in board:
    #     print(line)
    # print(ans)
    for row in range(r):
        if board[row][column]:
            ans += board[row][column]
            board[row][column] = 0
            where_shark.discard(row * c + column)
            break
    moved = [[0] * c for _ in range(r)]
    moved_where = set()
    for position in where_shark:
        x, y = position // c, position % c
        weight = board[x][y]
        speed, direction = sharks[weight]
        if direction > 2:
            ny = y + directions[direction] * speed
            if ny < 0:
                ny = -ny
                if ny >= c:
                    ny = c * 2 - ny - 2
                else:
                    sharks[weight][1] = 7 - direction
            elif ny >= c:
                ny = c * 2 - ny - 2
                if ny < 0:
                    ny = -ny
                else:
                    sharks[weight][1] = 7 - direction
            if moved[x][ny] < weight:
                moved[x][ny] = weight
                moved_where.add(x * c + ny)
        else:
            nx = x + directions[direction] * speed
            # print(x,nx,y,speed,direction)
            if nx < 0:
                nx = -nx
                if nx >= r:
                    nx = r * 2 - nx - 2
                else:
                    sharks[weight][1] = 3 - direction
            elif nx >= r:
                nx = r * 2 - nx - 2
                if nx < 0:
                    nx = -nx
                else:
                    sharks[weight][1] = 3 - direction
            # print(nx,y)
            if moved[nx][y] < weight:
                moved[nx][y] = weight
                moved_where.add(nx * c + y)
    board = moved
    where_shark = moved_where

print(ans)
