n, m, k = map(int, input().split())
task_matching = [0] * (m + 1)
graph = [[]] + [list(map(int, input().split()))[1:] for _ in range(n)]
staff_matched = [False] * (n + 1)


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

additional_matches = 0
while additional_matches < k:
    staff_matched = [False] * (n + 1)
    secondary_matches = 0
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
        secondary_matches += new_matches
    if not secondary_matches:
        break
    additional_matches += secondary_matches
additional_matches = min(additional_matches, k)
print(matches + additional_matches)
