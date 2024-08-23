"""
시작 시간 : 2시 42분
제출 시간 : 3시 05분


"""

# 구현, 시뮬레이션

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robots = []
up = 0
down = n - 1
step = 0
next_num = tuple((i + 1) % (n << 1) for i in range(n << 1))

while True:
    step += 1
    up -= 1
    down -= 1
    if up < 0:
        up = 2 * n - 1
    if down < 0:
        down = 2 * n - 1
    if robots and robots[0] == down:
        robots.pop(0)
    for idx, robot in enumerate(robots):
        if robots[idx - 1] != next_num[robot] and belt[next_num[robot]]:
            robots[idx] = next_num[robot]
            belt[robots[idx]] -= 1
    if robots and robots[0] == down:
        robots.pop(0)
    if belt[up]:
        robots.append(up)
        belt[up] -= 1
    if belt.count(0) >= k:
        break
print(step)
