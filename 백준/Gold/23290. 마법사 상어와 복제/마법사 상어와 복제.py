"""
BOJ : 마법사 상어와 복제

시작 시간 : 9시 01분
구상 완료 : 9시 14분
제출 시간 : 10시 16분
"""

m, s = map(int, input().split())

# 반시계는 -1
dir8 = ((1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0))

# 상 좌 하 우
dir4 = ((-1, 0), (0, -1), (1, 0), (0, 1))

# board[i][j][d]는 i,j칸에 d방향보고있는 물고기 수 (d = 8은 0으로)
board = [[[0] * 8 for __ in range(4)] for _ in range(4)]

for i in range(m):
    fx, fy, fd = map(int, input().split())
    board[fx - 1][fy - 1][fd % 8] += 1

sx, sy = map(int, input().split())
sx -= 1
sy -= 1
scent = [[0] * 4 for _ in range(4)]

for practice in range(s):
    # 1. 복제 마법 시전
    temp = [[block[:] for block in line] for line in board]

    # 2. 모든 물고기 한 칸 이동
    # 하기 전에 못 가는 칸 표시 (패딩 쳐서 oob도 거르기)
    can_go = [[True] * 4 + [False] for _ in range(4)] + [[False] * 5]
    for i in range(4):
        for j in range(4):
            if scent[i][j]:
                can_go[i][j] = False
    can_go[sx][sy] = False
    # 8방향 물고기들을 반시계 방향으로 회전
    # 하기 전에 board를 대체할 새 배열(move) 선언
    move = [[[0] * 8 for __ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            # i,j에서 8방향 중 갈 수 있는 곳 하나라도 있으면 모두 나가게 된다.
            if any(can_go[i + di][j + dj] for (di, dj) in dir8):
                fishes = 0
                for d in range(7, -1, -1):
                    di, dj = dir8[d]
                    if can_go[i + di][j + dj]:
                        move[i + di][j + dj][d] += fishes + board[i][j][d]
                        fishes = 0
                    else:
                        fishes += board[i][j][d]
                if fishes:
                    for d in range(7, -1, -1):
                        di, dj = dir8[d]
                        if can_go[i + di][j + dj]:
                            move[i + di][j + dj][d] += fishes
                            break
            # 8방향 다 못가면 그대로
            else:
                for d in range(8):
                    move[i][j][d] += board[i][j][d]

    # 움직인 상태를 원본 board로 복사
    board = [[block[:] for block in line] for line in move]

    # 3. 상어 3칸 이동
    # 방문처리를 하면 안 되면서 중복 방문할 때 물고기 수는 안 세야 한다는 점이 핵심이다. (상 하 상 같은 move가 최선일 수도 있다)
    fishes_in_the_block = [[sum(block) for block in line] for line in board]
    # 하기 전에 못 가는 칸 표시 (패딩 쳐서 oob 거르기) : 편의상 아까 한 거랑 반대로
    cant_go = [[False] * 4 + [True] for _ in range(4)] + [[True] * 5]
    will_move = [-1, -1, -1]
    erase_most = -1
    for move1, (dx1, dy1) in enumerate(dir4):
        nx1, ny1 = sx + dx1, sy + dy1
        if cant_go[nx1][ny1]:
            continue
        for move2, (dx2, dy2) in enumerate(dir4):
            nx2, ny2 = nx1 + dx2, ny1 + dy2
            if cant_go[nx2][ny2]:
                continue
            for move3, (dx3, dy3) in enumerate(dir4):
                nx3, ny3 = nx2 + dx3, ny2 + dy3
                if cant_go[nx3][ny3]:
                    continue
                # set으로 중복방문점 제거하고, 제거한 물고기 수 계산
                erase = sum(fishes_in_the_block[x][y] for x, y in {(nx1, ny1), (nx2, ny2), (nx3, ny3)})
                if erase > erase_most:
                    erase_most = erase
                    will_move = [move1, move2, move3]
    for move in will_move:
        dx, dy = dir4[move]
        sx += dx
        sy += dy
        # 냄새 남기려면 칸에 물고기가 있어야 된다
        if any(board[sx][sy]):
            scent[sx][sy] = 3
        # 해당 칸 물고기 전부 삭제
        board[sx][sy] = [0] * 8

    # 4. 두 턴 전에 생긴 냄새 삭제(를 하기 위해 scent를 선언 시 3으로 두고 1씩 줄인다)
    for i in range(4):
        for j in range(4):
            if scent[i][j]:
                scent[i][j] -= 1

    # 5. 복제 마법 적용
    for i in range(4):
        for j in range(4):
            for d in range(8):
                board[i][j][d] += temp[i][j][d]

print(sum(sum(sum(block) for block in line) for line in board))
