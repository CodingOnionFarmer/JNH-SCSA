# Dijkstra

# N*M 시간만큼 걸릴 수 있으므로 완전탐색 불가능


import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
when_can_go = [[] for _ in range(n + 1)]
q = [(0, 1)]
distance = [n * m + 1] * (n + 1)
distance[1] = 0
for time in range(m):
    a, b = map(int, input().split())
    when_can_go[a].append((b, time))
    when_can_go[b].append((a, time))
while q:
    ct, ca = heapq.heappop(q)
    if ct > distance[ca]:
        continue
    pt = ct % m
    for na, t in when_can_go[ca]:
        if pt > t:
            t += m
        nt = ct + t - pt + 1
        if nt < distance[na]:
            distance[na] = nt
            heapq.heappush(q, (nt, na))
print(distance[n])
