# set을 이용한 bfs
# 이차원 좌표를 정수 하나로 바꿔서 효율 늘리는 시도


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
now = [0]
maze[0] = 0
step = 1
while maze[goal]:
    next_step = []
    for position in now:
        for adj in (position + 1, position - 1, position + m, position - m):
            if maze[adj]:
                next_step.append(adj)
                maze[adj] = 0
    step += 1
    now = next_step
print(step)
