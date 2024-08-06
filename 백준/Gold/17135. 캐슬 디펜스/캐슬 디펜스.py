# 기본적으로 생각할 것
# 사거리 조건에 맞는 적을 찾을 때, n*m 행렬의 범위 체크를 꼼꼼히 해야 한다.
# 또는 10의 사거리에 맞춰 위로 10줄, 오른쪽으로 10줄씩 0을 추가해서 padding을 쳐도 된다.
# 또는 사거리 본위로 생각하지 않고, n*m 행렬을 순회하면서 각 지점의 거리가 몇인지를 체크해둘 수 있다.

# 구현을 효율적으로 하기 위해서 여러 가지 고민을 했다.
# 궁수의 위치에 따라, 각 적의 거리와 우선순위가 달라지므로, 모두 저장해놓고 경우의 수마다 시뮬레이션으로 돌렸다.
# 이렇게까지 안 해도 시간복잡도가 발목잡지는 않는 문제이므로 쉽게 구현하는 것이 나을 수도 있다.


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
for a1 in range(m - 2):  # archer1의 x좌표
    for a2 in range(a1 + 1, m - 1):  # archer2
        for a3 in range(a2 + 1, m):  # archer3
            dead = [[False] * m for _ in range(n)]
            killed = 0
            p1 = p2 = p3 = 0  # 각 궁수가 현재 최우선 타겟으로 쏘는 적의 index
            for turn in range(n):  # turn이 1 늘 때마다 적들이 1씩 내려온다.
                if killed + 3 * (n - turn) <= most_killed:
                    break  # 앞으로 매 턴 3킬씩 해도 기록 갱신이 안 되면 가지치기한다.

                targets = set()  # 해당 turn에 쏠 적이 있는 지점들
                while p1 < len(edfp[a1]):  # 궁수1이 쏠 수 있는 적을 찾는다.
                    d1, x1, y1 = edfp[a1][p1]
                    # 현재 최고 우선순위인 적의 (turn이 0일 때의 원래)거리, x좌표, y좌표

                    if y1 >= n - turn:  # 적이 이미 성까지 내려온 경우는 넘긴다.
                        p1 += 1
                        continue

                    if dead[y1][x1]:  # 적이 이미 죽은 경우도 넘긴다.
                        p1 += 1
                        continue

                    # 지금 쏘려는 적(edfp[a1][p1]에 해당한는 적)은 반드시 유효하다.
                    # 하지만 거리가 안 닿아서 아예 못 쏠 수도 있다.
                    # 그리고 우선순위(거리)가 가장 높은(가까운) 적이므로, 이 적을 못 쏘면 다른 적도 못 쏜다.
                    # 따라서, 쏠 수 있을 경우에만 targets에 추가하고 p1을 1 늘린다.
                    if d1 - turn <= d:
                        targets.add((y1, x1))
                        p1 += 1
                    # 그리고 쏘든 못 쏘든 while문은 종료한다.
                    break

                while p2 < len(edfp[a2]):  # 궁수2, 궁수3도 똑같이 한다.
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

                # 이번 턴에 쏜 적들을 사망처리한다.
                for y1, x1 in targets:
                    dead[y1][x1] = True
                    killed += 1

            # 최고 킬수 기록시 갱신
            if killed > most_killed:
                most_killed = killed
print(most_killed)
