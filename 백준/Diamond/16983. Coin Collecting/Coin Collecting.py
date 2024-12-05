import sys

input = sys.stdin.readline

n = int(input())
coins = [tuple(map(int, input().split())) for _ in range(n << 1)]
rectangle = [[0, 0] for _ in range(n + 1)]
column = 1
cnt = 0
answer = 0
positive = 0
for x, y in coins:
    if y > 1:
        answer += y - 2
        y = 1
    else:
        answer += 1 - y
        y = 0
    if x < 1:
        answer += 1 - x
        x = 1
    elif x > n:
        answer += x - n
        x = n
    rectangle[x][y] += 1
for i in range(1, n + 1):
    d, u = rectangle[i]
    s = d + u
    if s == 2:
        answer += abs(u - d) >> 1
        continue
    if s > 2:
        if u < 1:
            answer += d - 1
            rectangle[i + 1][0] += s - 2
            continue
        if d < 1:
            answer += u - 1
            rectangle[i + 1][1] += s - 2
            continue
        answer += s - 2
        rectangle[i + 1][0] += d - 1
        rectangle[i + 1][1] += u - 1
        continue
    if u > 1:
        answer += 1 - d
        rectangle[i + 1][0] += s - 2
        continue
    if d > 1:
        answer += 1 - u
        rectangle[i + 1][1] += s - 2
        continue
    answer += 2 - s
    rectangle[i + 1][0] += d - 1
    rectangle[i + 1][1] += u - 1
print(answer)
