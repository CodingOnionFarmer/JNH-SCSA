n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
second_rev = [0] * (n + 1)
for i, s in enumerate(second):
    second_rev[s] = i + 1
third = list(map(int, input().split()))
third_rev = [0] * (n + 1)
for i, s in enumerate(third):
    third_rev[s] = i + 1

seg = [n] * (n << 2)


def update(node, start, end, idx, value):
    if idx < start or end < idx:
        return
    if start == end:
        seg[node] = value
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    update(lc, start, mid, idx, value)
    update(rc, mid + 1, end, idx, value)
    seg[node] = min(seg[lc], seg[rc])


def query(node, start, end, left, right):
    if right < start or end < left:
        return n
    if left <= start and end <= right:
        return seg[node]
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    return min(query(lc, start, mid, left, right), query(rc, mid + 1, end, left, right))


answer = 0
for student in first:
    sr = second_rev[student]
    tr = third_rev[student]
    update(1, 1, n, sr, tr)
    if query(1, 1, n, 1, sr - 1) >= tr:
        answer += 1
print(answer)
