"""
BOJ : 마법사 상어와 토네이도

시작 시간 : 2시 06분
구상 완료 : 2시 12분
테케 틀림 : 2시 39분, 2시 52분
제출 시간 : 2시 58분


구상 때 생각한 것
1. 토네이도를 함수나 리스트로 만들고, 배열 회전으로 만들 수도 있지만,
    그냥 for문 네번 돌려도 안 헷갈릴 자신 있으므로 그냥 구현한다.
구상 중에 생각한 것
1. 구현 도중에 그냥 함수화하는게 보기 좋을 것 같아서 함수로 만들기로 생각 바꿈
    -> 함수화하는 김에 많이들 쓰는 oob 써보기
    -> 이거 다 하고 생각한 것 : blow_k_percent도 함수로 만들걸...

"""

# 왼 밑 오른 위 순으로 한 바퀴가 1사이클
# n//2사이클만큼 돌고 왼쪽으로 한 번 이동하고 끝

directions = ((0, -1), (1, 0), (0, 1), (-1, 0))  # 왼 밑 오른 위

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]


def oob(x, y):
    if 0 <= x < n and 0 <= y < n:
        return False
    return True


def tornado(x, y, d):
    sand = board[x][y]
    board[x][y] = 0
    remain = sand
    dx, dy = directions[d]
    nx, ny = x + dx, y + dy

    if sand < 10:
        if oob(nx, ny):
            return remain
        board[nx][ny] += remain
        return 0
    blow_outside = 0
    blow_10percent = sand // 10
    remain -= blow_10percent << 1
    dl, dr = (d + 1) % 4, (d - 1) % 4
    dlx, dly = directions[dl]
    drx, dry = directions[dr]
    nlx, nly, nrx, nry = nx + dlx, ny + dly, nx + drx, ny + dry
    if oob(nlx, nly):
        blow_outside += blow_10percent
    else:
        board[nlx][nly] += blow_10percent
    if oob(nrx, nry):
        blow_outside += blow_10percent
    else:
        board[nrx][nry] += blow_10percent

    if sand < 15:
        if oob(nx, ny):
            return blow_outside + remain
        board[nx][ny] += remain
        return blow_outside
    blow_7percent = sand * 7 // 100
    remain -= blow_7percent << 1
    nlx, nly, nrx, nry = x + dlx, y + dly, x + drx, y + dry
    if oob(nlx, nly):
        blow_outside += blow_7percent
    else:
        board[nlx][nly] += blow_7percent
    if oob(nrx, nry):
        blow_outside += blow_7percent
    else:
        board[nrx][nry] += blow_7percent

    if sand < 20:
        if oob(nx, ny):
            return blow_outside + remain
        board[nx][ny] += remain
        return blow_outside
    blow_5percent = sand // 20
    remain -= blow_5percent

    # 와... ny+dy 해야되는데 nx+dy 해놓고 11분동안 찾았네....
    nnx, nny = nx + dx, ny + dy
    # print('nnx:', nnx, 'nny:', nny)
    # print('nx,ny:', nx, ny, 'dx,dy,d:', dx, dy, d)
    #
    # for line in board:
    #     print(line)
    if oob(nnx, nny):
        blow_outside += blow_5percent
    else:
        board[nnx][nny] += blow_5percent

    if sand < 50:
        if oob(nx, ny):
            return blow_outside + remain
        board[nx][ny] += remain
        return blow_outside
    blow_2percent = sand // 50
    remain -= blow_2percent << 1
    nlx, nly, nrx, nry = x + dlx * 2, y + dly * 2, x + drx * 2, y + dry * 2
    if oob(nlx, nly):
        blow_outside += blow_2percent
    else:
        board[nlx][nly] += blow_2percent
    if oob(nrx, nry):
        blow_outside += blow_2percent
    else:
        board[nrx][nry] += blow_2percent

    if sand < 100:
        if oob(nx, ny):
            return blow_outside + remain
        board[nx][ny] += remain
        return blow_outside
    blow_1percent = sand // 100
    remain -= blow_1percent << 1
    nlx, nly, nrx, nry = x - dx + dlx, y - dy + dly, x - dx + drx, y - dy + dry
    if oob(nlx, nly):
        blow_outside += blow_1percent
    else:
        board[nlx][nly] += blow_1percent
    if oob(nrx, nry):
        blow_outside += blow_1percent
    else:
        board[nrx][nry] += blow_1percent

    if oob(nx, ny):
        return blow_outside + remain
    board[nx][ny] += remain
    return blow_outside


ci, cj = n >> 1, n >> 1
blown = 0
for c in range(n >> 1):
    # 왼쪽 이동
    di, dj = directions[0]
    for _ in range(c << 1 | 1):
        ci += di
        cj += dj
        blown += tornado(ci, cj, 0)
        # print('--------------')
        # print(ci, cj, blown)
        # for line in board:
        #     print(line)

    # 아래 이동
    di, dj = directions[1]
    for _ in range(c << 1 | 1):
        ci += di
        cj += dj
        blown += tornado(ci, cj, 1)
        # print('--------------')
        # print(ci, cj, blown)
        # for line in board:
        #     print(line)

    # 오른쪽 이동
    di, dj = directions[2]
    for _ in range(c + 1 << 1):
        ci += di
        cj += dj
        blown += tornado(ci, cj, 2)
        # print('--------------')
        # print(ci, cj, blown)
        # for line in board:
        #     print(line)

    # 위쪽 이동
    di, dj = directions[3]
    for _ in range(c + 1 << 1):
        ci += di
        cj += dj
        blown += tornado(ci, cj, 3)
        # print('--------------')
        # print(ci, cj, blown)
        # for line in board:
        #     print(line)

# 라스트 왼쪽 이동
di, dj = directions[0]
for _ in range(n - 1):
    ci += di
    cj += dj
    blown += tornado(ci, cj, 0)
    # print('--------------')
    # print(ci, cj, blown)
    # for line in board:
    #     print(line)

print(blown)
