# BFS


INF = 90001
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[INF] * n for _ in range(n)]
    q = [(0, 0, 0)]
    visited[0][0] = 0
    while q:
        nq = []
        for ci, cj, ct in q:
            if ct > visited[ci][cj]:
                continue
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < n and 0 <= nj < n:
                    nt = ct + board[ni][nj]
                    if nt < visited[ni][nj]:
                        visited[ni][nj] = nt
                        nq.append((ni, nj, nt))
        q = nq
    print(f'#{tc} {visited[n - 1][n - 1]}')
