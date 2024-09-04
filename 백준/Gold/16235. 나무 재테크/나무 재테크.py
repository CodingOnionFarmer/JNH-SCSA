"""
BOJ : 나무 재테크

시작 시간 : 4시 33분
구상 완료 : 4시 35분
테케 틀림 : 4시 52분
제출 시간 : 4시 53분

"""

n, m, k = map(int, input().split())

# directions = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j)
# print(directions)
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
adj = tuple(
    tuple(tuple((i + di, j + dj) for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n) for j in range(n))
    for i in range(n)
)

soil = [[5] * n for _ in range(n)]
trees = [[[] for __ in range(n)] for _ in range(n)]
baby_trees = [[0] * n for _ in range(n)]

winter_soil = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)

for year in range(k):
    for i in range(n):
        for j in range(n):
            baby = baby_trees[i][j]
            tree = trees[i][j]
            s = soil[i][j]
            if baby >= s:
                trees[i][j] = [2] * s
                soil[i][j] = sum(t >> 1 for t in tree)
                continue
            s -= baby
            trees[i][j] = [2] * baby
            dead = 0
            for t in tree:
                if t <= s:
                    s -= t
                    trees[i][j].append(t + 1)
                else:
                    dead += t >> 1
            soil[i][j] = s + dead

    baby_trees = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for age in trees[i][j]:
                if not age % 5:
                    for ni, nj in adj[i][j]:
                        baby_trees[ni][nj] += 1
            soil[i][j] += winter_soil[i][j]

print(sum(sum(len(trees[i][j]) for i in range(n)) for j in range(n)) + sum(sum(line) for line in baby_trees))
