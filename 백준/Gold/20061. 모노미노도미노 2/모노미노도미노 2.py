"""
BOJ : 모노미노도미노 2

시작 시간 : 3시 10분
구상 완료 : 3시 15분
1회 오답 : 3시 47분
2회 오답 : 4시 01분
제출 시간 : 

"""

######################
# 룩업 테이블부터 만들기
# t x y 받아서 green에 떨굴 거랑 blue에 떨굴 거, 떨어지는 모양과 두께를 저장한다.
blocks = [[[None] * 4 for x in range(4)] for t in range(4)]  # t가 0인 곳은 안 쓸 것
for x in range(4):
    for y in range(4):
        # 경계 넘어가는 입력 안준댔으니 딱히 예외처리 안해도됨
        # 각 튜플은 green에 떨어지는 모양과 두께, blue에 떨어지는 모양과 두께 순이다.
        blocks[1][x][y] = (1 << y, 1, 1 << x, 1)
        blocks[2][x][y] = (3 << y, 1, 1 << x, 2)
        blocks[3][x][y] = (1 << y, 2, 3 << x, 1)

# 이거 찍어서 복붙하면 위의 코드 생략하고 하드코딩도 가능
# for line in blocks:
#     print(line)

# 마지막에 칸수 세는 용도
cnt_blocks = [0] * 16
for digit in range(4):
    bit = 1 << digit
    for i in range(16):
        if i & bit:
            cnt_blocks[i] += 1

######################
# 입력 받고 자료구조 만들기 (비트마스킹 활용)
n = int(input())
# Green의 각 행, Blue의 각 열을 0000~1111의 비트로 나타내기, 1이 블록이 있는 곳이다.
G_board = [0] * 6
B_board = [0] * 6

######################
score = 0
for turn in range(n):
    t, x, y = map(int, input().split())
    green, gs, blue, bs = blocks[t][x][y]

    dropped_line = 1
    for drop in range(4):
        if green & G_board[dropped_line + 1]:
            break
        dropped_line += 1
    for line in range(dropped_line, dropped_line - gs, -1):
        G_board[line] |= green
    if G_board[dropped_line] == 15:
        score += 1
        erased = 1
        if gs == 2 and G_board[dropped_line - 1] == 15:
            score += 1
            erased += 1
        for line in range(dropped_line, 1, -1):
            G_board[line] = G_board[line - erased]
        G_board[0] = 0
        G_board[1] = 0
    elif gs == 2 and G_board[dropped_line - 1] == 15:
        score += 1
        for line in range(dropped_line - 1, 1, -1):
            G_board[line] = G_board[line - 1]
        G_board[0] = 0
        G_board[1] = 0

    if G_board[1]:
        drop = 1
        if G_board[0]:
            drop += 1
        for line in range(5, 1, -1):
            G_board[line] = G_board[line - drop]
        G_board[0] = 0
        G_board[1] = 0

    dropped_line = 1
    for drop in range(4):
        if blue & B_board[dropped_line + 1]:
            break
        dropped_line += 1
    for line in range(dropped_line, dropped_line - bs, -1):
        B_board[line] |= blue
    if B_board[dropped_line] == 15:
        score += 1
        erased = 1
        if bs == 2 and B_board[dropped_line - 1] == 15:
            score += 1
            erased += 1
        for line in range(dropped_line, 1, -1):
            B_board[line] = B_board[line - erased]
        B_board[0] = 0
        B_board[1] = 0
    elif bs == 2 and B_board[dropped_line - 1] == 15:
        score += 1
        for line in range(dropped_line - 1, 1, -1):
            B_board[line] = B_board[line - 1]
        B_board[0] = 0
        B_board[1] = 0

    if B_board[1]:
        drop = 1
        if B_board[0]:
            drop += 1
        for line in range(5, 1, -1):
            B_board[line] = B_board[line - drop]
        B_board[0] = 0
        B_board[1] = 0

print(score)
print(sum(cnt_blocks[line] for line in G_board) + sum(cnt_blocks[line] for line in B_board))
