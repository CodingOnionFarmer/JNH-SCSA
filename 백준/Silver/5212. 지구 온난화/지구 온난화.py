# 구현, 시뮬레이션

# 조건 꼼꼼히 파악 : 지도 밖은 모두 바다이다.
# 3면 또는 4면이 바다로 둘러싸인 칸은 바다가 된다.

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
r, c = map(int, input().split())
now_map = [list(input()) + ['.'] for _ in range(r)] + [['.'] * c]  # 현재 지도
# 원본 지도를 수정해서는 풀기 어려우므로(인접 칸 판정 때문에), 50년 뒤의 지도를 따로 만드는 것이 낫다.
later_map = [['.'] * c for _ in range(r)]  # 50년 뒤의 지도
rows = []  # 50년 뒤의 지도에 남아있는 땅 칸들의 행 위치
columns = []  # 열 위치
for i in range(r):
    for j in range(c):
        if now_map[i][j] == 'X':
            adj_sea = 0  # 인접한 칸 중 바다의 수
            for di, dj in directions:
                # 미리 바다로 Padding을 쳐 놨으므로 Out of Bound 검사 안 해도 된다.
                if now_map[i + di][j + dj] == '.':
                    adj_sea += 1
            if adj_sea < 3:  # 인접한 칸 중 땅이 2개 이상이면
                later_map[i][j] = 'X'  # 50년 뒤에도 남아있다.
                rows.append(i)
                columns.append(j)
up = min(rows)
down = max(rows)
left = min(columns)
right = max(columns)
for i in range(up, down + 1):  # up행부터 down행까지
    print(*later_map[i][left:right + 1], sep='')  # left열부터 right열까지가 최소 크기의 지도이다.
