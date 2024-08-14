# 다익스트라, Dijkstra
# 이분 탐색, Binary Search

# x원 이하의 요금으로 이루어진 길만으로 목적지에 c원 이하로 쓰고 도착할 수 있는지 다익스트라로 판정한다.
# 위의 x 중 가능한 최댓값을 이분 탐색으로 찾는다.


import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m, start, end, c = map(int, input().split())
connected = [[] for _ in range(n + 1)]
for i in range(m):
    a, b, p = map(int, input().split())
    connected[a].append((b, p))
    connected[b].append((a, p))

left = 1
right = c  # c+1원 이상은 체크할 필요 없으므로 가능한 x 중 최대는 c이다.
while left < right:
    mid = (left + right) >> 1

    # 다익스트라로 start에서 end까지 mid원 이하의 요금인 길만 통해서 c원 이내로 도착하는지 확인한다.
    q = [(0, start)]
    cost = [c + 1] * (n + 1)
    while q:
        p, a = heapq.heappop(q)
        if cost[a] < p:
            continue
        for b, bp in connected[a]:
            if bp > mid:
                continue
            if cost[b] > p + bp:
                cost[b] = p + bp
                heapq.heappush(q, (p + bp, b))
    # 도착 성공하면 left부터 mid까지로 탐색 범위를 좁힌다.
    if cost[end] <= c:
        right = mid
    # 도착 실패하면 mid+1부터 right까지로 좁힌다.
    else:
        left = mid + 1

# c원 이내로 도착하는 길이 아예 없는 경우에는, 어떤 mid로도 다 실패하고 left=right=c일 수 있다.
# 따라서 right가 c일 때만 다익스트라를 한 번 더 돌려서 가능한지 판정한다.
if right == c:
    q = [(0, start)]
    cost = [c + 1] * (n + 1)
    while q:
        p, a = heapq.heappop(q)
        if cost[a] < p:
            continue
        for b, bp in connected[a]:
            if bp > right:
                continue
            if cost[b] > p + bp:
                cost[b] = p + bp
                heapq.heappush(q, (p + bp, b))
    if cost[end] <= c:
        print(right)
    else:
        print(-1)
else:
    print(right)
