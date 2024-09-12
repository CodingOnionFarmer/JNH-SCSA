"""
BOJ : 마법사 상어와 블리자드

시작 시간 : 3시 13분
구상 완료 : 3시 31분
1회 오답 : 4시 08분
제출 시간 :

"""

# 구현, 시뮬레이션, 조건 분기, 규칙성 파악

directions = ((), (-1, 0), (1, 0), (0, -1), (0, 1))
ccw = (0, 3, 4, 2, 1)

n, m = map(int, input().split())
max_size = n * n - 1

blizzard = [[set()] for _ in range(5)]

ldru = (3, 2, 4, 1)
ldru_num = [0, 0, 0, 0, 0]

num = -1
for cycle in range(n >> 1):
    for d in ldru:
        num += 2
        ldru_num[d] += num
        blizzard[d].append(blizzard[d][cycle] | {ldru_num[d]})

# 단위 테스트
# print(blizzard)

board = [list(map(int, input().split())) for _ in range(n)]
beads = []


def fill():
    cr = cc = n >> 1
    cd = 3  # 왼쪽
    for layer in range(n >> 1):
        for ld in range(2):
            dr, dc = directions[cd]
            for move in range(layer << 1 | 1):
                cr += dr
                cc += dc
                if board[cr][cc]:
                    beads.append(board[cr][cc])
                else:
                    return
            cd = ccw[cd]
        for ru in range(2):
            dr, dc = directions[cd]
            for move in range(layer + 1 << 1):
                cr += dr
                cc += dc
                if board[cr][cc]:
                    beads.append(board[cr][cc])
                else:
                    return
            cd = ccw[cd]

    # 마지막 왼쪽 이동
    dr, dc = directions[cd]
    for move in range(n - 1):
        cr += dr
        cc += dc
        if board[cr][cc]:
            beads.append(board[cr][cc])
        else:
            return
    return


fill()
# 단위 테스트
# print(beads)


exploded = 0
for magic in range(m):
    d, s = map(int, input().split())
    destroyed = blizzard[d][s]
    new_beads = []
    for idx, num in enumerate(beads, 1):
        if idx in destroyed:
            continue
        if not new_beads:
            new_beads.append(1)
            new_beads.append(num)
        else:
            if num == new_beads[-1]:
                new_beads[-2] += 1
            else:
                if new_beads[-2] > 3:
                    exploded += new_beads[-1] * new_beads[-2]
                    new_beads.pop()
                    new_beads.pop()
                new_beads.append(1)
                new_beads.append(num)
    if new_beads and new_beads[-2] > 3:
        exploded += new_beads[-1] * new_beads[-2]
        new_beads.pop()
        new_beads.pop()

    explode = True
    while new_beads and explode:
        explode = False
        new_new_beads = [new_beads[0], new_beads[1]]
        for i in range(1, len(new_beads) >> 1):
            cnt, num = new_beads[i << 1], new_beads[i << 1 | 1]
            if not new_new_beads:
                new_new_beads.append(cnt)
                new_new_beads.append(num)
            else:
                if num == new_new_beads[-1]:
                    new_new_beads[-2] += cnt
                else:
                    if new_new_beads[-2] > 3:
                        explode = True
                        exploded += new_new_beads[-1] * new_new_beads[-2]
                        new_new_beads.pop()
                        new_new_beads.pop()
                    new_new_beads.append(cnt)
                    new_new_beads.append(num)
        if new_new_beads and new_new_beads[-2] > 3:
            exploded += new_new_beads[-1] * new_new_beads[-2]
            new_new_beads.pop()
            new_new_beads.pop()

        new_beads = new_new_beads

    if len(new_beads) > max_size:
        for over in range(len(new_beads) - max_size):
            new_beads.pop()
    beads = new_beads

print(exploded)
