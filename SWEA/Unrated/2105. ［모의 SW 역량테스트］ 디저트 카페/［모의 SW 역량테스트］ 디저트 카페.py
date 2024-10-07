"""
24.10.7 (월)

SWEA : 디저트 카페

특이 사항 : 작년에 풀어봄

1회차?(현재)
목표 풀이 시간 : 30분 이내

시작 시간 : 2시 02분
구상 완료 : 2시 05분
제출 완료 : 2시 34분
"""

# DFS

directions = ((1, 1), (1, -1), (-1, -1), (-1, 1))  # 위 꼭짓점 출발 -> 우하향 시작 시계방향
cw = (1, 2, 3, 0)


def dfs(moved, x, y, d, d_moved):
    # print(moved, x, y, d, d_moved)
    # print(ate[:10])
    global most_eat
    dx, dy = directions[d]
    nx, ny = x + dx, y + dy
    if d == 3:
        if nx == sx and ny == sy:
            if moved >= most_eat:
                most_eat = moved + 1
            return
        dessert = desserts[nx][ny]
        if not ate[dessert]:
            ate[dessert] = True
            dfs(moved + 1, nx, ny, 3, 0)
            ate[dessert] = False
        return

    if itb[nx][ny]:
        dessert = desserts[nx][ny]
        if not ate[dessert]:
            ate[dessert] = True
            dfs(moved + 1, nx, ny, d, d_moved + 1)
            ate[dessert] = False

    if d == 1 and moved << 1 <= most_eat:
        return

    if d < 2 and d_moved:
        nd = cw[d]
        dx, dy = directions[nd]
        nx, ny = x + dx, y + dy
        if itb[nx][ny]:
            dessert = desserts[nx][ny]
            if not ate[dessert]:
                ate[dessert] = True
                dfs(moved + 1, nx, ny, nd, 1)
                ate[dessert] = False
    elif d == 2 and x - sx == sy - y:
        nx, ny = x - 1, y + 1
        if nx == sx and ny == sy:
            if moved >= most_eat:
                most_eat = moved + 1
            return
        dessert = desserts[nx][ny]
        if itb[nx][ny]:
            if not ate[dessert]:
                ate[dessert] = True
                dfs(moved + 1, nx, ny, 3, 1)
                ate[dessert] = False


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    desserts = [list(map(int, input().split())) for _ in range(n)]
    itb = [[True] * n + [False] for _ in range(n)] + [[False] * (n + 1)]  # in the bound
    ate = [False] * 101
    most_eat = -1
    for sx in range(n - 2):
        for sy in range(1, n - 1):
            ate[desserts[sx][sy]] = True
            dfs(0, sx, sy, 0, 0)
            ate[desserts[sx][sy]] = False
    print(f'#{tc}', most_eat)
