directions = ((1, 0), (0, -1), (-1, 0), (0, 1))  # 우 하 좌 상
turn = ((3, 0, 1, 2), (1, 2, 3, 0))
m, n = map(int, input().split())
ci, cj, cd = 0, 0, 0
valid = True
for _ in range(n):
    order, num = input().split()
    number = int(num)
    if order == 'MOVE':
        di, dj = directions[cd]
        ci, cj = ci + di * number, cj + dj * number
        if ci < 0 or ci > m or cj < 0 or cj > m:
            valid = False
            break
    else:
        cd = turn[number][cd]
if valid:
    print(ci, cj)
else:
    print(-1)
