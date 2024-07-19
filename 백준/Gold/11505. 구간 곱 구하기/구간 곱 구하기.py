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
            self.tree[node] = self.tree[2 * node] * self.tree[2 * node + 1] % 1000000007

    def query1(self, index, value):
        self.arr[index] = value
        self.update(1, 0, len(self.arr) - 1, index, value)

    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return
        if start != end:
            mid = (start + end) // 2
            self.update(2 * node, start, mid, index, value)
            self.update(2 * node + 1, mid + 1, end, index, value)
            self.tree[node] = self.tree[2 * node] * self.tree[2 * node + 1] % 1000000007
            return
        self.tree[node] = value

    def query2(self, left, right):
        return self.get_mul(1, 0, len(self.arr) - 1, left, right)

    def get_mul(self, node, start, end, left, right):
        if left > end or right < start:
            return 1
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.get_mul(2 * node, start, mid, left, right) * self.get_mul(2 * node + 1, mid + 1, end, left,
                                                                              right) % 1000000007


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
segTree = SegmentTree(arr)
for i in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        segTree.query1(b - 1, c)
    else:
        print(segTree.query2(b - 1, c - 1))
