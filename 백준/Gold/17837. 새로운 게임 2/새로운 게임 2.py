"""
BOJ : 새로운 게임 2

시작 시간 : 2시 51분
구상 완료 : 2시 58분
제출 시간 : 3시 49분
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 오른 밑 왼 위
d_change = (0, 0, 2, 3, 1)  # 1->0 오른, 2->2 왼, 3->3 위, 4->1 밑

n, k = map(int, input().split())
color = [list(map(int, input().split())) + [2] for _ in range(n)] + [[2] * n]
board = [[[] for __ in range(n)] for _ in range(n)]
units = []
for i in range(k):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d = d_change[d]
    board[r][c].append(i)
    units.append([r, c, d])


# for line in board:
#     print(line)
#
# for line in color:
#     print(line)
#
# print(units)


def solve():
    for turn in range(1, 1002):
        for unit in range(k):
            ur, uc, ud = units[unit]
            idx = board[ur][uc].index(unit)

            unit_stacked = board[ur][uc][idx:]

            dr, dc = directions[ud]
            nr, nc = ur + dr, uc + dc
            # if turn == 2 and unit == 3:
            #     print(unit_stacked)
            #     print(ur,uc)
            #     print(dr,dc)
            #     print(nr,nc)
            #     print(color[nr][nc])
            if not color[nr][nc]:
                board[nr][nc].extend(unit_stacked)
                if len(board[nr][nc]) > 3:
                    print(turn)
                    return
                for u in unit_stacked:
                    units[u][0] = nr
                    units[u][1] = nc
                board[ur][uc] = board[ur][uc][:idx]
            elif color[nr][nc] == 1:
                board[nr][nc].extend(list(reversed(unit_stacked)))
                if len(board[nr][nc]) > 3:
                    print(turn)
                    return
                for u in unit_stacked:
                    units[u][0] = nr
                    units[u][1] = nc
                board[ur][uc] = board[ur][uc][:idx]
            else:
                units[unit][2] = (units[unit][2] + 2) % 4
                ud = units[unit][2]
                dr, dc = directions[ud]
                nr, nc = ur + dr, uc + dc
                if not color[nr][nc]:
                    board[nr][nc].extend(unit_stacked)
                    if len(board[nr][nc]) > 3:
                        print(turn)
                        return
                    for u in unit_stacked:
                        units[u][0] = nr
                        units[u][1] = nc
                    board[ur][uc] = board[ur][uc][:idx]
                elif color[nr][nc] == 1:
                    board[nr][nc].extend(list(reversed(unit_stacked)))
                    if len(board[nr][nc]) > 3:
                        print(turn)
                        return
                    for u in unit_stacked:
                        units[u][0] = nr
                        units[u][1] = nc
                    board[ur][uc] = board[ur][uc][:idx]

            # print('=========================')
            # print(turn, '턴', unit, '번 기물')
            # for line in board:
            #     print(line)

        # if any(len(board[i][j]) > 3 for i in range(4) for j in range(4)):
        #     print(turn)
        #     return

    print(-1)
    return


solve()
