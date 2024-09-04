"""
BOJ : 구슬 탈출 2

시작 시간 : 3시 00분
구상 완료 : 3시 08분
제출 시간 : 3시 37분
"""

# 우 하 좌 상
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for __ in range(m)] for ___ in range(n)]
ri, rj, bi, bj, gi, gj = 0, 0, 0, 0, 0, 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j
        elif board[i][j] == 'O':
            gi, gj = i, j


def move(d, cri, crj, cbi, cbj):
    di, dj = directions[d]
    while True:
        nri, nrj = cri + di, crj + dj
        if nri == gi and nrj == gj:
            return True, 0, 0
        if board[nri][nrj] == '#' or (nri == cbi and nrj == cbj):
            return False, cri, crj
        cri, crj = nri, nrj


visited[ri][rj][bi][bj] = True


def solve():
    q = [(ri, rj, bi, bj, -1)]
    step = 0
    nq = []
    step += 1
    for rx, ry, bx, by, d in q:
        if ry >= by:
            # 오른쪽 기울이기
            red_goal_in, nrx, nry = move(0, rx, ry, bx, by)
            blue_goal_in, nbx, nby = move(0, bx, by, nrx, nry)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 0))

            # 왼쪽 기울이기
            blue_goal_in, nbx, nby = move(2, bx, by, rx, ry)
            red_goal_in, nrx, nry = move(2, rx, ry, nbx, nby)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 2))

        else:
            # 오른쪽 기울이기
            blue_goal_in, nbx, nby = move(0, bx, by, rx, ry)
            red_goal_in, nrx, nry = move(0, rx, ry, nbx, nby)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 0))

            # 왼쪽 기울이기
            red_goal_in, nrx, nry = move(2, rx, ry, bx, by)
            blue_goal_in, nbx, nby = move(2, bx, by, nrx, nry)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 2))

        if rx >= bx:
            # 아래쪽 기울이기
            red_goal_in, nrx, nry = move(1, rx, ry, bx, by)
            blue_goal_in, nbx, nby = move(1, bx, by, nrx, nry)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 1))

            # 위쪽 기울이기
            blue_goal_in, nbx, nby = move(3, bx, by, rx, ry)
            red_goal_in, nrx, nry = move(3, rx, ry, nbx, nby)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 3))

        else:
            # 아래쪽 기울이기
            blue_goal_in, nbx, nby = move(1, bx, by, rx, ry)
            red_goal_in, nrx, nry = move(1, rx, ry, nbx, nby)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 1))

            # 위쪽 기울이기
            red_goal_in, nrx, nry = move(3, rx, ry, bx, by)
            blue_goal_in, nbx, nby = move(3, bx, by, nrx, nry)
            if not blue_goal_in:
                if red_goal_in:
                    print(step)
                    return
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    nq.append((nrx, nry, nbx, nby, 3))
    q = nq
    while q and step < 10:
        nq = []
        step += 1
        for rx, ry, bx, by, d in q:
            if d & 1:
                if ry >= by:
                    # 오른쪽 기울이기
                    red_goal_in, nrx, nry = move(0, rx, ry, bx, by)
                    blue_goal_in, nbx, nby = move(0, bx, by, nrx, nry)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 0))

                    # 왼쪽 기울이기
                    blue_goal_in, nbx, nby = move(2, bx, by, rx, ry)
                    red_goal_in, nrx, nry = move(2, rx, ry, nbx, nby)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 2))

                else:
                    # 오른쪽 기울이기
                    blue_goal_in, nbx, nby = move(0, bx, by, rx, ry)
                    red_goal_in, nrx, nry = move(0, rx, ry, nbx, nby)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 0))

                    # 왼쪽 기울이기
                    red_goal_in, nrx, nry = move(2, rx, ry, bx, by)
                    blue_goal_in, nbx, nby = move(2, bx, by, nrx, nry)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 2))
            else:
                if rx >= bx:
                    # 아래쪽 기울이기
                    red_goal_in, nrx, nry = move(1, rx, ry, bx, by)
                    blue_goal_in, nbx, nby = move(1, bx, by, nrx, nry)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 1))

                    # 위쪽 기울이기
                    blue_goal_in, nbx, nby = move(3, bx, by, rx, ry)
                    red_goal_in, nrx, nry = move(3, rx, ry, nbx, nby)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 3))

                else:
                    # 아래쪽 기울이기
                    blue_goal_in, nbx, nby = move(1, bx, by, rx, ry)
                    red_goal_in, nrx, nry = move(1, rx, ry, nbx, nby)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 1))

                    # 위쪽 기울이기
                    red_goal_in, nrx, nry = move(3, rx, ry, bx, by)
                    blue_goal_in, nbx, nby = move(3, bx, by, nrx, nry)
                    if not blue_goal_in:
                        if red_goal_in:
                            print(step)
                            return
                        if not visited[nrx][nry][nbx][nby]:
                            visited[nrx][nry][nbx][nby] = True
                            nq.append((nrx, nry, nbx, nby, 3))
        q = nq

    print(-1)
    return


solve()
