from collections import deque

for _ in range(int(input())):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    build_time = [0] + list(map(int, input().split()))
    total_time = [0] * (n + 1)
    in_degree = [0] * (n + 1)
    for _ in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1
    target = int(input())
    win_time = 0
    q = deque()
    for i in range(1, n + 1):
        if not in_degree[i]:
            q.append((i, build_time[i]))
    while q:
        p, time = q.popleft()
        if p == target:
            if time > win_time:
                win_time = time
        for r in graph[p]:
            total_time[r] = max(total_time[r], time + build_time[r])
            in_degree[r] -= 1
            if not in_degree[r]:
                q.append((r, total_time[r]))
    print(win_time)
