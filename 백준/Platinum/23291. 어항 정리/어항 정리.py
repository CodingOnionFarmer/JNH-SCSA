"""
BOJ : 어항 정리

시작 시간 : 3시 35분
구상 완료 : 3시 39분
테케 틀림 : 4시 19분
1회 오답 : 4시 32분
제출 시간 : 4시 41분

"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, k = map(int, input().split())
fish_tank = list(map(int, input().split()))
ans = 0

while True:
    least = min(fish_tank)
    most = max(fish_tank)
    if most - least <= k:
        break
    for i in range(n):
        if fish_tank[i] == least:
            fish_tank[i] += 1
    ans += 1

    # print('==============')
    # print(ans)
    # print(fish_tank)
    # print(sum(fish_tank))

    temp = [[fish_tank[i]] for i in range(n)]
    temp[1].append(temp[0][0])
    left = 1
    width = 1
    height = 2

    while left + width + height <= n:
        new_left = left + width
        for h in range(height):
            for w in range(left + width - 1, left - 1, -1):
                temp[new_left + h].append(temp[w][h])
        left = new_left
        width, height = height, width + 1

    fish_move = [[0] * height for _ in range(width)] + [[0] for _ in range(n - left - width)]
    for w in range(width):
        # 체스판 모양으로 지그재그로 탐색(중복 탐색 피하기 위함)
        for h in range(w & 1, height, 2):
            fish = temp[left + w][h]
            for dw, dh in directions:
                nw, nh = w + dw, h + dh
                if 0 <= nw < width and 0 <= nh < height:
                    diff = fish - temp[left + nw][nh]
                    if diff > 4:
                        diff //= 5
                        fish_move[w][h] -= diff
                        fish_move[nw][nh] += diff
                    elif diff < -4:
                        diff = -diff // 5
                        fish_move[w][h] += diff
                        fish_move[nw][nh] -= diff

    for w in range(width, n - left):
        # 왼쪽하고만 비교 (중복 탐색 없이)
        diff = temp[left + w][0] - temp[left + w - 1][0]
        if diff > 4:
            diff //= 5
            fish_move[w][0] -= diff
            fish_move[w - 1][0] += diff
        elif diff < -4:
            diff = -diff // 5
            fish_move[w][0] += diff
            fish_move[w - 1][0] -= diff

    # print(fish_move)
    # print(temp)

    new_temp = []
    for w in range(n - left):
        for h in range(len(fish_move[w])):
            new_temp.append([temp[left + w][h] + fish_move[w][h]])

    for w in range(n >> 1):
        new_temp[n - 1 - w].append(new_temp[w][0])

    left = n >> 1
    for w in range(n >> 2):
        new_temp[n - 1 - w].append(new_temp[left + w][1])
        new_temp[n - 1 - w].append(new_temp[left + w][0])
    left += n >> 2

    fish_move = [[0] * 4 for _ in range(n >> 2)]
    for w in range(n >> 2):
        # 지그재그 탐색
        for h in range(w & 1, 4, 2):
            fish = new_temp[left + w][h]
            for dw, dh in directions:
                nw, nh = w + dw, h + dh
                if 0 <= nw < n - left and 0 <= nh < 4:
                    diff = fish - new_temp[left + nw][nh]
                    if diff > 4:
                        diff //= 5
                        fish_move[w][h] -= diff
                        fish_move[nw][nh] += diff
                    elif diff < -4:
                        diff = -diff // 5
                        fish_move[w][h] += diff
                        fish_move[nw][nh] -= diff

    # print(fish_move)
    # print(new_temp)

    fish_tank = []
    for w in range(n - left):
        for h in range(4):
            fish_tank.append(new_temp[left + w][h] + fish_move[w][h])

print(ans)
# print(fish_tank)
