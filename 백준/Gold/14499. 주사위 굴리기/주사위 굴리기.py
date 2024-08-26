"""
시작 시간 : 3시 16분
제출 시간 : 3시 33분
"""

# 구현, 시뮬레이션

n, m, cx, cy, k = map(int, input().split())
up = 0  # 윗면
down = 0  # 밑면
E, S, W, N = 0, 0, 0, 0  # 동 남 서 북
board = [list(map(int, input().split())) + [-1] for _ in range(n)] + [[-1] * m]
orders = list(map(int, input().split()))
answer = []
for order in orders:
    if order == 1:  # 동쪽
        nx, ny = cx, cy + 1
        if board[nx][ny] < 0:  # 벗어나면 무효
            continue
        E, up, W, down = up, W, down, E  # 회전
        if board[nx][ny]:
            down = board[nx][ny]
            board[nx][ny] = 0
        else:
            board[nx][ny] = down
        answer.append(up)
        cx, cy = nx, ny
    elif order == 2:  # 서쪽
        nx, ny = cx, cy - 1
        if board[nx][ny] < 0:  # 벗어나면 무효
            continue
        E, up, W, down = down, E, up, W  # 회전
        if board[nx][ny]:
            down = board[nx][ny]
            board[nx][ny] = 0
        else:
            board[nx][ny] = down
        answer.append(up)
        cx, cy = nx, ny
    elif order == 3:  # 북쪽
        nx, ny = cx - 1, cy
        if board[nx][ny] < 0:  # 벗어나면 무효
            continue
        N, up, S, down = up, S, down, N  # 회전
        if board[nx][ny]:
            down = board[nx][ny]
            board[nx][ny] = 0
        else:
            board[nx][ny] = down
        answer.append(up)
        cx, cy = nx, ny
    else:  # 남쪽
        nx, ny = cx + 1, cy
        if board[nx][ny] < 0:  # 벗어나면 무효
            continue
        N, up, S, down = down, N, up, S  # 회전
        if board[nx][ny]:
            down = board[nx][ny]
            board[nx][ny] = 0
        else:
            board[nx][ny] = down
        answer.append(up)
        cx, cy = nx, ny
print(*answer, sep='\n')
