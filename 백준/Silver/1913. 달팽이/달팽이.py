directions = ((1, 0), (0, -1), (-1, 0), (0, 1))  # 하 좌 상 우
turn = (1, 2, 3, 0)
n = int(input())
m = int(input())
snail = [[0] * n for _ in range(n)]
ci, cj, cd = n >> 1, n >> 1, 2
number = 1
snail[ci][cj] = 1
answer = [ci + 1, cj + 1]
for scale in range(1, n):
    for _ in range(scale):
        number += 1
        di, dj = directions[cd]
        ci += di
        cj += dj
        snail[ci][cj] = number
        if number == m:
            answer = [ci + 1, cj + 1]
    cd = turn[cd]
    for _ in range(scale):
        number += 1
        di, dj = directions[cd]
        ci += di
        cj += dj
        snail[ci][cj] = number
        if number == m:
            answer = [ci + 1, cj + 1]
    cd = turn[cd]
for _ in range(n - 1):
    number += 1
    di, dj = directions[cd]
    ci += di
    cj += dj
    snail[ci][cj] = number
    if number == m:
        answer = [ci + 1, cj + 1]
for line in snail:
    print(*line)
print(*answer)
