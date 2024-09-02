# 구현, 시뮬레이션

directions = ((0, 0), (0, -1), (1, 0), (0, 1), (-1, 0))

T = int(input())
for tc in range(1, T + 1):
    m, a = map(int, input().split())
    a_path = list(map(int, input().split()))
    b_path = list(map(int, input().split()))
    board = [[[] for _ in range(10)] for _ in range(10)]
    chargers = sorted([tuple(map(int, input().split())) for _ in range(a)], key=lambda ch: ch[3], reverse=True)
    for idx, (x, y, c, p) in enumerate(chargers):
        for i in range(max(0, x - 1 - c), min(10, x + c)):
            x_dist = abs(x - 1 - i)
            for j in range(max(0, y - 1 - c + x_dist), min(10, y + c - x_dist)):
                board[i][j].append((idx, p))
    ax, ay = 0, 0
    bx, by = 9, 9
    ans = 0
    if board[ax][ay]:
        a_first = board[ax][ay][0]
        ans += a_first[1]
        if len(board[ax][ay]) == 1:
            if board[bx][by]:
                b_first = board[bx][by][0]
                if a_first[0] != b_first[0]:
                    ans += b_first[1]
                else:
                    if len(board[bx][by]) > 1:
                        ans += board[bx][by][1][1]
        else:
            if board[bx][by]:
                b_first = board[bx][by][0]
                if a_first[0] != b_first[0]:
                    ans += b_first[1]
                else:
                    if len(board[bx][by]) == 1:
                        ans += board[ax][ay][1][1]
                    else:
                        ans += max(board[ax][ay][1][1], board[bx][by][1][1])
    elif board[bx][by]:
        ans += board[bx][by][0][1]

    for i in range(m):
        adx, ady = directions[a_path[i]]
        bdx, bdy = directions[b_path[i]]
        ax += adx
        ay += ady
        bx += bdx
        by += bdy
        if board[ax][ay]:
            a_first = board[ax][ay][0]
            ans += a_first[1]
            if len(board[ax][ay]) == 1:
                if board[bx][by]:
                    b_first = board[bx][by][0]
                    if a_first[0] != b_first[0]:
                        ans += b_first[1]
                    else:
                        if len(board[bx][by]) > 1:
                            ans += board[bx][by][1][1]
            else:
                if board[bx][by]:
                    b_first = board[bx][by][0]
                    if a_first[0] != b_first[0]:
                        ans += b_first[1]
                    else:
                        if len(board[bx][by]) == 1:
                            ans += board[ax][ay][1][1]
                        else:
                            ans += max(board[ax][ay][1][1], board[bx][by][1][1])

        elif board[bx][by]:
            ans += board[bx][by][0][1]

    print(f'#{tc}', ans)
