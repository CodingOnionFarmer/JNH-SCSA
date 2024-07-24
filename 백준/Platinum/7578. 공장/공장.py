class SegTree:
    def __init__(self, arr):
        self.arr = arr
        self.tree = [0] * (4 * len(arr))
        self.build(1, 0, len(arr) - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = 1
            return
        mid = (start + end) // 2
        self.build(node * 2, start, mid)
        self.build(node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, index):
        self.arr[index] = 0
        return self.del_and_check(1, 0, len(self.arr) - 1, index)

    def del_and_check(self, node, start, end, index):
        if start > index:
            return 0
        if end < index:
            return self.tree[node]
        if start == end:
            self.tree[node] = 0
            return 0
        mid = (start + end) // 2
        self.tree[node] -= 1
        return self.del_and_check(node * 2, start, mid, index) + self.del_and_check(node * 2 + 1, mid + 1, end, index)


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Bidx = [0] * 1000001
for idx, num in enumerate(B):
    Bidx[num] = idx
arr = [1] * n
segTree = SegTree(arr)
ans = 0
for num in A:
    ans += SegTree.query(segTree, Bidx[num])
print(ans)
