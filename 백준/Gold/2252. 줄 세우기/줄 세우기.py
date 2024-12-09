from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1
q = deque()
for i in range(1, n + 1):
    if not in_degree[i]:
        q.append(i)
while q:
    p = q.popleft()
    print(p, end=' ')
    for r in graph[p]:
        in_degree[r] -= 1
        if not in_degree[r]:
            q.append(r)
