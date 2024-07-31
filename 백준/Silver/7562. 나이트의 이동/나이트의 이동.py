# 충분히 가까워질 때까지 greedy한 move
# 충분히 가까운 곳은 하드코딩


tc = int(input())
needed_moves = (
    (0, 3, 2, 3, 2),
    (3, 2, 1, 2, 3),
    (2, 1, 4, 3, 2),
    (3, 2, 3, 2, 3),
    (2, 3, 2, 3, 4),
)
for _ in range(tc):
    l = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    x, y = abs(a - c), abs(b - d)
    if x > y:  # x가 더 작게, y가 더 크게 맞춰줌 (개념상 x가 세로축, y가 가로축 좌표)
        x, y = y, x

    # 예외처리 파트, 구석에 몰려 있거나 판이 작으면 문제가 생길 수 있음
    oa, ob = l - a - 1, l - b - 1
    oc, od = l - c - 1, l - d - 1
    ab_in_corner = (not a or not oa) and (not b or not ob)
    cd_in_corner = (not c or not oc) and (not d or not od)
    if ab_in_corner:
        if cd_in_corner and x + y == 3:  # 4x4에서 둘 다 구석이고 가로나 세로로 3만큼만 떨어져 있을 때
            print(5)
            continue
        elif x == 1 and y == 1:
            print(4)
            continue
    elif cd_in_corner and x == 1 and y == 1:
        print(4)
        continue

    ans = 0

    # 중요 : greedy move의 근거는 needed_move에 진입하기 직전의 상태에 따른 횟수를 직접 카운트하여 경우의 수를 따져야 함

    if y > 7 and x > 1:  # 가로 4 세로 2만큼 greedy move 최대한 수행
        # x,y의 대소관계가 깨지지 않고, x가 0보다 작아지지 않고, y가 4보다 작아지지 않는 최대한의 move
        move = min(y // 4 - 1, x // 2, (y - x) // 2)
        ans += move * 2
        y -= move * 4
        x -= move * 2

    if x > 5:  # 위의 move 조건 중 x,y의 대소관계 때문에 x와 y가 비슷해진 채로 멈춘 경우
        # 두 번 이동으로 가로3 세로3만큼 이동하는 greedy move 수행
        diagonal_move = x // 3 - 1
        # 5,5에서 2,2로 들어가면 망하므로 한 번 덜 가야함
        # 6,6에서 3,3, 6,7에서 3,4, 7,7에서 4,4로 들어가는 것은 정당한 move이므로 x가 6 이상일 때는 가도 됨
        ans += diagonal_move * 2
        x -= diagonal_move * 3
        y -= diagonal_move * 3

    if y > 7:  # x는 최대 5인 상태
        # 두 번 이동으로 가로로만 4 이동하는 move 수행
        # y를 4씩 가능한 만큼 줄일 건데, x값을 줄일 수 있으면 가로4 세로2 move 한 번을 해서 줄여야 함
        # 5,6에서 4,4로 진입하면 4번이지만 3,6이나 1,6에서 2,4나 0,4로 진입하면 2번으로 되기 때문
        # 이런 경우가 실제로 안 나올 수도 있으나, 디버깅하기 어렵다고 판단하여 안전하게 체크
        # 그 외에는 두 번 이동으로 가로4만큼 이동하는 greedy move 수행
        y_move = y // 4 - 1
        if x > 2:
            x -= 2
        ans += y_move * 2
        y -= y_move * 4

    while y > 4:  # 아직 x,y가 5,5나 4,6이나 4,7 등의 상태가 가능
        # 경우의 수를 따져 봤을 때, 가로2칸 세로1칸씩 직선 진입하면 문제없음
        x = abs(x - 1)
        y -= 2
        ans += 1

    ans += needed_moves[x][y]
    print(ans)
