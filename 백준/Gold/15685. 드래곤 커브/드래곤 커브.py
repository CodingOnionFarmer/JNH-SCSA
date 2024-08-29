"""
BOJ : 드래곤 커브

시작 시간 : 3시 36분
구상 완료 : 3시 46분
제출 시간 : 3시 55분
"""

directions = ((1, 0), (0, -1), (-1, 0), (0, 1))
counter_clockwise = (1, 2, 3, 0)

dragon_curve = [[0]]
for generation in range(1, 11):
    new_curve = dragon_curve[-1][:]
    for p in range(len(new_curve) - 1, -1, -1):
        new_curve.append(counter_clockwise[new_curve[p]])
    dragon_curve.append(new_curve)

n = int(input())
dots = [[False] * 101 for _ in range(101)]
for dc in range(n):
    x, y, d, g = map(int, input().split())
    dots[x][y] = True
    for dcd in dragon_curve[g]:
        dx, dy = directions[(dcd + d) % 4]
        x += dx
        y += dy
        dots[x][y] = True

ans = 0
for i in range(100):
    for j in range(100):
        if dots[i][j] and dots[i + 1][j] and dots[i][j + 1] and dots[i + 1][j + 1]:
            ans += 1
print(ans)
