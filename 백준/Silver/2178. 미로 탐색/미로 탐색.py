# set을 이용한 bfs


n, m = map(int, input().split())
maze = [list(input()) + ['0'] for _ in range(n)] + [['0'] * m]
now = {(0, 0)}
step = 1
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
while (n - 1, m - 1) not in now:
    next_step = set()
    for i, j in now:
        maze[i][j] = '0'
        for di, dj in directions:
            if maze[i + di][j + dj] == '1':
                next_step.add((i + di, j + dj))
    step += 1
    now = next_step
print(step)
