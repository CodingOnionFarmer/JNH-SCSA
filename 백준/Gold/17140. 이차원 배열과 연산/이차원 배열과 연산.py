"""
BOJ : 마법사 상어와 파이어볼

시작 시간 : 2시 32분
구상 완료 : 2시 38분
테케 틀림 : 2시 57분, 3시 01분, 3시 02분
제출 시간 : 3시 05분
"""

r, c, k = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
for i in range(3):
    n1, n2, n3 = map(int, input().split())
    board[i][0] = n1
    board[i][1] = n2
    board[i][2] = n3
r -= 1
c -= 1
r_size = 3
c_size = 3
time = 0

while time <= 100 and board[r][c] != k:
    if r_size >= c_size:
        new_c_size = 0
        for i in range(r_size):
            cnt_numbers = {}
            for j in range(c_size):
                num = board[i][j]
                if not num:
                    continue
                if num in cnt_numbers:
                    cnt_numbers[num] += 1
                else:
                    cnt_numbers[num] = 1
            sorted_cnt_numbers = sorted([(cnt, num) for num, cnt in cnt_numbers.items()])
            cs = min(100, len(sorted_cnt_numbers) << 1)
            if cs > new_c_size:
                new_c_size = cs
            if cs < c_size:
                for cj in range(cs, c_size):
                    board[i][cj] = 0
            for cj in range(cs):
                board[i][cj] = sorted_cnt_numbers[cj >> 1][1 ^ cj & 1]
        c_size = new_c_size
    else:
        new_r_size = 0
        for j in range(c_size):
            cnt_numbers = {}
            for i in range(r_size):
                num = board[i][j]
                if not num:
                    continue
                if num in cnt_numbers:
                    cnt_numbers[num] += 1
                else:
                    cnt_numbers[num] = 1
            sorted_cnt_numbers = sorted([(cnt, num) for num, cnt in cnt_numbers.items()])
            rs = min(100, len(sorted_cnt_numbers) << 1)
            if rs > new_r_size:
                new_r_size = rs
            if rs < r_size:
                for ri in range(rs, r_size):
                    board[ri][j] = 0
            for ri in range(rs):
                board[ri][j] = sorted_cnt_numbers[ri >> 1][1 ^ ri & 1]
        r_size = new_r_size
    time += 1
    # print('------------------')
    # print(time)
    # for line in board[:r_size]:
    #     print(line[:c_size])

if time == 101:
    time = -1
print(time)
