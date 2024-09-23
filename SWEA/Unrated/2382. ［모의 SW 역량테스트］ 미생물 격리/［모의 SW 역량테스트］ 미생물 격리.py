directions = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))  # 0은 더미 데이터, 상1 하2 좌3 우4
turn_180 = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = [[-1] * n for _ in range(n)]
    microbes = []
    alive = {i for i in range(k)}
    for i in range(k):
        x, y, c, d = map(int, input().split())
        microbes.append([x, y, c, d, 0, 0])  # 5번째 인자는 움직인 시간 수, 6번째 인자는 움직이고 나서 모였을 때 제일 많은 군집 개수
    for hour in range(m):
        dead = []
        for idx in alive:
            x, y, c, d, moved, nothing = microbes[idx]
            # 이미 움직여서 온 군집 번호가 있을 수도 있으므로 그럴 땐 -1로 안 비운다.
            if board[x][y] == idx:
                board[x][y] = -1
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy

            # 가장자리에서는 다른 군집과 겹칠 일 x
            if not nx or not ny or nx == n - 1 or ny == n - 1:
                # 절반돼서 0되면 삭제
                if c == 1:
                    dead.append(idx)
                    continue
                board[nx][ny] = idx
                microbes[idx] = [nx, ny, c >> 1, turn_180[d], moved + 1, 0]
                continue

            # 빈 칸이거나 움직이기 전인 녀석이 있으면(동시에 움직일 거니까 사실 빈칸)
            if board[nx][ny] == -1 or microbes[board[nx][ny]][4] == hour:
                board[nx][ny] = idx
                microbes[idx] = [nx, ny, c, d, moved + 1, c]

            # 이미 온 다른 군집과 만난 경우
            else:
                other = board[nx][ny]
                info = microbes[other]
                total, cd, most = info[2], info[3], info[5]
                # 내가 지면 병합됨
                if most > c:
                    dead.append(idx)
                    info[2] += c
                # 내가 이기면 있던 애를 병합시킴
                else:
                    dead.append(other)
                    board[nx][ny] = idx
                    microbes[idx] = [nx, ny, total + c, d, moved + 1, c]

        for idx in dead:
            alive.remove(idx)

    print(f'#{tc}', sum(microbes[idx][2] for idx in alive))
