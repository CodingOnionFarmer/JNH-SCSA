directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
pool = [list(map(int, list(input()))) + [0] for _ in range(n)] + [[0] * m]
ans = 0
for h in range(2, 10):
    visited = [[False] * m for _ in range(n)]
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if pool[i][j] < h and not visited[i][j]:
                visited[i][j] = True
                area = 1
                q = [(i, j)]
                spill = False
                while q:
                    nq = []
                    for ci, cj in q:
                        for di, dj in directions:
                            ni, nj = ci + di, cj + dj
                            if not pool[ni][nj]:
                                spill = True
                                continue
                            if pool[ni][nj] < h and not visited[ni][nj]:
                                nq.append((ni, nj))
                                visited[ni][nj] = True
                                area += 1
                    q = nq
                if not spill:
                    ans += area
print(ans)
