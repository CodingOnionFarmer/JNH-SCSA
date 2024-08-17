# Dijkstra

# N*M 시간만큼 걸릴 수 있으므로 완전탐색 불가능


import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
when_can_go = [{} for _ in range(n + 1)]
q = [(0, 1)]
distance = [n * m + 1] * (n + 1)
distance[1] = 0
for time in range(m):
    a, b = map(int, input().split())
    if b in when_can_go[a]:
        when_can_go[a][b].append(time)
        when_can_go[b][a].append(time)
    else:
        when_can_go[a][b] = [time]
        when_can_go[b][a] = [time]
while q:
    ct, ca = heapq.heappop(q)
    if ct > distance[ca]:
        continue
    pt = ct % m
    for na in when_can_go[ca]:
        start = 0
        end = len(when_can_go[ca][na]) - 1
        if pt > when_can_go[ca][na][end]:
            nt = ct + when_can_go[ca][na][0] + 1 - pt + m
        else:
            while end > start:
                mid = (start + end) >> 1
                if when_can_go[ca][na][mid] < pt:
                    start = mid + 1
                else:
                    end = mid
            nt = ct + when_can_go[ca][na][end] + 1 - pt
        if nt < distance[na]:
            distance[na] = nt
            heapq.heappush(q, (nt, na))
print(distance[n])
