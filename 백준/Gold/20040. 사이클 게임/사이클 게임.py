import sys


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    p, q = find(x), find(y)
    parent[max(p, q)] = parent[min(p, q)]


v, e = map(int, sys.stdin.readline().split())
arr = []
parent = [i for i in range(v + 1)]
end = 0
for i in range(e):
    a, b = map(int, sys.stdin.readline().split())
    if find(a) == find(b):
        end = i + 1
        break
    else:
        union(a, b)
print(end)
