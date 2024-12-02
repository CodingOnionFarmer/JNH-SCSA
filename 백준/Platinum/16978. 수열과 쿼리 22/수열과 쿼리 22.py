import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def build(node, start, end):
    if start == end:
        seg[node] = numbers[start]
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    build(lc, start, mid)
    build(rc, mid + 1, end)
    seg[node] = seg[lc] + seg[rc]


def find_sum(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return seg[node]
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    return find_sum(lc, start, mid, left, right) + find_sum(rc, mid + 1, end, left, right)


def update(node, start, end, idx, value):
    if start > idx or end < idx:
        return
    if start == end:
        seg[node] = value
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    update(lc, start, mid, idx, value)
    update(rc, mid + 1, end, idx, value)
    seg[node] = seg[lc] + seg[rc]


n = int(input())
numbers = [0] + list(map(int, input().split()))
seg = [0] * (n << 2)
build(1, 1, n)

query1 = []
query2 = []
q2_idx = 0
m = int(input())
for _ in range(m):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        query1.append(query[1:])
    else:
        query2.append(query[1:] + (q2_idx,))
        q2_idx += 1
answer = [0] * q2_idx
query2.sort()
applied_updates = 0
for k, i, j, qi in query2:
    while applied_updates < k:
        idx, v = query1[applied_updates]
        update(1, 1, n, idx, v)
        applied_updates += 1
    answer[qi] = find_sum(1, 1, n, i, j)
print(*answer, sep='\n')
