"""
시작 시간 : 3시 06분
제출 시간 : 3시 27분


"""

# 구현, 시뮬레이션


n, m = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]  # 인덱스 주의

# 룩업 테이블 구성
directions = ((), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
# adj[i][j]는 i,j 칸에 대각인접한 칸들 (out of bound 검사 매번 하지 않고 한 번 해 놓고 계속 쓰기)
adj = [[[] for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        for d in (2, 4, 6, 8):
            di, dj = directions[d]
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:
                adj[i][j].append((ni, nj))

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for turn in range(m):
    cloud_cleared = [[False] * n for i in range(n)]
    d, s = map(int, input().split())
    di, dj = directions[d]
    mi, mj = di * s, dj * s
    moved_clouds = [((i + mi) % n, (j + mj) % n) for i, j in clouds]
    for i, j in moved_clouds:
        water[i][j] += 1
        cloud_cleared[i][j] = True
    for i, j in moved_clouds:
        water_copy_bug = 0
        for ai, aj in adj[i][j]:
            if water[ai][aj]:
                water_copy_bug += 1
        water[i][j] += water_copy_bug
    clouds = []
    for i in range(n):
        for j in range(n):
            if not cloud_cleared[i][j] and water[i][j] >= 2:
                clouds.append((i, j))
                water[i][j] -= 2

print(sum(sum(line) for line in water))
