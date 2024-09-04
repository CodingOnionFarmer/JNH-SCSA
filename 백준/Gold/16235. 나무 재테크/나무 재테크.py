"""
BOJ : 나무 재테크

시작 시간 : 4시 33분
구상 완료 : 4시 35분
테케 틀림 : 4시 52분
제출 시간 : 4시 53분

"""

# directions = tuple((i, j) for i in range(-1, 2) for j in range(-1, 2) if i or j)
# print(directions)
directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

n, m, k = map(int, input().split())
soil = [[5] * n for _ in range(n)]
trees = [[[] for __ in range(n)] for _ in range(n)]

winter_soil = [list(map(int, input().split())) for _ in range(n)]
for tree in range(m):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
for i in range(n):
    for j in range(n):
        trees[i][j].sort()

for year in range(k):
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for idx, age in enumerate(trees[i][j]):
                    if age <= soil[i][j]:
                        soil[i][j] -= age
                        trees[i][j][idx] += 1
                    else:
                        dead = 0
                        for old in range(idx, len(trees[i][j])):
                            dead += trees[i][j].pop() >> 1
                        soil[i][j] += dead
                        break

    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                for age in trees[i][j]:
                    if not age % 5:
                        for di, dj in directions:
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                trees[ni][nj].insert(0, 1)
            soil[i][j] += winter_soil[i][j]

print(sum(sum(len(trees[i][j]) for i in range(n)) for j in range(n)))
