# 언어 : PyPy 7.3.4
# 메모리 : 59204KB
# 시간 : 386ms (2회차)
# 시도횟수 : 3회차 (리팩토링)

directions = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))  # 0은 더미 데이터, 상1 하2 좌3 우4
turn_180 = (0, 2, 1, 4, 3)

T = int(input())
for tc in range(1, T + 1):
    n, m, k = map(int, input().split())
    board = {}
    microbes = []
    for i in range(k):
        x, y, c, d = map(int, input().split())
        microbes.append([x, y, c, d, 0, 0])  # 5번째 인자는 움직인 시간 수, 6번째 인자는 움직이고 나서 모였을 때 제일 많은 군집 개수
        board[x * n + y] = i
    for hour in range(m):
        temp = {}
        for idx in board.values():
            x, y, c, d, moved, nothing = microbes[idx]
            dx, dy = directions[d]
            nx, ny = x + dx, y + dy
            np = nx * n + ny  # next position

            # 가장자리에서는 다른 군집과 겹칠 일 x
            if not nx or not ny or nx == n - 1 or ny == n - 1:
                if c > 1:
                    microbes[idx] = [nx, ny, c >> 1, turn_180[d], moved + 1, 0]
                    temp[np] = idx
                continue

            # 빈 칸이면 그냥 착륙
            if np not in temp:
                microbes[idx] = [nx, ny, c, d, moved + 1, c]
                temp[np] = idx

            # 이미 온 다른 군집과 만난 경우
            else:
                other = temp[np]
                info = microbes[other]
                total, cd, most = info[2], info[3], info[5]
                # 내가 지면 병합됨
                if most > c:
                    info[2] += c
                # 내가 이기면 있던 애를 병합시킴
                else:
                    temp[np] = idx
                    microbes[idx] = [nx, ny, total + c, d, moved + 1, c]

        board = temp

    print(f'#{tc}', sum(microbes[idx][2] for idx in board.values()))
