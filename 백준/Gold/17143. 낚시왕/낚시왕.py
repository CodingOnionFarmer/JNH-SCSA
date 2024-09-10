directions = (0, -1, 1, 1, -1)

r, c, m = map(int, input().split())
board = {}
sharks = {}
for i in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    board[x * c + y] = z
    if d < 3:
        s %= 2 * r - 2
    else:
        s %= 2 * c - 2
    sharks[z] = [s, d]

ans = 0
for column in range(c):
    for row in range(r):
        if column in board:
            ans += board[column]
            board.pop(column)
            break
        column += c
    moved = {}
    for position in board:
        x, y = position // c, position % c
        weight = board[position]
        speed, direction = sharks[weight]
        if direction > 2:
            ny = y + directions[direction] * speed
            if ny < 0:
                ny = -ny
                if ny >= c:
                    ny = c * 2 - ny - 2
                else:
                    sharks[weight][1] = 7 - direction
            elif ny >= c:
                ny = c * 2 - ny - 2
                if ny < 0:
                    ny = -ny
                else:
                    sharks[weight][1] = 7 - direction
            np = x*c + ny
            if np not in moved or moved[np] < weight:
                moved[np] = weight
        else:
            nx = x + directions[direction] * speed
            if nx < 0:
                nx = -nx
                if nx >= r:
                    nx = r * 2 - nx - 2
                else:
                    sharks[weight][1] = 3 - direction
            elif nx >= r:
                nx = r * 2 - nx - 2
                if nx < 0:
                    nx = -nx
                else:
                    sharks[weight][1] = 3 - direction
            np = nx*c + y
            if np not in moved or moved[np] < weight:
                moved[np] = weight
    board = moved

print(ans)
