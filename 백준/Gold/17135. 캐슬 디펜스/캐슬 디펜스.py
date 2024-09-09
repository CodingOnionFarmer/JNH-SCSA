# 언어 : PyPy3
# 메모리 : 111836KB
# 시간 : 140ms
# 시도횟수 : 1회

# 구현, 시뮬레이션, 그리디 알고리즘

n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
enemy_priority_from_column = [[] for _ in range(m)]
enemy_cnt = []

# 각 열에서 적들의 우선순위를 미리 정해 둘 수 있다. 인덱스를 하나씩 밀면서 유효한 타겟일 때만 쏘면 된다.
enemies = 0
for i in range(n - 1, -1, -1):
    enemy_cnt.append(enemies)
    for j in range(m):
        if board[i][j]:
            enemies += 1
            for c in range(m):
                enemy_priority_from_column[c].append((n - i + abs(j - c), j, n - 1 - i))
for c in range(m):
    enemy_priority_from_column[c].sort()
for r in range(n):
    enemy_cnt[r] = enemies - enemy_cnt[r]
maximal = 3 * n, enemies


def solve():
    ans = 0
    # a1 : archer1(이 서 있는 열), a1a : archer1 aiming(궁수1이 쏠 최우선 타겟의 인덱스)
    for a1 in range(m - 2):
        epc1 = enemy_priority_from_column[a1]
        for a2 in range(a1 + 1, m - 1):
            epc2 = enemy_priority_from_column[a2]
            for a3 in range(a2 + 1, m):
                epc3 = enemy_priority_from_column[a3]
                a1a = 0
                a2a = 0
                a3a = 0
                killed = 0
                dead = [0] * n
                for turn in range(n):
                    # 남은 턴 동안 매턴 3명씩 쏴도 최고기록 갱신 안 되면 가지치기
                    if killed + (n - turn) * 3 <= ans:
                        break
                    if killed + enemy_cnt[turn] <= ans:
                        break
                    shoot = []
                    while a1a < enemies:
                        # distance는 원래 거리(적이 움직이기 전)이다.
                        # i는 편의상 인덱스를 뒤집어놨다 (맨 밑이 0이다)
                        distance, j, i = epc1[a1a]

                        # 이미 지나가 버려서 못 쏘는 적은 넘김
                        if i < turn:
                            a1a += 1
                            continue

                        # 아직 안 지나갔고 유효 사거리인 적이면
                        if distance - turn <= d:
                            # 근데 이미 그 전에 쏴서 죽어있으면 넘김
                            if dead[i] & (1 << j):
                                a1a += 1
                                continue
                            # 아직 안 지나갔고 유효 사거리고 살아있는 적이면 쏘는 것을 확정하고 종료
                            if (i, j) not in shoot:
                                shoot.append((i, j))
                            a1a += 1
                            break
                        # 아직 안 지나갔는데 유효 사거리 밖인 적이어도 종료 (사거리 우선 정렬했으므로 greedy하게 가능)
                        break

                    # 궁수2, 3도 똑같이 해 준다.
                    while a2a < enemies:
                        distance, j, i = epc2[a2a]
                        if i < turn:
                            a2a += 1
                            continue
                        if distance - turn <= d:
                            if dead[i] & (1 << j):
                                a2a += 1
                                continue
                            if (i, j) not in shoot:
                                shoot.append((i, j))
                            a2a += 1
                            break
                        break

                    while a3a < enemies:
                        distance, j, i = epc3[a3a]
                        if i < turn:
                            a3a += 1
                            continue
                        if distance - turn <= d:
                            if dead[i] & (1 << j):
                                a3a += 1
                                continue
                            if (i, j) not in shoot:
                                shoot.append((i, j))
                            a3a += 1
                            break
                        break

                    # 쏜 적들은 시체가 된다.
                    for i, j in shoot:
                        dead[i] |= 1 << j
                        killed += 1

                # 시체 수가 최고기록 달성시 갱신
                if killed > ans:
                    ans = killed
                    if ans == maximal:
                        print(ans)
                        return

    print(ans)


solve()
