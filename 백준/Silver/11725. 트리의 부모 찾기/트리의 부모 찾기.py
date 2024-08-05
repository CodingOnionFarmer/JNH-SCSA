import os, io, sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write

sys.setrecursionlimit(100001)

n = int(input())
connected = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)
parent = [i for i in range(n + 1)]
visited = [False] * (n + 1)


def dfs(node):
    for child in connected[node]:
        if not visited[child]:
            visited[child] = True
            parent[child] = node
            dfs(child)


visited[1] = True
dfs(1)
for i in range(2, n + 1):
    print(str(parent[i]) + '\n')
