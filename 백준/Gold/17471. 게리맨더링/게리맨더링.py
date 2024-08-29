n = int(input())
popularity = list(map(int, input().split()))
total = sum(popularity)
graph = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    if lst[0]:
        for j in lst[1:]:
            graph[i].append(j - 1)

full = (1 << n) - 1
best = 1001
for code in range(1, (1 << n) - 1):
    groups = [set(), set()]
    for i in range(n):
        groups[code & 1].add(i)
        code >>= 1
    group0_popularity = 0
    for area in groups[0]:
        group0_popularity += popularity[area]
    diff = abs(total - (group0_popularity << 1))
    if diff >= best:
        continue
    q = [groups[0].pop()]
    visited = 1 << q[0]
    while q:
        nq = []
        for area in q:
            for connected_area in graph[area]:
                if connected_area in groups[0] and not visited & (1 << connected_area):
                    nq.append(connected_area)
                    visited |= 1 << connected_area
        q = nq
    q = [groups[1].pop()]
    visited |= 1 << q[0]
    while q:
        nq = []
        for area in q:
            for connected_area in graph[area]:
                if connected_area in groups[1] and not visited & (1 << connected_area):
                    nq.append(connected_area)
                    visited |= 1 << connected_area
        q = nq
    if visited == full:
        best = diff
        if not best:
            break
if best == 1001:
    best = -1
print(best)
