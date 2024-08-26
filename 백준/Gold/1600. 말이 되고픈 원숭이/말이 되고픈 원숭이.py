k = int(input())
w, h = map(int, input().split())
trip = [list(map(int, input().split())) + [1, 1] for _ in range(h)] + [[1] * (w + 2) for _ in range(2)]

# 상하좌우 이동
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 나이트 이동
knight_directions = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))

# visited[i][j]는 i,j 칸에 해당 숫자만큼의 찬스를 쓰고 갈 수 있음을 의미한다
visited = [[31] * w for _ in range(h)]
visited[0][0] = 0
q = [(0, 0, 0)]  # 찬스 쓴 개수, 행위치, 열위치
step = 0
while q and visited[h - 1][w - 1] > k:
    step += 1
    nq = []
    for used, ci, cj in q:
        if visited[ci][cj] < used:
            continue
        for di, dj in directions:
            ni, nj = ci + di, cj + dj
            if trip[ni][nj] or visited[ni][nj] <= used:
                continue
            visited[ni][nj] = used
            nq.append((used, ni, nj))
        if used < k:
            for di, dj in knight_directions:
                ni, nj = ci + di, cj + dj
                if trip[ni][nj] or visited[ni][nj] <= used + 1:
                    continue
                visited[ni][nj] = used + 1
                nq.append((used + 1, ni, nj))
    q = nq
if visited[h - 1][w - 1] <= k:
    print(step)
else:
    print(-1)
