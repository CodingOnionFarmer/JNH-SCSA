import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
connected = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    connected[a].append(b)
    connected[b].append(a)

for adj_nodes in connected:
    adj_nodes.sort()

dfs_route = []
bfs_route = []
dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)


def dfs(node):
    dfs_visited[node] = True
    dfs_route.append(node)
    for adj_node in connected[node]:
        if not dfs_visited[adj_node]:
            dfs(adj_node)
    return


def bfs(nodes):
    if not nodes:
        return
    next_nodes = []
    for node in nodes:
        bfs_route.append(node)
        for adj_node in connected[node]:
            if not bfs_visited[adj_node]:
                bfs_visited[adj_node] = True
                next_nodes.append(adj_node)
    bfs(next_nodes)


dfs(v)
bfs_visited[v] = True
bfs([v])

print(*dfs_route)
print(*bfs_route)
