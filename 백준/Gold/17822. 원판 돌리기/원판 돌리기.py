n, m, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)] + [[0] * m]
line_rotated = [0] * n
num_cnt = n * m
num_sum = 0
for i in range(n):
    for j in range(m):
        num_sum += board[i][j]

for query in range(t):
    if num_cnt <= 1:
        break
    x, d, k = map(int, input().split())
    if d:
        k = m - k

    for line_num in range(x, n + 1, x):
        line_num -= 1
        line_rotated[line_num] -= k
        if line_rotated[line_num] <= -m:
            line_rotated[line_num] += m

    erase = set()

    for i in range(n):
        lr = line_rotated[i]
        lr_up = line_rotated[i - 1]
        for j in range(m):
            num = board[i][j + lr]
            if not num:
                continue

            left_num = board[i][j + lr - 1]
            up_num = board[i - 1][j + lr_up]
            if left_num == num:
                erase.add(i * m + (j + lr) % m)
                erase.add(i * m + (j + lr - 1) % m)
                if up_num == num:
                    erase.add((i - 1) % n * m + (j + lr_up) % m)
            elif up_num == num:
                erase.add((i * m + (j + lr) % m))
                erase.add((i - 1) % n * m + (j + lr_up) % m)

    if erase:
        num_cnt -= len(erase)
        for position in erase:
            i, j = position // m, position % m
            num_sum -= board[i][j]
            board[i][j] = 0

    else:
        changed = 0
        for r in range(n):
            for c in range(m):
                if not board[r][c]:
                    continue
                is_num_over_average = board[r][c] * num_cnt
                if is_num_over_average > num_sum:
                    board[r][c] -= 1
                    changed -= 1
                elif is_num_over_average < num_sum:
                    board[r][c] += 1
                    changed += 1
        num_sum += changed

print(num_sum)
