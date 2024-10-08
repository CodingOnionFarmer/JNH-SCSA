"""
어떤 양방향 루트의 양 끝은 둘 다 블랙홀이거나, 양끝이 이어진 무한루프이다.
블랙홀에서 나와서 출발하면 블랙홀으로 반드시 들어간다.
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 우 하 좌 상
opposite = (2, 3, 0, 1)
blocks = (
    (0, 1, 2, 3),
    (2, 0, 3, 1),
    (2, 3, 1, 0),
    (1, 3, 0, 2),
    (3, 2, 0, 1),
    (2, 3, 0, 1),
)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = [list(map(int, input().split())) + [5] for _ in range(n)] + [[5] * n]
    score = [[[-1] * 4 for _ in range(n)] for _ in range(n)]
    last_route_num_and_direction_of_the_block = [[0] * n for _ in range(n)]  # 비트마스킹, 4로 나눈 몫은 경로 번호, 나머지는 방향
    wormholes = {}
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 6:
                num = board[i][j]
                if num in wormholes:
                    wormholes[(i, j)] = wormholes[num]
                    wormholes[wormholes[num]] = (i, j)
                    wormholes.pop(num)
                else:
                    wormholes[num] = (i, j)

    best_score = 0
    route_num = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == -1:
                for d, (di, dj) in enumerate(directions):
                    route_num += 4
                    cx, cy, cd, dx, dy = i, j, d, di, dj
                    crashed = 0
                    route = []
                    while True:
                        cx += dx
                        cy += dy
                        num = board[cx][cy]
                        if num == -1:
                            break
                        if not num:
                            route.append((cx, cy, cd, crashed))
                        elif num <= 5:
                            crashed += 1
                            cd = blocks[num][cd]
                            dx, dy = directions[cd]
                        else:
                            cx, cy = wormholes[(cx, cy)]
                    if crashed <= best_score:
                        # 점수 볼 필요 없으므로 방문처리만 대충
                        for rx, ry, rd, rc in route:
                            score[rx][ry][rd] = 0
                    else:
                        # 점수 마킹
                        for rx, ry, rd, rc in route:
                            if last_route_num_and_direction_of_the_block[rx][ry] >> 2 == route_num:
                                bd = last_route_num_and_direction_of_the_block[rx][ry] & 3  # before direction
                                score[rx][ry][bd] -= (crashed - rc)
                            score[rx][ry][rd] = crashed - rc
                            last_route_num_and_direction_of_the_block[rx][ry] = route_num << 2 | rd
                        # 점수 체크
                        for rx, ry, rd, rc in route:
                            if score[rx][ry][rd] > best_score:
                                best_score = score[rx][ry][rd]
                                if best_score == crashed:
                                    break

    for i in range(n):
        for j in range(n):
            if not board[i][j]:
                for d, (di, dj) in enumerate(directions):
                    if score[i][j][d] >= 0:
                        continue
                    route_num += 4
                    cx, cy, cd, dx, dy = i, j, d, di, dj
                    crashed = 0
                    route = [(cx, cy, cd, 0)]
                    while True:
                        cx += dx
                        cy += dy
                        if cx == i and cy == j and cd == d:
                            break
                        num = board[cx][cy]
                        if not num:
                            route.append((cx, cy, cd, crashed))
                        elif num <= 5:
                            crashed += 1
                            cd = blocks[num][cd]
                            dx, dy = directions[cd]
                        else:
                            cx, cy = wormholes[(cx, cy)]

                    if crashed <= best_score:
                        for rx, ry, rd, rc in route:
                            score[rx][ry][rd] = 0
                    else:
                        # 점수 마킹(한 점에 몇 번 들르는지 모르므로 맨 앞 거는 한 번 더 돌아와야 알 수 있음)
                        for rx, ry, rd, rc in route:
                            if last_route_num_and_direction_of_the_block[rx][ry] >> 2 == route_num:
                                bd = last_route_num_and_direction_of_the_block[rx][ry] & 3  # before direction
                                score[rx][ry][bd] -= (crashed - rc)
                            score[rx][ry][rd] = crashed - rc
                            last_route_num_and_direction_of_the_block[rx][ry] = route_num << 2 | rd
                        # 점수 체크 (맨 뒤 거는 맨 앞 거의 rc만큼 더해줘야됨, 더하고나면 루트번호마킹 지우기)
                        for rx, ry, rd, rc in route:
                            if last_route_num_and_direction_of_the_block[rx][ry]:
                                ld = last_route_num_and_direction_of_the_block[rx][ry] & 3  # last direction
                                score[rx][ry][ld] += rc
                                last_route_num_and_direction_of_the_block[rx][ry] = 0
                            if score[rx][ry][rd] > best_score:
                                best_score = score[rx][ry][rd]
                                if best_score == crashed:
                                    break

    print(f'#{tc}', best_score)