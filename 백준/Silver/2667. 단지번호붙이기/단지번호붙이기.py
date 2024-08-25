# bfs(또는 dfs)

n = int(input())
houses = [list(input()) + ['0'] for _ in range(n)] + [['0'] * n]
danji = []
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
for i in range(n):
    for j in range(n):
        if houses[i][j] == '1':
            count = 1
            houses[i][j] = None
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if houses[ni][nj] == '1':
                            count += 1
                            houses[ni][nj] = None
                            nq.append((ni, nj))
                q = nq
            danji.append(count)
danji.sort()
print(len(danji))
for cnt in danji:
    print(cnt)
