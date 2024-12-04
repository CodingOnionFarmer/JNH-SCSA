import heapq, sys

sys.setrecursionlimit(1001)


def dfs(node):
    tc = cost[node]
    ts = 1
    child_trees = []
    for child in graph[node]:
        child_tc, child_ts, child_nsc = dfs(child)
        child_trees.append((child_ts / child_tc, child_tc, child_ts))
        child_trees.extend(child_nsc)
    child_trees.sort()
    nsc = []  # not selected child
    for div, ctc, cts in child_trees:
        if div <= ts / tc:
            tc += ctc
            ts += cts
        else:
            nsc.append((div, ctc, cts))
    total_cost[node] = tc
    tree_size[node] = ts
    return tc, ts, nsc


n, r = map(int, input().split())
cost = [0] + list(map(int, input().split()))
total_cost = [0] * (n + 1)
tree_size = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
dfs(r)
q = [(tree_size[r] / total_cost[r], r)]  # 평균 비용의 역수를 넣어서 평균 비용이 비싼 것부터 뽑게
order = 1
minimal_cost = 0
while q:
    node = heapq.heappop(q)[1]
    minimal_cost += order * cost[node]
    order += 1
    for child in graph[node]:
        heapq.heappush(q, (tree_size[child] / total_cost[child], child))
print(minimal_cost)
