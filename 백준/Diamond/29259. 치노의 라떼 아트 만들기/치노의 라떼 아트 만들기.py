import math

vertical = 234
horizontal = 116
x = y = 0
moves = []
cnt = 0
h = 0
w = 0
for n in range(1, vertical + 1):
    for m in range(1, horizontal + 1):
        if math.gcd(n, m) == 1:
            cnt += 1
            h += n
            w += m
            moves.append((m / n, m, n))
for m in range(1, 83):
    if math.gcd(235, m) == 1:
        cnt += 1
        h += 235
        w += m
        moves.append((m / 235, m, 235))
# print(cnt, h, w)
moves.sort()
# print(moves)
# print(0, 0)
for i, dx, dy in moves:
    x += dx
    y += dy
    print(x, y)
x += 127
y += 1
print(x, y)
x += 1
print(x, y)
x += 127
y -= 1
print(x, y)
for i in range(16664, -1, -1):
    x += moves[i][1]
    y -= moves[i][2]
    print(x, y)
y -= 1
print(x, y)
for i, dx, dy in moves:
    x -= dx
    y -= dy
    print(x, y)
x -= 970142
y -= 1
print(x, y)
x -= 970142
y += 1
print(x, y)
for i in range(16664, -1, -1):
    x -= moves[i][1]
    y += moves[i][2]
    print(x, y)
y += 1
print(x, y)
for i, dx, dy in moves:
    x += dx
    y += dy
    print(x, y)
x += 127
y += 1
print(x, y)
x += 1
print(x, y)
x += 127
y -= 1
print(x, y)
for i in range(16664, -1, -1):
    x += moves[i][1]
    y -= moves[i][2]
    print(x, y)
