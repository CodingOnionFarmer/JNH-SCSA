n, m = map(int, input().split())
maze = [list(input()) + ['#'] for _ in range(n)] + [['#'] * m]
door_key = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32}
door = {'A': 1, 'B': 2, 'C': 4, 'D': 8, 'E': 16, 'F': 32}
visited = [[[False] * 64 for _ in range(m)] for _ in range(n)]

si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if maze[i][j] == '0':
            maze[i][j] = '.'
            si, sj = i, j

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))


def solve():
    q = [(si, sj, 0)]
    visited[si][sj][0] = True
    step = 0
    while q:
        nq = []
        step += 1
        for ci, cj, ck in q:
            for di, dj in directions:
                ni, nj = ci + di, cj + dj
                block = maze[ni][nj]
                if block == '#':
                    continue
                if block == '1':
                    print(step)
                    return
                if block == '.':
                    if visited[ni][nj][ck]:
                        continue
                    visited[ni][nj][ck] = True
                    nq.append((ni, nj, ck))
                elif block in door_key:
                    nk = ck | door_key[block]
                    if visited[ni][nj][nk]:
                        continue
                    visited[ni][nj][nk] = True
                    nq.append((ni, nj, nk))
                else:
                    if door[block] & ck and not visited[ni][nj][ck]:
                        visited[ni][nj][ck] = True
                        nq.append((ni, nj, ck))
        q = nq
    print(-1)
    return


solve()
