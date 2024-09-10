directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, k = map(int, input().split())
fish_tank = list(map(int, input().split()))
ans = 0
temp = [[i] for i in range(n)]
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

adj1 = [[] for _ in range(n)]
for w in range(width):
    for h in range(w & 1, height, 2):
        idx = temp[left + w][h]
        for dw, dh in directions:
            nw, nh = w + dw, h + dh
            if 0 <= nw < width and 0 <= nh < height:
                adj1[idx].append(temp[left + nw][nh])
for w in range(width, n - left):
    adj1[temp[left + w][0]].append(temp[left + w - 1][0])

new_temp = []
for w in range(n - left):
    for h in range(len(temp[left + w])):
        new_temp.append([temp[left + w][h]])

for w in range(n >> 1):
    new_temp[n - 1 - w].append(new_temp[w][0])

left = n >> 1
for w in range(n >> 2):
    new_temp[n - 1 - w].append(new_temp[left + w][1])
    new_temp[n - 1 - w].append(new_temp[left + w][0])
left += n >> 2

adj2 = [[] for _ in range(n)]
for w in range(n >> 2):
    for h in range(w & 1, 4, 2):
        idx = new_temp[left + w][h]
        for dw, dh in directions:
            nw, nh = w + dw, h + dh
            if 0 <= nw < n - left and 0 <= nh < 4:
                adj2[idx].append(new_temp[left + nw][nh])

newly_arranged = []
for w in range(n - left):
    for h in range(4):
        newly_arranged.append(new_temp[left + w][h])

while True:
    least = min(fish_tank)
    most = max(fish_tank)
    if most - least <= k:
        break
    for i in range(n):
        if fish_tank[i] == least:
            fish_tank[i] += 1
    ans += 1

    fish_move = [0] * n
    for i in range(n):
        fish = fish_tank[i]
        for ni in adj1[i]:
            diff = fish - fish_tank[ni]
            if diff > 4:
                diff //= 5
                fish_move[i] -= diff
                fish_move[ni] += diff
            elif diff < -4:
                diff = -diff // 5
                fish_move[i] += diff
                fish_move[ni] -= diff
    for idx, move in enumerate(fish_move):
        fish_tank[idx] += move

    fish_move = [0] * n
    for i in range(n):
        fish = fish_tank[i]
        for ni in adj2[i]:
            diff = fish - fish_tank[ni]
            if diff > 4:
                diff //= 5
                fish_move[i] -= diff
                fish_move[ni] += diff
            elif diff < -4:
                diff = -diff // 5
                fish_move[i] += diff
                fish_move[ni] -= diff
    for idx, move in enumerate(fish_move):
        fish_tank[idx] += move

    new_fish_tank = []
    for original_idx in newly_arranged:
        new_fish_tank.append(fish_tank[original_idx])
    fish_tank = new_fish_tank

print(ans)
