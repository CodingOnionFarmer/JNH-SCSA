# 언어 : PyPy3
# 메모리 : 51792KB
# 실행시간 : 194ms
# 시도횟수 : 1회

# BFS, 시뮬레이션, 구현

# 룩업 테이블을 만들어두고 두 칸에 파이프가 있고 서로 연결되어있는지 판정했다.


directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상
pipes = ((), (0, 1, 2, 3), (1, 3), (0, 2), (0, 3), (0, 1), (1, 2), (2, 3))
can_move_from_direction = [{1, 3, 6, 7}, {1, 2, 4, 7}, {1, 3, 4, 5}, {1, 2, 5, 6}]

T = int(input())
for tc in range(1, T + 1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * m]
    now = {r * m + c}
    ans = 0
    while now and l:  # 시간이 다 되거나 더 갈 곳이 없을 때까지
        move = set()
        for position in now:
            ci, cj = position // m, position % m
            p = tunnel[ci][cj]
            tunnel[ci][cj] = 0
            ans += 1
            for d in pipes[p]:
                di, dj = directions[d]
                ni, nj = ci + di, cj + dj
                if tunnel[ni][nj] in can_move_from_direction[d]:
                    move.add(ni * m + nj)
        now = move
        l -= 1
    print(f'#{tc} {ans}')
