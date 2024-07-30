import sys

input = sys.stdin.readline

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

for tc in range(int(input())):
    m, n, k = map(int, input().split())
    field = [[0] * (n + 1) for _ in range(m + 1)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[x][y] = 1
    worm = 0
    for i in range(m):
        for j in range(n):
            if field[i][j]:
                worm += 1
                stack = [(i, j)]
                while stack:
                    ci, cj = stack.pop()
                    if field[ci][cj]:
                        field[ci][cj] = 0
                        for di, dj in direction:
                            if field[ci + di][cj + dj]:
                                stack.append((ci + di, cj + dj))
    print(worm)
