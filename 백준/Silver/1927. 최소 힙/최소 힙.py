import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
priority_queue = []
ans = []
for i in range(n):
    x = int(input())
    if x:
        heapq.heappush(priority_queue, x)
    else:
        if priority_queue:
            ans.append(heapq.heappop(priority_queue))
        else:
            ans.append(0)
print(*ans, sep='\n')
