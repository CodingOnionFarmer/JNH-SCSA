n, m = map(int, input().split())
n -= 1
m -= 1
board = [0] * (n * m)
input()
rsp, bsp, ep = 0, 0, 0

for i in range(n):
    line = input()
    for j in range(m):
        char = line[j + 1]
        if char != '.':
            if char == 'B':
                bsp = i * m + j
            elif char == 'R':
                rsp = i * m + j
            elif char == 'O':
                ep = i * m + j
                board[ep] = 2
            else:
                board[i * m + j] = 1


def move(fp, sp, d):  # d가 1:오른쪽, -1:왼쪽, m:아래쪽, -m:위쪽
    while not board[fp]:
        fp += d
    if board[fp] == 1:
        fp -= d
        board[fp] = 1
    while not board[sp]:
        sp += d
    if board[sp] == 1:
        sp -= d
    if board[fp] == 1:
        board[fp] = 0
    return fp, sp


visited = [[False] * (n * m) for _ in range(n * m)]  # red blue 순
visited[rsp][bsp] = True
for i in range(n * m):
    visited[i][i] = True
    visited[i][ep] = True
moved = 0
goal_in = False
q = [(rsp, bsp, 0), (rsp, bsp, 1)]  # 0은 수직 1은 수평

while q and not goal_in:
    if moved == 10:
        break
    moved += 1
    nq = []
    for rcp, bcp, cvh in q:
        # 1은 수평 이동
        if cvh:
            # 빨강이 더 오른쪽
            if rcp % m > bcp % m:
                # 오른쪽
                rnp, bnp = move(rcp, bcp, 1)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 0))

                # 왼쪽
                bnp, rnp = move(bcp, rcp, -1)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 0))

            # 빨강이 더 왼쪽
            else:
                # 왼쪽
                rnp, bnp = move(rcp, bcp, -1)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 0))

                # 오른쪽
                bnp, rnp = move(bcp, rcp, 1)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 0))

        # 0은 수직 이동
        else:
            # 빨강이 더 아래쪽
            if rcp > bcp:
                # 아래쪽
                rnp, bnp = move(rcp, bcp, m)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 1))

                # 위쪽
                bnp, rnp = move(bcp, rcp, -m)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 1))

            # 빨강이 더 위쪽
            else:
                # 위쪽
                rnp, bnp = move(rcp, bcp, -m)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 1))

                # 아래쪽
                bnp, rnp = move(bcp, rcp, m)
                if not visited[rnp][bnp]:
                    if rnp == ep:
                        goal_in = True
                        break
                    visited[rnp][bnp] = True
                    nq.append((rnp, bnp, 1))
    q = nq

if not goal_in:
    moved = -1
print(moved)
