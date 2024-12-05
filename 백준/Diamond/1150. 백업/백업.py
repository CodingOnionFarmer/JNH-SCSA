import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, k = map(int, input().split())
linked_list = {}  # 좌 : 우
ll_rev = {}  # 우 : 좌
distance = {}
q = []
left = int(input())
for _ in range(n - 1):
    right = int(input())
    linked_list[left] = right
    ll_rev[right] = left
    distance[left] = right - left
    q.append((right - left, left, right))
    left = right
heapq.heapify(q)
answer = 0
for _ in range(k):
    while True:
        d, l, r = heapq.heappop(q)
        if l in linked_list and linked_list[l] == r:
            linked_list.pop(l)
            if r in ll_rev:
                ll_rev.pop(r)
            else:
                print(1/0)
            answer += d
            if l in ll_rev:
                ll = ll_rev.pop(l)
                if r in linked_list:
                    rr = linked_list.pop(r)
                    linked_list[ll] = rr
                    ll_rev[rr] = ll
                    nd = distance[ll] + distance[r] - d
                    distance[ll] = nd
                    heapq.heappush(q, (nd, ll, rr))
                else:
                    linked_list.pop(ll)
            else:
                if r in linked_list:
                    rr = linked_list.pop(r)
                    ll_rev.pop(rr)
            break
print(answer)
