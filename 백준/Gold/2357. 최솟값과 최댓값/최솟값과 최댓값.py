import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
numbers = [0] + [int(input()) for _ in range(n)]
seg_min = [0] * (n << 2)
seg_max = [0] * (n << 2)


def build(start, end, node):
    if start == end:
        seg_min[node] = seg_max[node] = numbers[start]
        return
    mid = (start + end) >> 1
    left_child = node << 1
    right_child = left_child | 1
    build(start, mid, left_child)
    build(mid + 1, end, right_child)
    seg_min[node] = min(seg_min[left_child], seg_min[right_child])
    seg_max[node] = max(seg_max[left_child], seg_max[right_child])


def find_minmax(start, end, node, left, right):  # start, end는 찾으려는 범위이고, left,right는 node가 커버하는 범위이다.
    if right < start or left > end:
        return 1000000001, 0
    if start <= left and right <= end:
        return seg_min[node], seg_max[node]
    if left == right:
        return numbers[left]
    mid = (left + right) >> 1
    left_child = node << 1
    right_child = left_child | 1
    left_min, left_max = find_minmax(start, end, left_child, left, mid)
    right_min, right_max = find_minmax(start, end, right_child, mid + 1, right)
    return min(left_min, right_min), max(left_max, right_max)


build(1, n, 1)
for _ in range(m):
    a, b = map(int, input().split())
    print(*find_minmax(a, b, 1, 1, n))
