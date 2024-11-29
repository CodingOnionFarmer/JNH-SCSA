n, m = map(int, input().split())
task_matching = [0] * (m + 1)
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]


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


matches = 0
for _ in range(2):
    staff_matched = [False] * (n + 1)
    while True:
        new_matches = 0
        vs = [False] * (n + 1)
        vt = [False] * (m + 1)
        for s in range(1, n + 1):
            if staff_matched[s]:
                continue
            if dfs(s, 0):
                new_matches += 1
                staff_matched[s] = True
        if not new_matches:
            break
        matches += new_matches
print(matches)
