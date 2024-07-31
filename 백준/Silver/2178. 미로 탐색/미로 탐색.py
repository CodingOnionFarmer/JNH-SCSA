# 이차원 좌표를 정수 하나로 바꿔서 효율 늘리는 시도
# 메모리를 더 써서 시간을 줄이는 시도


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
maze = []
for _ in range(n):
    line = input().rstrip('\n')
    for num in line:
        maze.append(int(num))
    maze.append(0)
for _ in range(m):
    maze.append(0)
m += 1
goal = n * m - 2
queue = [(0, 1)]
maze[0] = 0
p = 0
while True:
    position, step = queue[p]
    if position == goal:
        print(step)
        break
    step += 1
    for adj in (position - 1, position + 1, position - m, position + m):
        if maze[adj]:
            queue.append((adj, step))
            maze[adj] = 0
    p += 1
