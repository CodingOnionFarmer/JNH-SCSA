import sys

input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())
    si, sj = map(int, input().split())
    store_and_festival = [tuple(map(int, input().split())) for _ in range(n + 1)]
    ei, ej = store_and_festival[-1]
    if abs(si - ei) + abs(sj - ej) <= 1000:
        print('happy')
        continue
    visited = [False] * (n + 1)
    connected = [[] for _ in range(n + 1)]
    can_go = []
    for i in range(n):
        x1, y1 = store_and_festival[i]
        if abs(x1 - si) + abs(y1 - sj) <= 1000:
            can_go.append(i)
            visited[i] = True
        for j in range(i + 1, n + 1):
            x2, y2 = store_and_festival[j]
            if abs(x1 - x2) + abs(y1 - y2) <= 1000:
                connected[i].append(j)
                connected[j].append(i)
    while not visited[n] and can_go:
        next_go = []
        for store in can_go:
            for adj in connected[store]:
                if not visited[adj]:
                    visited[adj] = True
                    next_go.append(adj)
        can_go = next_go
    if visited[n]:
        print('happy')
    else:
        print('sad')
