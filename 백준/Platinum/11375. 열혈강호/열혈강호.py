# 이분 매칭
# 홉크로프트-카프 알고리즘

n, m = map(int, input().split())
staff_level = [0] * (n + 1)
task_matching = [0] * (m + 1)
graph = [[]]
graph_rev = [[] for _ in range(m + 1)]
for s in range(1, n + 1):
    graph.append(list(map(int, input().split()))[1:])
    for t in graph[s]:
        graph_rev[t].append(s)
edges = [[False] * (m + 1) for _ in range(n + 1)]
remaining_staff = {s for s in range(1, n + 1)}


def dfs(s, level):
    vs[s] = True
    for t in graph[s]:
        if vt[t]:
            continue
        ns = task_matching[t]
        if vs[ns]:
            continue
        if not ns:
            vt[t] = True
            task_matching[t] = s
            return True
        vt[t] = True
        if dfs(ns, level + 1):
            task_matching[t] = s
            return True
    return False


match = 0
while True:
    vs = [False] * (n + 1)
    vt = [False] * (m + 1)
    q = [s for s in remaining_staff]
    for s in q:
        vs[s] = True
    level = 0
    while q:
        tq = []
        level += 1
        for s in q:
            for t in graph[s]:
                if vt[t]:
                    continue
                vt[t] = True
                tq.append(t)
        q = []
        for t in tq:
            for s in graph_rev[t]:
                if vs[s]:
                    continue
                vs[s] = True
                staff_level[s] = level
                q.append(s)
    vs = [False] * (n + 1)
    vt = [False] * (m + 1)
    new_vs = set()
    for s in remaining_staff:
        if dfs(s, 0):
            match += 1
            new_vs.add(s)
    if not new_vs:
        print(match)
        break
    remaining_staff -= new_vs
