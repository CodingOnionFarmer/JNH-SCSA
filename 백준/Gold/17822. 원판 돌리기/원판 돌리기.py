"""
BOJ : 원판 돌리기

시작 시간 : 2시 46분
구상 완료 : 2시 50분
테케 틀림 : 3시 18분
제출 시간 : 3시 33분
"""

n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] + [[-50] * m]
line_rotated = [0] * n
num_cnt = n * m
num_sum = 0
for i in range(n):
    for j in range(m):
        num_sum += board[i][j]

# for line in board:
#     print(line)

for query in range(t):
    if num_cnt <= 1:
        break

    x, d, k = map(int, input().split())
    if d:
        k = m - k
    for line_num in range(x, n + 1, x):
        line_num -= 1
        line_rotated[line_num] -= k
        if line_rotated[line_num] <= -m:
            line_rotated[line_num] += m

    erase = [[False] * m for _ in range(n)]
    same = False

    for i in range(n):
        lr = line_rotated[i]
        lr_up = line_rotated[i - 1]
        for j in range(m):
            num = board[i][j + lr]
            if num == -50:
                continue

            left_num = board[i][j + lr - 1]
            up_num = board[i - 1][j + lr_up]
            if left_num == num:
                same = True
                if not erase[i][j + lr]:
                    erase[i][j + lr] = True
                    num_cnt -= 1
                    num_sum -= num
                if not erase[i][j + lr - 1]:
                    erase[i][j + lr - 1] = True
                    num_cnt -= 1
                    num_sum -= num
                if up_num == num and not erase[i - 1][j + lr_up]:
                    erase[i - 1][j + lr_up] = True
                    num_cnt -= 1
                    num_sum -= num
            elif up_num == num:
                same = True
                if not erase[i][j + lr]:
                    erase[i][j + lr] = True
                    num_cnt -= 1
                    num_sum -= num
                if not erase[i - 1][j + lr_up]:
                    erase[i - 1][j + lr_up] = True
                    num_cnt -= 1
                    num_sum -= num

    if same:
        for r in range(n):
            for c in range(m):
                if erase[r][c]:
                    board[r][c] = -50
    else:
        changed = 0
        for r in range(n):
            for c in range(m):
                if board[r][c] == -50:
                    continue
                is_num_over_average = board[r][c] * num_cnt
                if is_num_over_average > num_sum:
                    board[r][c] -= 1
                    changed -= 1
                elif is_num_over_average < num_sum:
                    board[r][c] += 1
                    changed += 1
        num_sum += changed

    # for line in board:
    #     print(line)

print(num_sum)
# for line in board:
#     print(line)
# print(line_rotated)
