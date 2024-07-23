import sys

input = sys.stdin.readline
print = sys.stdout.write


class SegTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))

    def query1(self, candy, amount):
        self.arr[candy] += amount
        self.update(1, 0, len(self.arr) - 1, candy, amount)

    def update(self, node, start, end, candy, amount):
        if candy < start or candy > end:
            return
        if start != end:
            mid = (start + end) // 2
            self.update(node * 2, start, mid, candy, amount)
            self.update(node * 2 + 1, mid + 1, end, candy, amount)
            self.tree[node] += amount
            return
        self.tree[node] += amount

    def query2(self, rank):
        candy = self.find(1, 0, len(self.arr) - 1, rank)
        self.arr[candy] -= 1
        self.update(1, 0, len(self.arr) - 1, candy, -1)
        return candy

    def find(self, node, start, end, rank):
        if start == end:
            return start
        mid = (start + end) // 2
        if self.tree[node * 2] >= rank:
            return self.find(node * 2, start, mid, rank)
        return self.find(node * 2 + 1, mid + 1, end, rank - self.tree[node * 2])


n = int(input())
candies = [0] * 1000001
segTree = SegTree(candies)
ans = ''
for _ in range(n):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(str(SegTree.query2(segTree, query[1])) + '\n')
    else:
        SegTree.query1(segTree, query[1], query[2])
