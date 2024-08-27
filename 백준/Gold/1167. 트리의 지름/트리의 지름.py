import os, io, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(100000)

v = int(input())
visited = [False] * (v + 1)
graph = [{} for _ in range(v + 1)]
for i in range(v):
    lst = list(map(int, input().split()))
    idx = lst[0]
    for j in range(len(lst) // 2 - 1):
        graph[idx][lst[j * 2 + 1]] = lst[j * 2 + 2]


def dfs(node, distance_from_parent):
    temp = 0
    first = 0
    second = 0
    for adj in graph[node]:
        if visited[adj]:
            continue
        visited[adj] = True
        adj_best, adj_first = dfs(adj, graph[node][adj])
        if adj_best > temp:
            temp = adj_best
        if adj_first > first:
            second, first = first, adj_first
        elif adj_first > second:
            second = adj_first
    if first + second > temp:
        temp = first + second
    return temp, first + distance_from_parent


visited[1] = True
best, one_way_best = dfs(1, 0)
if one_way_best > best:
    best = one_way_best
print(best)
