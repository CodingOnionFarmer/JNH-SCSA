# 최대 힙 클래스 직접 구현

import os, io


input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


class MaxHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def heapify_upward(self, idx):
        if idx == 1:  # root node
            return
        parent = idx >> 1
        if self.heap[parent] < self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            self.heapify_upward(parent)

    def heapify_downward(self, idx):
        left = idx << 1
        if left > self.size:
            return
        if left == self.size:
            if self.heap[left] > self.heap[idx]:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
            return
        right = left + 1
        if self.heap[left] >= self.heap[right]:
            if self.heap[left] > self.heap[idx]:
                self.heap[left], self.heap[idx] = self.heap[idx], self.heap[left]
                self.heapify_downward(left)
        else:
            if self.heap[right] > self.heap[idx]:
                self.heap[right], self.heap[idx] = self.heap[idx], self.heap[right]
                self.heapify_downward(right)

    def heappush(self, a):
        self.heap.append(a)
        self.size += 1
        self.heapify_upward(self.size)

    def heappop(self):
        if not self.size:
            return 0
        popped = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1
        self.heapify_downward(1)
        return popped


n = int(input())
ans = []
heap = MaxHeap()
for i in range(n):
    x = int(input())
    if x:
        MaxHeap.heappush(heap, x)
    else:
        ans.append(MaxHeap.heappop(heap))
print(*ans, sep='\n')
