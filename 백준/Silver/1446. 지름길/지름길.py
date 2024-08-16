# 브루트포스, 구현
# 비트마스킹

n, d = map(int, input().split())
path = [tuple(map(int, input().split())) for _ in range(n)]
path.sort()
best = d
for code in range(1 << n):
    now = 0
    moved = 0
    valid = True
    for i in range(n):
        if code & (1 << i):
            s, e, l = path[i]
            if s < now or e > d:
                valid = False
                continue
            moved += s - now
            moved += l
            now = e
    moved += d - now
    if valid and moved < best:
        best = moved
print(best)
