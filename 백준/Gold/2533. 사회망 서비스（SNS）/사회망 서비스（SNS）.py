import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000001)

n = int(input())
friends = {num: set() for num in range(1, n + 1)}
for edge in range(n - 1):
    u, v = map(int, input().split())
    friends[u].add(v)
    friends[v].add(u)
early_adapters = set()


def dfs(node):
    not_ea_friends = 0
    for friend in friends[node]:
        friends[friend].discard(node)
        not_ea_friends += dfs(friend)
    if not_ea_friends:
        early_adapters.add(node)
        return 0
    return 1


dfs(1)
print(len(early_adapters))
