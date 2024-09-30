import os, io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
lightened = [[False] * (n + 2) for _ in range(n + 2)]
lightened[1][1] = True
light_switches = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    x, y, a, b = map(int, input().split())
    light_switches[x][y].append((a, b))
visited = [[False] * (n + 2) for _ in range(n + 2)]
visited[1][1] = True
ans = 1
q = [(1, 1)]
while q:
    nq = []
    for x, y in q:
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if lightened[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                nq.append((nx, ny))
        for a, b in light_switches[x][y]:
            if not lightened[a][b]:
                lightened[a][b] = True
                ans += 1
                for da, db in directions:
                    if visited[a + da][b + db]:
                        visited[a][b] = True
                        nq.append((a, b))
                        break
    q = nq
print(ans)
