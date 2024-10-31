import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m, k = map(int, input().split())
numbers = [0] + [int(input()) for _ in range(n)]
seg_sum = [0] * (n << 2)


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


def find_sum(start, end, node, left, right):  # start, end는 찾으려는 범위이고, left,right는 node가 커버하는 범위이다.
    if right < start or left > end:
        return 0
    if start <= left and right <= end:
        return seg_sum[node]
    if left == right:
        return numbers[left]
    mid = (left + right) >> 1
    left_child = node << 1
    right_child = left_child | 1
    return find_sum(start, end, left_child, left, mid) + find_sum(start, end, right_child, mid + 1, right)


def update(start, end, node, idx, value):
    if start > idx or end < idx:
        return
    if start == end:
        seg_sum[node] = value
        return
    mid = (start + end) >> 1
    left_child = node << 1
    right_child = left_child | 1
    update(start, mid, left_child, idx, value)
    update(mid + 1, end, right_child, idx, value)
    seg_sum[node] = seg_sum[left_child] + seg_sum[right_child]


build(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        numbers[b] = c
        update(1, n, 1, b, c)
    else:
        print(find_sum(b, c, 1, 1, n))
