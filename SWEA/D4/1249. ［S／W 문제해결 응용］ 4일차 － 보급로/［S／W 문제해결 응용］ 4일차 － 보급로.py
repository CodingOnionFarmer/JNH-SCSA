# BFS


INF = 90001
wall = 90002
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(n):
        line = input()
        for char in line:
            board.append(int(char))
        board.append(wall)
    board.extend([wall] * n)
    n += 1
    directions = (1, n, -n, -1)
    distance = [INF] * (n * n)
    q = {0}
    distance[0] = 0
    while q:
        nq = set()
        for c in q:
            ct = distance[c]
            for d in directions:
                nn = c + d
                nt = ct + board[nn]
                if nt < distance[nn]:
                    distance[nn] = nt
                    nq.add(nn)
        q = nq
    print(f'#{tc} {distance[n * (n - 1) - 2]}')
