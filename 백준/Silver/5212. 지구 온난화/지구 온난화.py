# 구현, 시뮬레이션

# 조건 꼼꼼히 파악 : 지도 밖은 모두 바다이다.
# 3면 또는 4면이 바다로 둘러싸인 칸은 바다가 된다.

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
r, c = map(int, input().split())
now_map = [list(input()) + ['.'] for _ in range(r)] + [['.'] * c]
later_map = [['.'] * c for _ in range(r)]
rows = []
columns = []
for i in range(r):
    for j in range(c):
        if now_map[i][j] == 'X':
            adj_sea = 0
            for di, dj in directions:
                if now_map[i + di][j + dj] == '.':
                    adj_sea += 1
            if adj_sea < 3:
                later_map[i][j] = 'X'
                rows.append(i)
                columns.append(j)
up = min(rows)
down = max(rows)
left = min(columns)
right = max(columns)
for i in range(up, down + 1):
    print(*later_map[i][left:right + 1], sep='')
