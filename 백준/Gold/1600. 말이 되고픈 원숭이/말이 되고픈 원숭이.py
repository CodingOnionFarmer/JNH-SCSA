k = int(input())
w, h = map(int, input().split())
trip = [list(map(int, input().split())) + [1, 1] for _ in range(h)] + [[1] * (w + 2) for _ in range(2)]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
knight_directions = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
visited = [[[False] * (k + 1) for __ in range(w)] for _ in range(h)]
visited[0][0][0] = True
q = [(0, 0, 0)]  # 찬스 쓴 개수, 행위치, 열위치
chance = k
step = 0
while q and not any(visited[h - 1][w - 1][i] for i in range(k + 1)):
    step += 1
    nq = []
    for used, ci, cj in q:
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if trip[ni][nj] or visited[ni][nj][used]:
                continue
            visited[ni][nj][used] = True
            nq.append((used, ni, nj))
        if used < k:
            for di, dj in knight_directions:
                ni, nj = ci + di, cj + dj
                if trip[ni][nj] or visited[ni][nj][used + 1]:
                    continue
                visited[ni][nj][used + 1] = True
                nq.append((used + 1, ni, nj))
    q = nq
if any(visited[h - 1][w - 1][i] for i in range(k + 1)):
    print(step)
else:
    print(-1)
