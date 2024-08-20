directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상
pipes = (
    (), (True, True, True, True), (False, True, False, True), (True, False, True, False), (True, False, False, True),
    (True, True, False, False), (False, True, True, False), (False, False, True, True))

T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * m]
    now = {r * m + c}
    ans = 0
    while now and l:
        move = set()
        for position in now:
            ci, cj = position // m, position % m
            p = tunnel[ci][cj]
            tunnel[ci][cj] = 0
            ans += 1
            for d in range(4):  # 우0 하1 좌2 상3, d의 반대방향은 (d+2)%4이다.
                if pipes[p][d]:
                    di, dj = directions[d]
                    ni, nj = ci + di, cj + dj
                    np = tunnel[ni][nj]
                    if np and pipes[np][(d + 2) % 4]:
                        move.add(ni * m + nj)
        now = move
        l -= 1
    print(f'#{tc} {ans}')
