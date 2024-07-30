import sys

input = sys.stdin.readline

direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

m, n, k = map(int, input().split())
paper = [[1] * n + [0] for _ in range(m)] + [[0] * n]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 0
areas = []
for i in range(m):
    for j in range(n):
        if paper[i][j]:
            area = 0
            stack = [(i, j)]
            while stack:
                ci, cj = stack.pop()
                if paper[ci][cj]:
                    paper[ci][cj] = 0
                    area += 1
                    for di, dj in direction:
                        if paper[ci + di][cj + dj]:
                            stack.append((ci + di, cj + dj))
            areas.append(area)
areas.sort()
print(len(areas))
print(*areas)
