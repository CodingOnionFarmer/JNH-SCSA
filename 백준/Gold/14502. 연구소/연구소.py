# 완전탐색, BFS

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
board = [int(x) for _ in range(n) for x in input().split()]
size = n * m
adj = [[(i + di) * m + j + dj for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < m] for i in range(n) for j
       in range(m)]

safe = []
fire = []
original_visited = [False] * size
for idx, num in enumerate(board):
    if num == 2:
        fire.append(idx)
        original_visited[idx] = True
    elif not num:
        safe.append(idx)

isz = len(safe)  # initial safe zone
isz_m3 = isz - 3
most = 0
for i in range(isz - 2):
    si = safe[i]
    board[si] = 1
    for j in range(i + 1, isz - 1):
        sj = safe[j]
        board[sj] = 1
        for k in range(j + 1, isz):
            sk = safe[k]
            board[sk] = 1
            temp = isz_m3
            q = fire[:]
            visited = original_visited[:]
            visited[si] = True
            visited[sj] = True
            visited[sk] = True

            while q:
                nq = []
                for cp in q:
                    for np in adj[cp]:
                        if not visited[np] and not board[np]:
                            visited[np] = True
                            temp -= 1
                            nq.append(np)
                q = nq
            if temp > most:
                most = temp
            board[safe[k]] = 0
        board[safe[j]] = 0
    board[safe[i]] = 0

print(most)
