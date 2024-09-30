directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def dfs(depth, arr, hoc):  # height of column
    global left
    if all(not height for height in hoc):
        left = 0
        return
    if depth == n:
        left = min(left, sum(hoc))
        return
    for c in range(w):
        if not left:
            return
        if not hoc[c]:
            continue
        r = h - hoc[c]
        if arr[r][c] == 1:
            n_hoc = hoc[:]
            n_hoc[c] -= 1
            # temp = [line[:] for line in arr]
            # temp[r][c] = 0
            dfs(depth + 1, arr, n_hoc)
            continue
        n_hoc = [0] * w
        temp = [[0] * w for _ in range(h)]
        temp[r][c] = 1
        q = [(r, c, arr[r][c] - 1)]
        while q:
            nq = []
            for cr, cc, ce in q:  # current explode
                for nr in range(max(h - hoc[cc], cr - ce), min(h, cr + ce + 1)):
                    if not temp[nr][cc]:
                        temp[nr][cc] = 1
                        if arr[nr][cc] != 1:
                            nq.append((nr, cc, arr[nr][cc] - 1))
                for nc in range(max(0, cc - ce), min(w, cc + ce + 1)):
                    if not temp[cr][nc]:
                        temp[cr][nc] = 1
                        if arr[cr][nc] != 1:
                            nq.append((cr, nc, arr[cr][nc] - 1))
            q = nq
        for j in range(w):
            bottom = h - 1
            for i in range(h - 1, h - 1 - hoc[j], -1):
                if temp[i][j]:
                    temp[i][j] = 0
                    continue
                temp[bottom][j] = arr[i][j]
                bottom -= 1
            n_hoc[j] = h - 1 - bottom
        dfs(depth + 1, temp, n_hoc)


T = int(input())
for tc in range(1, T + 1):
    n, w, h = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(h)]
    oob = [[False] * w + [True] for _ in range(h)] + [[True] * w]
    heights = [0] * w
    for j in range(w):
        for i in range(h):
            if board[i][j]:
                heights[j] = h - i
                break
    left = h * w
    if sum(heights) <= n:
        print(f'#{tc}', 0)
    else:
        dfs(0, board, heights)
        print(f'#{tc}', left)
