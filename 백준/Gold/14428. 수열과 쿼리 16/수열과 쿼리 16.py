import sys

input = sys.stdin.readline


def print(something):
    sys.stdout.write(str(something) + '\n')


class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [[0, 0] for _ in range(4 * len(arr))]
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node][0] = self.arr[start]
            self.tree[node][1] = start
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            if self.tree[2 * node][0] <= self.tree[2 * node + 1][0]:
                self.tree[node][0] = self.tree[2 * node][0]
                self.tree[node][1] = self.tree[2 * node][1]
            else:
                self.tree[node][0] = self.tree[2 * node + 1][0]
                self.tree[node][1] = self.tree[2 * node + 1][1]

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
            if self.tree[2 * node][0] <= self.tree[2 * node + 1][0]:
                self.tree[node][0] = self.tree[2 * node][0]
                self.tree[node][1] = self.tree[2 * node][1]
            else:
                self.tree[node][0] = self.tree[2 * node + 1][0]
                self.tree[node][1] = self.tree[2 * node + 1][1]
        else:
            self.tree[node][0] = value

    def query2(self, left, right):
        return self.get_min(1, 0, len(self.arr) - 1, left, right)

    def get_min(self, node, start, end, left, right):
        if left > end or right < start:
            return 1000000001, 0
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        num1, idx1 = self.get_min(2 * node, start, mid, left, right)
        num2, idx2 = self.get_min(2 * node + 1, mid + 1, end, left, right)
        if num1 <= num2:
            return num1, idx1
        return num2, idx2


n = int(input())
arr = list(map(int, input().split()))
segTree = SegmentTree(arr)
m = int(input())
for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        segTree.query1(b - 1, c)
    else:
        print(segTree.query2(b - 1, c - 1)[1] + 1)
