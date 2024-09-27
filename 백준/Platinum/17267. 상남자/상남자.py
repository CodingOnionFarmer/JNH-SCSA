n, m = map(int, input().split())
l, r = map(int, input().split())
board = [list(map(int, input())) + [1] for _ in range(n)]
groups_adj_left = [set(), set(), set()]
groups_adj_right = [set(), set(), set()]
groups_size = [0, 0, 0]
group_num = 3
si, sj = 0, 0
group = False
for j in range(m):
    i = 0
    if group:
        group = False
        group_num += 1
    while i < n:
        if board[i][j]:
            if board[i][j] == 2:
                board[i][j] = 0
                si, sj = i, j
            else:
                if group:
                    group = False
                    group_num += 1
                i += 1
                continue
        if not group:
            group = True
            groups_adj_left.append(set())
            groups_adj_right.append(set())
            groups_size.append(0)
        board[i][j] = group_num
        groups_size[group_num] += 1
        left = board[i][j - 1]
        if left >= 3:
            groups_adj_right[left].add(group_num)
            groups_adj_left[group_num].add(left)

        i += 1

sg = board[si][sj]
visited = [False] * len(groups_adj_left)
q = [(sg, l, r)]
visited[sg] = True
area = groups_size[sg]
while q:
    nq = []
    for cg, cl, cr in q:
        if cl:
            for lg in groups_adj_left[cg]:
                if visited[lg]:
                    continue
                visited[lg] = True
                area += groups_size[lg]
                nq.append((lg, cl - 1, cr))
        if cr:
            for rg in groups_adj_right[cg]:
                if visited[rg]:
                    continue
                visited[rg] = True
                area += groups_size[rg]
                nq.append((rg, cl, cr - 1))
    q = nq

print(area)
