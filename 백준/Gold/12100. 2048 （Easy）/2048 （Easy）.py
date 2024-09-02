"""
BOJ : 2048(Easy)

시작 시간 : 3시 45분
구상 완료 : 3시 47분
제출 시간 : 4시 06분

"""

n = int(input())
original_board = [list(map(int, input().split())) for _ in range(n)]
biggest = max(max(line) for line in original_board)

# 방향 : 오른,밑,왼,위로 밀기

for move_code in range(1024):
    board = [line[:] for line in original_board]
    for _ in range(5):
        move = move_code % 4
        move_code >>= 2

        if not move:
            for i in range(n):
                moved_line_from_right = []
                before = -1
                for j in range(n - 1, -1, -1):
                    num = board[i][j]
                    if not num:
                        continue
                    if num == before:
                        moved_line_from_right[-1] <<= 1
                        before = -1
                        if num == biggest:
                            biggest <<= 1
                    else:
                        moved_line_from_right.append(num)
                        before = num
                    board[i][j] = 0
                for idx, num in enumerate(moved_line_from_right, 1):
                    board[i][n - idx] = num

        elif move == 1:
            for j in range(n):
                moved_line_from_bottom = []
                before = -1
                for i in range(n - 1, -1, -1):
                    num = board[i][j]
                    if not num:
                        continue
                    if num == before:
                        moved_line_from_bottom[-1] <<= 1
                        before = -1
                        if num == biggest:
                            biggest <<= 1
                    else:
                        moved_line_from_bottom.append(num)
                        before = num
                    board[i][j] = 0
                for idx, num in enumerate(moved_line_from_bottom, 1):
                    board[n - idx][j] = num

        elif move == 2:
            for i in range(n):
                moved_line_from_left = []
                before = -1
                for j in range(n):
                    num = board[i][j]
                    if not num:
                        continue
                    if num == before:
                        moved_line_from_left[-1] <<= 1
                        before = -1
                        if num == biggest:
                            biggest <<= 1
                    else:
                        moved_line_from_left.append(num)
                        before = num
                    board[i][j] = 0
                for idx, num in enumerate(moved_line_from_left):
                    board[i][idx] = num

        else:
            for j in range(n):
                moved_line_from_top = []
                before = -1
                for i in range(n):
                    num = board[i][j]
                    if not num:
                        continue
                    if num == before:
                        moved_line_from_top[-1] <<= 1
                        before = -1
                        if num == biggest:
                            biggest <<= 1
                    else:
                        moved_line_from_top.append(num)
                        before = num
                    board[i][j] = 0
                for idx, num in enumerate(moved_line_from_top):
                    board[idx][j] = num

print(biggest)
