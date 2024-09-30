# ㄱ

directions = ((0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, -1), (0, -1, 0), (-1, 0, 0))

boards = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
adj = [[[[(i + di, j + dj, k + dk) for di, dj, dk in directions if
          0 <= i + di < 5 and 0 <= j + dj < 5 and 0 <= k + dk < 5] for k in range(5)] for j in range(5)] for i in
       range(5)]

boards_rotated = []
for idx, board in enumerate(boards):
    cw_90 = list(zip(*board[::-1]))
    ccw_90 = list(zip(*board))[::-1]
    rotated_180 = [row[::-1] for row in board[::-1]]
    boards_rotated.append([board, cw_90, ccw_90, rotated_180])


def solve():
    least = 125
    temp = []
    for i1 in range(5):
        for board1 in boards_rotated[i1]:
            if not board1[0][0]:
                continue
            temp.append(board1)
            for i2 in {0, 1, 2, 3, 4} - {i1}:
                for board2 in boards_rotated[i2]:
                    temp.append(board2)
                    for i3 in {0, 1, 2, 3, 4} - {i1, i2}:
                        for board3 in boards_rotated[i3]:
                            temp.append(board3)
                            for i4 in {0, 1, 2, 3, 4} - {i1, i2, i3}:
                                for board4 in boards_rotated[i4]:
                                    temp.append(board4)
                                    for i5 in {0, 1, 2, 3, 4} - {i1, i2, i3, i4}:
                                        for board5 in boards_rotated[i5]:
                                            if not board5[4][4]:
                                                continue
                                            temp.append(board5)
                                            visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
                                            visited[0][0][0] = True
                                            step = 0
                                            q = [(0, 0, 0)]
                                            while q and not visited[4][4][4]:
                                                step += 1
                                                if step == least:
                                                    break
                                                nq = []
                                                for i, j, k in q:
                                                    for ni, nj, nk in adj[i][j][k]:
                                                        if temp[ni][nj][nk] and not visited[ni][nj][nk]:
                                                            visited[ni][nj][nk] = True
                                                            nq.append((ni, nj, nk))
                                                q = nq

                                            if visited[4][4][4]:
                                                if step < least:
                                                    least = step
                                                    if least == 12:
                                                        print(12)
                                                        return

                                            temp.pop()
                                    temp.pop()
                            temp.pop()
                    temp.pop()
            temp.pop()

    if least == 125:
        least = -1
    print(least)
    return


solve()
