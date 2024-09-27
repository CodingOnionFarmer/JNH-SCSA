n = int(input())
friend = [[] for _ in range(n)]
while True:
    a, b = map(int, input().split())
    if a == -1:
        break
    friend[a - 1].append(b - 1)
    friend[b - 1].append(a - 1)

best = 51
candidates = []
for i in range(n):
    visited = [False] * n
    q = [i]
    visited[i] = True
    step = -1
    while q:
        step += 1
        nq = []
        for p in q:
            for f in friend[p]:
                if visited[f]:
                    continue
                visited[f] = True
                nq.append(f)
        q = nq
    if step < best:
        best = step
        candidates = [i + 1]
    elif step == best:
        candidates.append(i + 1)

print(best, len(candidates))
print(*candidates)
