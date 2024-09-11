n, m, k = map(int, input().split())
maximal_pick = (n * m + 1) >> 1
if k > maximal_pick:
    k = maximal_pick
candidates = min(k * 5 + 1, n * m)
ruby = []
for i in range(n):
    line = list(map(int, input().split()))
    for j, value in enumerate(line):
        ruby.append((value, i, j))
ruby.sort(reverse=True)
adj = [[False] * candidates for _ in range(candidates)]
for c1 in range(candidates - 1):
    v1, i1, j1 = ruby[c1]
    for c2 in range(c1 + 1, candidates):
        v2, i2, j2 = ruby[c2]
        if abs(i1 - i2) + abs(j1 - j2) == 1:
            adj[c1][c2] = True


def dfs(depth, before_idx):
    if depth == k:
        return 0
    most_value = 0
    for idx in range(before_idx + 1, candidates - (k - 1 - depth)):
        if any(adj[chosen][idx] for chosen in choose):
            continue
        choose.append(idx)
        most_value = max(most_value, ruby[idx][0] + dfs(depth + 1, idx))
        choose.pop()
    return most_value


choose = []
print(dfs(0, -1))
