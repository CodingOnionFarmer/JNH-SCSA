directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
adj = [[[(i + di, j + dj) for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n] for j in range(n)] for i in
       range(n)]


def find():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                return i, j


def bfs(ci, cj, level):
    step = 0
    can_kill = []
    visited = [[False] * n for _ in range(n)]
    q = [(ci, cj)]
    visited[ci][cj] = True
    while q and not can_kill:
        step += 1
        nq = []
        for i, j in q:
            for ni, nj in adj[i][j]:
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
        return step, *min(can_kill)
    return 0, 0, 0


def solve():
    level = 2
    exp = 0
    time = 0
    ci, cj = find()
    while True:
        distance, ci, cj = bfs(ci, cj, level)
        if distance:
            time += distance
            board[ci][cj] = 0
            exp += 1
            if exp == level:
                exp = 0
                level += 1
        else:
            print(time)
            return


solve()
