n = int(input())
anthill = {}
for line in range(n):
    info = list(input().split())
    now = anthill
    for i in range(1, len(info)):
        if info[i] not in now:
            now[info[i]] = {}
        now = now[info[i]]


def dfs(depth, tree):
    for food in sorted(tree.keys()):
        print('--' * depth + food)
        dfs(depth + 1, tree[food])


dfs(0, anthill)
