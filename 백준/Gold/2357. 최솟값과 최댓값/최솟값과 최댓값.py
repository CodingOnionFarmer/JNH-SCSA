import sys

input = sys.stdin.readline


def print(ans):
    sys.stdout.write(str(ans[0]) + ' ' + str(ans[1]) + '\n')


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [[0, 0] for _ in range(4 * len(arr))]
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node][0] = self.arr[start]
            self.tree[node][1] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node][0] = min(self.tree[2 * node][0], self.tree[2 * node + 1][0])
            self.tree[node][1] = max(self.tree[2 * node][1], self.tree[2 * node + 1][1])

    def query(self, left, right):
        return self.get_min(1, 0, len(self.arr) - 1, left, right), self.get_max(1, 0, len(self.arr) - 1, left, right)

    def get_min(self, node, start, end, left, right):
        if left > end or right < start:
            return 1000000001
        if left <= start and right >= end:
            return self.tree[node][0]
        mid = (start + end) // 2
        return min(self.get_min(2 * node, start, mid, left, right),
                   self.get_min(2 * node + 1, mid + 1, end, left, right))

    def get_max(self, node, start, end, left, right):
        if left > end or right < start:
            return -1
        if left <= start and right >= end:
            return self.tree[node][1]
        mid = (start + end) // 2
        return max(self.get_max(2 * node, start, mid, left, right),
                   self.get_max(2 * node + 1, mid + 1, end, left, right))


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
segTree = SegmentTree(arr)
for i in range(m):
    a, b = map(int, input().split())
    print(segTree.query(a - 1, b - 1))
