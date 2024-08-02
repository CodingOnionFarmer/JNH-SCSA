import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
min_heap = []
ans = []
for _ in range(n):
    x = int(input())
    if x:
        heapq.heappush(min_heap, x)
    else:
        if not min_heap:
            ans.append(0)
        else:
            ans.append(heapq.heappop(min_heap))
print(*ans, sep='\n')
