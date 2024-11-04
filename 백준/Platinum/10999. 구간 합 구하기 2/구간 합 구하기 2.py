# lazy propagation

import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m, k = map(int, input().split())
numbers = [0] + [int(input()) for _ in range(n)]
seg_sum = [0] * (n << 2)
lazy = [0] * (n << 2)


def build(start, end, node):
    if start == end:
        seg_sum[node] = numbers[start]
        return
    mid = (start + end) >> 1
    left_child = node << 1
    right_child = left_child | 1
    build(start, mid, left_child)
    build(mid + 1, end, right_child)
    seg_sum[node] = seg_sum[left_child] + seg_sum[right_child]


def propagate(start, end, node):
    change = lazy[node]
    lazy[node] = 0
    if start == end:
        numbers[start] += change
        return
    left_child = node << 1
    right_child = left_child | 1
    lazy[left_child] += change
    lazy[right_child] += change
    return


def find_sum(start, end, node, left, right):  # start, end는 node가 커버하는 범위, left,right는 찾으려는 범위이다.
    if end < left or start > right:
        return 0
    change = lazy[node]
    if change:
        seg_sum[node] += change * (end - start + 1)
        propagate(start, end, node)
    if left <= start and end <= right:
        return seg_sum[node]
    if start == end:
        return numbers[left]
    mid = (start + end) >> 1
    left_child = node << 1
    right_child = left_child | 1
    return find_sum(start, mid, left_child, left, right) + find_sum(mid + 1, end, right_child, left, right)


def update(start, end, node, left, right, value):  # start, end는 node가 커버하는 범위, left, right는 update하려는 범위
    change = lazy[node]
    if change:
        seg_sum[node] += change * (end - start + 1)
        propagate(start, end, node)
    if end < left or start > right:
        return
    if left <= start and end <= right:
        seg_sum[node] += value * (end - start + 1)
        if start != end:
            lazy[node << 1] += value
            lazy[node << 1 | 1] += value
        return
    mid = (start + end) >> 1
    left_child = node << 1
    right_child = left_child | 1
    update(start, mid, left_child, left, right, value)
    update(mid + 1, end, right_child, left, right, value)
    seg_sum[node] = seg_sum[left_child] + seg_sum[right_child]


build(1, n, 1)
answer = []
for _ in range(m + k):
    query = tuple(map(int, input().split()))
    if query[0] == 1:
        b, c, d = query[1:]
        update(1, n, 1, b, c, d)
    else:
        b, c = query[1:]
        answer.append(find_sum(1, n, 1, b, c))
print(*answer, sep='\n')
