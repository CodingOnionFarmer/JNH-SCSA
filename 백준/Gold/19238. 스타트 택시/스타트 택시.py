"""
BOJ : 스타트 택시

시작 시간 : 10시 01분
구상 완료 : 10시 07분
제출 시간 : 10시 38분
"""


# 400짜리 bfs 800번 해도 충분

def int_idx(num):
    return int(num) - 1


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m, f = map(int, input().split())
board = [list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * n]
adj = [[[(i + di, j + dj) for di, dj in directions if not board[i + di][j + dj]] for j in range(n)] for i in range(n)]
csx, csy = map(int_idx, input().split())
start_site = [[None] * n for _ in range(n)]

for p in range(m):
    sx, sy, gx, gy = map(int_idx, input().split())
    start_site[sx][sy] = (gx, gy)


def solve():
    fuel = f
    cx, cy = csx, csy

    for move in range(m):
        visited = [[False] * n for _ in range(n)]
        q = [(cx, cy)]
        visited[cx][cy] = True
        while q and fuel:
            nq = []
            sq = []
            for x, y in q:
                if start_site[x][y]:
                    sq.append((x, y))
                for nx, ny in adj[x][y]:
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        nq.append((nx, ny))
            if sq:
                break
            fuel -= 1
            q = nq

        if not sq:
            print(-1)
            return

        cx, cy = min(sq)
        dx, dy = start_site[cx][cy]
        start_site[cx][cy] = None
        visited = [[False] * n for _ in range(n)]
        q = [(cx, cy)]
        visited[cx][cy] = True
        distance = 0
        arrived = False
        while q and fuel:
            nq = []
            fuel -= 1
            distance += 1
            for x, y in q:
                for nx, ny in adj[x][y]:
                    if nx == dx and ny == dy:
                        cx, cy = nx, ny
                        arrived = True
                        break
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        nq.append((nx, ny))
                if arrived:
                    break
            if arrived:
                break
            q = nq

        if not arrived:
            print(-1)
            return
        fuel += distance << 1

    print(fuel)
    return


solve()
