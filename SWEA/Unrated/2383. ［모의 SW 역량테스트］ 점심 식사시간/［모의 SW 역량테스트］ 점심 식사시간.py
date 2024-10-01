rotate_3 = (1, 2, 0)


def dfs(depth, ps1, ps2):
    global shortest
    if depth == p:
        if not ps1:
            time1 = 0
        elif len(ps1) <= 3:
            time1 = max(ps1) + s1
        else:
            ps1.sort()
            when_down1 = [s1 + t for t in ps1[:3]]
            sd1 = 2
            for t in ps1[3:]:
                sd1 = rotate_3[sd1]
                when_down1[sd1] = max(t, when_down1[sd1]) + s1
            time1 = when_down1[sd1]
        if time1 >= shortest:
            return

        if not ps2:
            time2 = 0
        elif len(ps2) <= 3:
            time2 = max(ps2) + s2
        else:
            ps2.sort()
            when_down2 = [s2 + t for t in ps2[:3]]
            sd2 = 2
            for t in ps2[3:]:
                sd2 = rotate_3[sd2]
                when_down2[sd2] = max(t, when_down2[sd2]) + s2
            time2 = when_down2[sd2]
        if time2 >= shortest:
            return

        shortest = max(time1, time2)
        return

    if pd1[depth] + s1 < shortest:
        dfs(depth + 1, ps1 + [pd1[depth]], ps2)
    if pd2[depth] + s2 < shortest:
        dfs(depth + 1, ps1, ps2 + [pd2[depth]])
    return


T = int(input())
s1x = s1y = s2x = s2y = 0
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    person_pos = []
    s1 = s2 = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                if board[i][j] == 1:
                    person_pos.append((i, j))
                else:
                    if s1:
                        s2x, s2y = i, j
                        s2 = board[i][j]
                    else:
                        s1x, s1y = i, j
                        s1 = board[i][j]
    p = len(person_pos)
    pd1 = [abs(px - s1x) + abs(py - s1y) for px, py in person_pos]
    pd2 = [abs(px - s2x) + abs(py - s2y) for px, py in person_pos]
    shortest = 10000
    dfs(0, [], [])
    print(f'#{tc}', shortest + 1)
