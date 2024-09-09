n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
enemy_priority_from_column = [[] for _ in range(m)]
enemy_cnt = []
enemies = 0
for i in range(n - 1, -1, -1):
    enemy_cnt.append(enemies)
    for j in range(m):
        if board[i][j]:
            enemies += 1
            for c in range(m):
                enemy_priority_from_column[c].append((n - i + abs(j - c), j * n + n - 1 - i))
for c in range(m):
    enemy_priority_from_column[c].sort()
for r in range(n):
    enemy_cnt[r] = enemies - enemy_cnt[r]
maximal = 3 * n, enemies


def solve():
    ans = 0
    for a1 in range(m - 2):
        epc1 = enemy_priority_from_column[a1]
        for a2 in range(a1 + 1, m - 1):
            epc2 = enemy_priority_from_column[a2]
            for a3 in range(a2 + 1, m):
                epc3 = enemy_priority_from_column[a3]
                a1a = 0
                a2a = 0
                a3a = 0
                dead = set()
                for turn in range(n):
                    if len(dead) + (n - turn) * 3 <= ans:
                        break
                    if len(dead) + enemy_cnt[turn] <= ans:
                        break
                    shoot = set()
                    while a1a < enemies:
                        distance, position = epc1[a1a]
                        if position % n < turn or position in dead:
                            a1a += 1
                            continue
                        if distance - turn <= d:
                            shoot.add(position)
                            a1a += 1
                            break
                        break
                    while a2a < enemies:
                        distance, position = epc2[a2a]
                        if position % n < turn or position in dead:
                            a2a += 1
                            continue
                        if distance - turn <= d:
                            shoot.add(position)
                            a2a += 1
                            break
                        break
                    while a3a < enemies:
                        distance, position = epc3[a3a]
                        if position % n < turn or position in dead:
                            a3a += 1
                            continue
                        if distance - turn <= d:
                            shoot.add(position)
                            a3a += 1
                            break
                        break
                    dead |= shoot
                if len(dead) > ans:
                    ans = len(dead)
                    if ans == maximal:
                        print(ans)
                        return

    print(ans)


solve()
