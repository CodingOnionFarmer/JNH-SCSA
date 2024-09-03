directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def bfs():
    q = []
    fq = []
    for i in range(h):
        for j in range(w):
            if board[i][j] == '@':
                q.append((i, j))
                board[i][j] = None
            elif board[i][j] == '*':
                fq.append((i, j))
                board[i][j] = None

    time = 0
    while q:
        time += 1
        nq = []
        nfq = []
        for fi, fj in fq:
            for di, dj in directions:
                ni, nj = fi + di, fj + dj
                if 0 <= ni < h and 0 <= nj < w and board[ni][nj] == '.':
                    board[ni][nj] = None
                    nfq.append((ni, nj))
        for si, sj in q:
            for di, dj in directions:
                ni, nj = si + di, sj + dj
                if ni < 0 or nj < 0 or ni >= h or nj >= w:
                    print(time)
                    return
                elif board[ni][nj] == '.':
                    board[ni][nj] = None
                    nq.append((ni, nj))
        q = nq
        fq = nfq

    print('IMPOSSIBLE')
    return


T = int(input())
for tc in range(T):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    bfs()
