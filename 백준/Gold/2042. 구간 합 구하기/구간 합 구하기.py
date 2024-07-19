import sys

input = sys.stdin.readline


def print(something):
    sys.stdout.write(str(something) + '\n')


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def query1(self, index, value):
        diff = value - self.arr[index]
        self.arr[index] = value
        self.update(1, 0, len(self.arr) - 1, index, diff)

    def update(self, node, start, end, index, diff):
        if index < start or index > end:
            return
        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(2 * node, start, mid, index, diff)
            self.update(2 * node + 1, mid + 1, end, index, diff)

    def query2(self, left, right):
        return self.get_sum(1, 0, len(self.arr) - 1, left, right)

    def get_sum(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.get_sum(2 * node, start, mid, left, right) + self.get_sum(2 * node + 1, mid + 1, end, left, right)


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
segTree = SegmentTree(arr)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        segTree.query1(b - 1, c)
    else:
        print(segTree.query2(b - 1, c - 1))
