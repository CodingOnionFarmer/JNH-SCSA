n = int(input())

popularity = list(map(int, input().split()))
total = sum(popularity)

graph = [0] * n
for i in range(n):
    lst = list(map(int, input().split()))
    if lst[0]:
        for j in lst[1:]:
            graph[i] |= 1 << j - 1

full = (1 << n) - 1
best = 1001

for code in range(1, 1 << n - 1):
    code0 = full - code
    group1_popularity = sum(popularity[i] for i in range(n) if (1 << i) & code)
    diff = abs(total - (group1_popularity << 1))

    if diff >= best:
        continue

    q = 1 << n - 1
    visited = 0
    while q:
        nq = 0
        for i in range(n):
            if q & (1 << i):
                visited |= 1 << i
                nq |= graph[i]
        nq &= code0
        nq &= full - visited
        q = nq

    if visited != code0:
        continue

    q = 1
    while not q & code:
        q <<= 1
    while q:
        nq = 0
        for i in range(n):
            if q & (1 << i):
                visited |= 1 << i
                nq |= graph[i]
        nq &= code
        nq &= full - visited
        q = nq

    if visited == full:
        best = diff
        if best < 2:
            break

if best == 1001:
    best = -1
print(best)
