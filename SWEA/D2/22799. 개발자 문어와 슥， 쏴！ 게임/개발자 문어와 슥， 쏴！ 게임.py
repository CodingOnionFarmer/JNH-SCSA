directions = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상 하 좌 우


def find_treasure():
    for x, line in enumerate(board):
        for y, block in enumerate(line):
            if block == 2:
                return x, y


# 움직이면 True 아니면 False
def sc(p):
    cx = px[p]
    cy = py[p]
    visited = [[False] * n for _ in range(m)]
    visited[cx][cy] = True
    q = []
    for direction, (dx, dy) in enumerate(directions):
        nx, ny = cx + dx, cy + dy
        if nx == tx and ny == ty:
            got_treasure.append(p)
            gone.append(p)
            px[p] = 100
            return True
        if board[nx][ny] == 1:
            continue
        q.append((direction, nx, ny))
        visited[nx][ny] = True
    while q:
        nq = []
        for cd, cx, cy in q:
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if nx == tx and ny == ty:
                    first_dx, first_dy = directions[cd]
                    px[p] += first_dx
                    py[p] += first_dy
                    return True
                if board[nx][ny] == 1 or visited[nx][ny]:
                    continue
                nq.append((cd, nx, ny))
                visited[nx][ny] = True
        q = nq
    return False


def sa(p):
    x, y = px[p], py[p]
    can_shoot = []  # 보물과 맨하탄 거리(음수로), 좌표(행,열)
    for other_p in players:
        if other_p == p:
            continue
        ox, oy = px[other_p], py[other_p]
        if oy == y:
            if ox == x:
                continue
            if abs(x - ox) <= br:
                if not any(board[check_x][y]==1 for check_x in range(min(x, ox), max(x, ox))):
                    can_shoot.append((-abs(ox - tx) - abs(oy - ty), ox, oy))
        if ox == x:
            if abs(y - oy) <= br:
                if not any(board[x][check_y]==1 for check_y in range(min(y, oy), max(y, oy))):
                    can_shoot.append((-abs(ox - tx) - abs(oy - ty), ox, oy))
    if can_shoot:
        dist, bx, by = max(can_shoot)
        board[bx][by] = 1
        temp_wall.append([bx, by, p, d])
        pb[p] -= 1
        for other_p in players:
            ox, oy = px[other_p], py[other_p]
            if ox == bx and oy == by:
                gone.append(other_p)
                px[other_p] = 100
    return


def boom(p):
    gone_wall = []
    for tw_idx, (bx, by, bp, bd) in enumerate(temp_wall):
        if bp == p:
            continue
        bd -= 1
        if not bd:
            gone_wall.append(tw_idx)
            board[bx][by] = 0
            continue
        temp_wall[tw_idx][3] -= 1
    for gw_idx in reversed(gone_wall):
        temp_wall.pop(gw_idx)
    return


def rotate():
    for dx in range(half + 1):
        for dy in range(1, half + 1):
            board[tx + dx][ty + dy], board[tx + dy][ty - dx], board[tx - dx][ty - dy], board[tx - dy][ty + dx] = \
                board[tx - dy][ty + dx], board[tx + dx][ty + dy], board[tx + dy][ty - dx], board[tx - dx][ty - dy]
    for tw_idx, (bx, by, bp, bd) in enumerate(temp_wall):
        if abs(bx - tx) <= half and abs(by - ty) <= half:
            rx, ry = rotate_board[bx][by]
            temp_wall[tw_idx][0], temp_wall[tw_idx][1] = rx, ry
    for p in players:
        cx, cy = px[p], py[p]
        if abs(cx - tx) <= half and abs(cy - ty) <= half:
            rx, ry = rotate_board[cx][cy]
            px[p] = rx
            py[p] = ry


T = int(input())
for tc in range(1, T + 1):
    m, n = map(int, input().split())
    # k 사람수, br 폭 사거리, d 임시벽 수명, r 보물 중심 회전
    k, br, d, r = map(int, input().split())
    players = [1 + i for i in range(k)]
    board = [list(map(int, input().split())) + [1] for _ in range(m)] + [[1] * n]
    tx, ty = find_treasure()
    rotate_board = [[(0, 0)] * n for _ in range(m)]
    half = r >> 1
    for x in range(-half, half + 1):
        for y in range(-half, half + 1):
            rotate_board[tx + x][ty + y] = (tx + y, ty - x)
    px = [0]
    py = [0]
    pb = [0]
    for _ in range(k):
        x, y, b = map(int, input().split())
        px.append(x - 1)
        py.append(y - 1)
        pb.append(b)

    got_treasure = []
    ended_turn = 0
    temp_wall = []
    for turn in range(1, 1001):
        gone = []
        anyone_moved = False
        for player in players:
            if px[player] == 100:
                continue
            moved = sc(player)
            anyone_moved |= moved
            if px[player] == 100:
                continue
            if pb[player] and moved:
                sa(player)
            boom(player)
        rotate()
        for out_player in gone:
            players.remove(out_player)
        if not players or not anyone_moved:
            ended_turn = turn
            break

    if not got_treasure or not ended_turn:
        print(f'#{tc} -1')
        continue
    print(f'#{tc} {got_treasure[0]} {len(got_treasure)} {ended_turn}')
