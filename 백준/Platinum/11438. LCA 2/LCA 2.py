import sys

input = sys.stdin.readline
print = sys.stdout.write

sys.setrecursionlimit(100001)
n = int(input())
parents = [[] for _ in range(n + 1)]
depths = [-1] * (n + 1)
checked = [False] * (n + 1)
connected = [[] for _ in range(n + 1)]
for i in range(n - 1):
    n1, n2 = map(int, input().split())
    connected[n1].append(n2)
    connected[n2].append(n1)


def dfs(node, depth):
    checked[node] = True
    depths[node] = depth
    for node_ in connected[node]:
        if not checked[node_]:
            parents[node_].append(node)
            dfs(node_, depth + 1)


def build_binary_parents():
    parents[1].append(1)
    dfs(1, 0)
    max_depth = max(depths)
    log_depth = 0
    depth_check = 1
    while depth_check < max_depth:
        log_depth += 1
        depth_check <<= 1
    for d in range(log_depth):
        for node in range(1, n + 1):
            parents[node].append(parents[parents[node][d]][d])


def find_lca(node1, node2):
    if node1 == node2:
        return node1
    if depths[node1] == depths[node2]:
        if parents[node1][0] == parents[node2][0]:
            return parents[node1][0]
        if parents[node1][1] == parents[node2][1]:
            return parents[node1][1]
        for d in range(2, len(parents[node1])):
            if parents[node1][d] == parents[node2][d]:
                return find_lca(parents[node1][d - 1], parents[node2][d - 1])
    if depths[node1] < depths[node2]:
        node1, node2 = node2, node1
    dd = depths[node1] - depths[node2]
    if dd == 1:
        return find_lca(parents[node1][0], node2)
    if dd <= 3:
        return find_lca(parents[node1][1], node2)
    if dd == 4:
        return find_lca(parents[node1][2], node2)
    for d in range(2, len(parents[node1])):
        if depths[parents[node1][d]] <= depths[node2]:
            return find_lca(parents[node1][d - 1], node2)
    return 0


build_binary_parents()
m = int(input())
for i in range(m):
    n1, n2 = map(int, input().split())
    print(str(find_lca(n1, n2)) + '\n')
