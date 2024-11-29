# 이분 매칭
# 홉크로프트-카프 알고리즘

n, m = map(int, input().split())
task_matching = [0] * (m + 1)
graph = [[]] + [list(map(int,input().split()))[1:] for _ in range(n)]
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
    new_vs = set()
    for s in remaining_staff:
        if dfs(s, 0):
            match += 1
            new_vs.add(s)
    if not new_vs:
        print(match)
        break
    remaining_staff -= new_vs
