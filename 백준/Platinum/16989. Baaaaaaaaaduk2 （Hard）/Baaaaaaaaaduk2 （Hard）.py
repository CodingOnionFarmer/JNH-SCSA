# BFS
# Greedy, 많은 조건 분기

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
oob = [[False] * m + [True] for _ in range(n)] + [[True] * m]
can_kill_with_one_stone = [[0] * m for _ in range(n)]
can_kill_with_two_stones = []

group_num = 3
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            size = 1
            board[i][j] = group_num
            hwalo = []
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if oob[ni][nj] or board[ni][nj] == group_num or board[ni][nj] == 1:
                            continue
                        if board[ni][nj] == 2:
                            size += 1
                            board[ni][nj] = group_num
                            nq.append((ni, nj))
                            continue
                        board[ni][nj] = group_num
                        hwalo.append((ni, nj))
                q = nq
            if len(hwalo) == 1:
                x, y = hwalo[0]
                can_kill_with_one_stone[x][y] += size
            elif len(hwalo) == 2:
                hwalo.sort()
                can_kill_with_two_stones.append([size, *hwalo[0], *hwalo[1]])
            group_num += 1

first = second = 0
for line in can_kill_with_one_stone:
    # print(*line)
    for kill in line:
        if kill >= first:
            first, second = kill, first
        elif kill > second:
            second = kill

group_kill_with_two_stones = {-1: 0}
for size, sx1, sy1, sx2, sy2 in can_kill_with_two_stones:
    two_stones_num = sx1 * 8000 + sy1 * 400 + sx2 * 20 + sy2
    kill = size + can_kill_with_one_stone[sx1][sy1] + can_kill_with_one_stone[sx2][sy2]
    if two_stones_num in group_kill_with_two_stones:
        group_kill_with_two_stones[two_stones_num] += kill
    else:
        group_kill_with_two_stones[two_stones_num] = kill
print(max(max(group_kill_with_two_stones.values()), first + second))
