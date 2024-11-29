n, m, k = map(int, input().split())
jewel_islands = [int(input()) for _ in range(k)]
# is_jewel_in_1st_island = 1 in jewel_islands
can_go_with_limit_weight = [0] * (n + 1)
bridges_by_weight_limit = [[] for _ in range(k + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    # if is_jewel_in_1st_island:
    #     if a == 1 or b == 1:
    #         c += 1
    if c >= k:
        c = k
    bridges_by_weight_limit[c].append((a, b))

head = [i for i in range(n + 1)]


def find(x):
    hx = head[x]
    if hx == x:
        return x
    head[x] = find(hx)
    return head[x]


def union(x, y):
    hx, hy = find(x), find(y)
    if hx <= hy:
        head[hy] = hx
    else:
        head[hx] = hy
    return


for limit in range(k, 0, -1):
    for a, b in bridges_by_weight_limit[limit]:
        union(a, b)
    for i in jewel_islands:
        if not can_go_with_limit_weight[i] and find(i) == 1:
            can_go_with_limit_weight[i] = limit

limit_weight_for_jewel_islands = sorted([can_go_with_limit_weight[i] for i in jewel_islands])
get = 0
for limit in limit_weight_for_jewel_islands:
    if limit >= get + 1:
        get += 1
print(get)
