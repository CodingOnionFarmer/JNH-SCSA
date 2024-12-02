import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def merge(lst1, lst2):
    lst = []
    l1 = len(lst1)
    l2 = len(lst2)
    i1 = i2 = 0
    while i1 < l1 and i2 < l2:
        if lst1[i1] <= lst2[i2]:
            lst.append(lst1[i1])
            i1 += 1
        else:
            lst.append(lst2[i2])
            i2 += 1
    lst.extend(lst1[i1:])
    lst.extend(lst2[i2:])
    return lst


def build(node, start, end):
    if start == end:
        mst[node] = [sequence[start]]
        return
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    build(lc, start, mid)
    build(rc | 1, mid + 1, end)
    mst[node] = merge(mst[lc], mst[rc])
    return


def binary_search(lst, number):  # 정렬된 lst에서 number보다 큰 원소의 개수
    if lst[-1] <= number:
        return 0
    l = len(lst)
    left = 0
    right = l - 1
    while left < right:
        mid = (left + right) >> 1
        if lst[mid] > number:
            right = mid
        else:
            left = mid + 1
    return l - left


def bigger_than(node, start, end, left, right, number):  # left~right 구간에서 number보다 큰 원소의 개수
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return binary_search(mst[node], number)
    mid = (start + end) >> 1
    lc = node << 1
    rc = lc | 1
    return bigger_than(lc, start, mid, left, right, number) + bigger_than(rc, mid + 1, end, left, right, number)


n = int(input())
sequence = [0] + list(map(int, input().split()))
mst = [[] for _ in range(n << 2)]  # merge sort tree
build(1, 1, n)

m = int(input())
answer = []
for _ in range(m):
    i, j, k = map(int, input().split())
    answer.append(bigger_than(1, 1, n, i, j, k))
print(*answer, sep='\n')
