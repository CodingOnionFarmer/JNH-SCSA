n, w = int(input()), int(input())
work = [tuple(map(int, input().split())) for _ in range(w)]
latest = [[0] * (w + 1) for _ in range(w + 1)]
for i in range(w + 1):
    for j in range(w + 1):
        if i == j:
            continue
        elif not i:
            if j == 1:
                latest[i][j] = 2 * n - sum(work[0])
            else:
                latest[i][j] = latest[i][j - 1] + abs(work[j - 1][0] - work[j - 2][0]) + abs(
                    work[j - 1][1] - work[j - 2][1])
        elif not j:
            if i == 1:
                latest[i][j] = sum(work[0]) - 2
            else:
                latest[i][j] = latest[i - 1][j] + abs(work[i - 1][0] - work[i - 2][0]) + abs(
                    work[i - 1][1] - work[i - 2][1])
        elif i - j == 1:
            latest[i][j] = min(
                [latest[k][j] + abs(work[i - 1][0] - work[k - 1][0]) + abs(work[i - 1][1] - work[k - 1][1]) for k in
                 range(1, i - 1)] + [latest[0][j] + sum(work[i - 1]) - 2])
        elif j - i == 1:
            latest[i][j] = min(
                [latest[i][k] + abs(work[j - 1][0] - work[k - 1][0]) + abs(work[j - 1][1] - work[k - 1][1]) for k in
                 range(1, j - 1)] + [latest[i][0] + 2 * n - sum(work[j - 1])])
        elif i > j:
            latest[i][j] = latest[i - 1][j] + abs(work[i - 1][0] - work[i - 2][0]) + abs(
                work[i - 1][1] - work[i - 2][1])
        else:
            latest[i][j] = latest[i][j - 1] + abs(work[j - 1][0] - work[j - 2][0]) + abs(
                work[j - 1][1] - work[j - 2][1])
shortest = 2000001
x, y = 0, 0
for i in range(w):
    if latest[i][w] < shortest:
        shortest = latest[i][w]
        x, y = i, w
    if latest[w][i] < shortest:
        shortest = latest[w][i]
        x, y = w, i
print(shortest)
order = []
for i in range(w):
    if x > y:
        order.append(1)
        if x - y == 1:
            if latest[x][y] - latest[0][y] == sum(work[x - 1]) - 2:
                x = 0
            else:
                for j in range(1, x - 1):
                    if latest[x][y] - latest[j][y] == abs(work[x - 1][0] - work[j - 1][0]) + abs(
                            work[x - 1][1] - work[j - 1][1]):
                        x = j
                        break
        else:
            x -= 1
    else:
        order.append(2)
        if y - x == 1:
            if latest[x][y] - latest[x][0] == 2 * n - sum(work[y - 1]):
                y = 0
            else:
                for j in range(1, y - 1):
                    if latest[x][y] - latest[x][j] == abs(work[y - 1][0] - work[j - 1][0]) + abs(
                            work[y - 1][1] - work[j - 1][1]):
                        y = j
                        break
        else:
            y -= 1
for i in range(w):
    print(order[w - i - 1])
