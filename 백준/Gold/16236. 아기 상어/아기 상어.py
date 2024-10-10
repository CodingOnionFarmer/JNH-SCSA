directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n = int(input())
board = [list(map(int, input().split())) + [100] for _ in range(n)] + [[100] * n]
level = 2
exp = 0
time = 0
ci, cj = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            ci, cj = i, j

while True:
    step = 0
    can_kill = []
    visited = [[False] * n for _ in range(n)]
    q = [(ci, cj)]
    visited[ci][cj] = True
    while q and not can_kill:
        step += 1
        nq = []
        for i, j in q:
            for di, dj in directions:
                ni, nj = i + di, j + dj
                num = board[ni][nj]
                if num > level:
                    continue
                elif not visited[ni][nj]:
                    visited[ni][nj] = True
                    if num == level or not num:
                        nq.append((ni, nj))
                    else:
                        can_kill.append((ni, nj))
        q = nq
    if can_kill:
        time += step
        ci, cj = min(can_kill)
        board[ci][cj] = 0
        exp += 1
        if exp == level:
            exp = 0
            level += 1
    else:
        break

print(time)