import heapq, sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    heap_min = []
    heap_max = []
    queue = {}
    heap_length = 0
    for i in range(k):
        op, num = map(str, input().strip().split())
        num = int(num)
        if op == 'I':
            heapq.heappush(heap_min, num)
            heapq.heappush(heap_max, -num)
            if num in queue:
                queue[num] += 1
            else:
                queue[num] = 1
            heap_length += 1
        elif not heap_length:
            pass
        elif num == 1:
            while True:
                deleted = -heapq.heappop(heap_max)
                if queue[deleted]:
                    queue[deleted] -= 1
                    break
            heap_length -= 1
        else:
            while True:
                deleted = heapq.heappop(heap_min)
                if queue[deleted]:
                    queue[deleted] -= 1
                    break
            heap_length -= 1
    if not heap_length:
        print('EMPTY')
    else:
        while True:
            maximum = -heapq.heappop(heap_max)
            if queue[maximum]:
                break
        while True:
            minimum = heapq.heappop(heap_min)
            if queue[minimum]:
                break
        print(maximum, minimum)
