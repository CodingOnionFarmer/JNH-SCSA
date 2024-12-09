import sys


def find(x):
    px = parent[x]
    if px == x:
        return px
    ppx = find(px)
    parent[x] = ppx
    return ppx


def union(x, y):
    p, q = find(x), find(y)
    parent[max(p, q)] = parent[min(p, q)]


v, e = map(int, input().split())
arr = []
parent = [i for i in range(v + 1)]
for i in range(e):
    a, b, cost = map(int, sys.stdin.readline().split())
    arr.append((cost, a, b))
arr.sort()
result = 0
cnt = 0
for cost, a, b in arr:
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        if cnt == v - 1:
            break
        result += cost
print(result)
