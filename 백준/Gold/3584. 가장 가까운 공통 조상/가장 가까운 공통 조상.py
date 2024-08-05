# LCA 알고리즘 (Naive Version)


import sys

input = sys.stdin.readline

sys.setrecursionlimit(10001)


def dfs(node, depth):
    for child in children[node]:
        if not visited[child]:
            visited[child] = True
            depths[child] = depth + 1
            dfs(child, depth + 1)


def find_lca(node1, node2):
    if node1 == node2:
        return node1
    if depths[node1] == depths[node2]:
        return find_lca(parent[node1], parent[node2])
    if depths[node1] < depths[node2]:
        node1, node2 = node2, node1
    return find_lca(parent[node1], node2)


t = int(input())
for tc in range(t):
    n = int(input())
    parent = [i for i in range(n + 1)]
    depths = [-1] * (n + 1)
    visited = [False] * (n + 1)
    children = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        n1, n2 = map(int, input().split())
        parent[n2] = n1
        children[n1].append(n2)
    for node in range(1, n + 1):
        if parent[node] == node:
            root = node
            break
    dfs(root, 0)
    a, b = map(int, input().split())
    print(find_lca(a, b))
