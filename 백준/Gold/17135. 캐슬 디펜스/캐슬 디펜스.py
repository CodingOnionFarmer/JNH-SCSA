# 기본적으로 생각할 것
# 사거리 조건에 맞는 적을 찾을 때, n*m 행렬의 범위 체크를 꼼꼼히 해야 한다.
# 또는 10의 사거리에 맞춰 위로 10줄, 오른쪽으로 10줄씩 0을 추가해서 padding을 쳐도 된다.

# 구현을 효율적으로 하기 위해서 여러 가지 고민을 했다.
#


n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
edfp = [[] for _ in range(m)]  # enemy_distance_from_position
# edfp[j]에는 j번 위치에서 쏠 때 각 적의 거리,적위치의 x좌표,y좌표 순으로 정보를 저장한다.
for i in range(n):
    for j in range(m):
        if board[i][j]:
            for k in range(j):
                edfp[k].append((n - i + j - k, j, i))
                # 거리가 같으면 왼쪽 우선 타겟팅이므로, j를 i보다 앞에 둬서 sort에 우선순위를 준다.
            for k in range(j, m):
                edfp[k].append((n - i + k - j, j, i))
for j in range(m):
    edfp[j].sort()

most_killed = 0
for a1 in range(m - 2):  # archer1
    for a2 in range(a1 + 1, m - 1):  # archer2
        for a3 in range(a2 + 1, m):  # archer3
            dead = [[False] * m for _ in range(n)]
            killed = 0
            p1 = p2 = p3 = 0  # 각 궁수가 우선순위 순으로 쏘는 적의 index
            for turn in range(n):
                targets = set()
                while p1 < len(edfp[a1]):
                    d1, x1, y1 = edfp[a1][p1]
                    if y1 >= n - turn:
                        p1 += 1
                        continue
                    if dead[y1][x1]:
                        p1 += 1
                        continue
                    if d1 - turn <= d:
                        targets.add((y1, x1))
                        p1 += 1
                    break
                while p2 < len(edfp[a2]):
                    d2, x2, y2 = edfp[a2][p2]
                    if y2 >= n - turn:
                        p2 += 1
                        continue
                    if dead[y2][x2]:
                        p2 += 1
                        continue
                    if d2 - turn <= d:
                        targets.add((y2, x2))
                        p2 += 1
                    break
                while p3 < len(edfp[a3]):
                    d3, x3, y3 = edfp[a3][p3]
                    if y3 >= n - turn:
                        p3 += 1
                        continue
                    if dead[y3][x3]:
                        p3 += 1
                        continue
                    if d3 - turn <= d:
                        targets.add((y3, x3))
                        p3 += 1
                    break
                for y1, x1 in targets:
                    dead[y1][x1] = True
                    killed += 1
            if killed > most_killed:
                most_killed = killed
print(most_killed)
