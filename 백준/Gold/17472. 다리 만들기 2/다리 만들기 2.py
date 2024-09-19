directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
oob = [[False] * m + [True] for _ in range(n)] + [[True] * m]
visited = [[0] * m for _ in range(n)]
island = 0
distance = [[]]
for i in range(n):
    for j in range(m):
        if board[i][j] and not visited[i][j]:
            island += 1
            visited[i][j] = island
            distance.append([100] * island)
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if oob[ni][nj]:
                            continue
                        if board[ni][nj]:
                            if not visited[ni][nj]:
                                visited[ni][nj] = island
                                nq.append((ni, nj))
                        else:
                            dist = 1
                            while True:
                                ni += di
                                nj += dj
                                if oob[ni][nj]:
                                    break
                                if board[ni][nj]:
                                    nv = visited[ni][nj]
                                    if nv and nv != island:
                                        if 1 < dist < distance[island][nv]:
                                            distance[island][nv] = dist
                                    break
                                dist += 1
                q = nq

head = [i for i in range(island + 1)]


def union(a, b):
    ha = find(a)
    hb = find(b)
    head[hb] = ha


def find(a):
    ha = head[a]
    if a == ha:
        return a
    head[a] = find(ha)
    return head[a]


bridges = []
for i in range(2, island + 1):
    for j in range(1, i):
        if distance[i][j] != 100:
            bridges.append((distance[i][j], i, j))
bridges.sort()
connected = 0
total_length = 0
for d, i, j in bridges:
    if find(i) != find(j):
        total_length += d
        union(i, j)
        connected += 1
if connected < island - 1:
    total_length = -1

print(total_length)
