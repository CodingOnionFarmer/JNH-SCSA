n, m, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
edfp = [[] for _ in range(m)]
for i in range(n):
    for j in range(m):
        if board[i][j]:
            for k in range(j):
                edfp[k].append((n - i + j - k, j, i))
            for k in range(j, m):
                edfp[k].append((n - i + k - j, j, i))
for j in range(m):
    edfp[j].sort()

most_killed = 0
for a1 in range(m - 2):
    for a2 in range(a1 + 1, m - 1):
        for a3 in range(a2 + 1, m):
            dead = set()
            killed = 0
            p1 = p2 = p3 = 0
            for turn in range(n):
                if killed + 3 * (n - turn) <= most_killed:
                    break

                targets = set()
                while p1 < len(edfp[a1]):
                    d1, x1, y1 = edfp[a1][p1]

                    if y1 >= n - turn:
                        p1 += 1
                        continue

                    if (y1, x1) in dead:
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
                    if (y2, x2) in dead:
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
                    if (y3, x3) in dead:
                        p3 += 1
                        continue
                    if d3 - turn <= d:
                        targets.add((y3, x3))
                        p3 += 1
                    break

                for y1, x1 in targets:
                    dead.add((y1, x1))
                    killed += 1

            if killed > most_killed:
                most_killed = killed
print(most_killed)
