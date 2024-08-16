# Dijkstra
# 아이디어 : 뚫려있으면 거리0, 벽막혀있으면 거리1으로 다익스트라 돌리기

import heapq

n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(m)]
distance = [[200] * n for _ in range(m)]
q = [(0, 0, 0)]
distance[0][0] = 0
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
while q:
    cd, ci, cj = heapq.heappop(q)
    for di, dj in directions:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < m and 0 <= nj < n and cd + maze[ni][nj] < distance[ni][nj]:
            distance[ni][nj] = cd + maze[ni][nj]
            heapq.heappush(q, (cd + maze[ni][nj], ni, nj))
print(distance[m - 1][n - 1])
