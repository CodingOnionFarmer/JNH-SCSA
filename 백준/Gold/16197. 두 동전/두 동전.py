directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m = map(int, input().split())
size = n * m
board = []
for i in range(n):
    board.extend(list(input()))

coins = []
for i in range(size):
    if board[i] == 'o':
        board[i] = '.'
        coins.append(i)

visited = [[False] * size for _ in range(size)]
c1, c2 = coins[0], coins[1]
visited[c1][c2] = True


def solve():
    button = 0
    q = [(c1, c2)]
    while q and button < 10:
        button += 1
        nq = []
        for p1, p2 in q:
            i1, j1 = p1 // m, p1 % m
            i2, j2 = p2 // m, p2 % m
            for di, dj in directions:
                out = 0
                np1, np2 = 0, 0
                ni1, nj1 = i1 + di, j1 + dj
                ni2, nj2 = i2 + di, j2 + dj
                if 0 <= ni1 < n and 0 <= nj1 < m:
                    np1 = ni1 * m + nj1
                else:
                    out += 1

                if 0 <= ni2 < n and 0 <= nj2 < m:
                    np2 = ni2 * m + nj2
                else:
                    out += 1

                if out == 1:
                    print(button)
                    return
                if out == 2:
                    continue

                if board[np1] == '#':
                    np1 = p1
                if board[np2] == '#':
                    np2 = p2
                if np1 == np2:
                    continue

                if not visited[np1][np2]:
                    visited[np1][np2] = True
                    nq.append((np1, np2))
        q = nq
    print(-1)
    return


solve()
