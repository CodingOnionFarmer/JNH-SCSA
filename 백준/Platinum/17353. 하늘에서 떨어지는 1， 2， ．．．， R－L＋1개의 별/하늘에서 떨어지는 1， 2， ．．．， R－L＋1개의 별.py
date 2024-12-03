import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def build(node, start, end):
    if start == end:
        seg[node] = stars[start]
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    build(lc, start, mid)
    build(rc, mid + 1, end)
    seg[node] = seg[lc] + seg[rc]


def propagate(node, start, end):
    change, first = lazy[node]
    lazy[node] = [0, 0]
    if start == end:
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    lazy[lc][0] += change
    lazy[lc][1] += first
    lazy[rc][0] += change
    lazy[rc][1] += first + change * (mid + 1 - start)
    return


def find_sum(node, start, end, point):
    if start > point or end < point:
        return 0
    change, first = lazy[node]
    if change:
        length = end + 1 - start
        seg[node] += first * length + change * length * (length - 1) // 2
        propagate(node, start, end)
    if start >= point >= end:
        return seg[node]
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    return find_sum(lc, start, mid, point) + find_sum(rc, mid + 1, end, point)


def update(node, start, end, left, right):
    change, first = lazy[node]
    length = end + 1 - start
    if change:
        seg[node] += first * length + change * length * (length - 1) // 2
        propagate(node, start, end)
    if end < left or start > right:
        return
    lc = node << 1
    rc = lc | 1
    mid = (start + end) >> 1
    if left <= start and end <= right:
        seg[node] += length * (start - left + 1) + length * (length - 1) // 2
        if start != end:
            lazy[lc][0] += 1
            lazy[lc][1] += start - left + 1
            lazy[rc][0] += 1
            lazy[rc][1] += mid - left + 2
        return
    update(lc, start, mid, left, right)
    update(rc, mid + 1, end, left, right)
    seg[node] = seg[lc] + seg[rc]


n = int(input())
stars = [0] + list(map(int, input().split()))
seg = [0] * (n << 2)
lazy = [[0, 0] for _ in range(n << 2)]
build(1, 1, n)

q = int(input())
answer = []
for _ in range(q):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        update(1, 1, n, *query[1:])
    else:
        answer.append(find_sum(1, 1, n, query[1]))
print(*answer, sep='\n')
