# 다익스트라, Dijkstra

# 왜 맞은사람에 안뜨죠?;;


import os, io, heapq

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
cannot_go = list(map(int, input().split()))  # 0이면 갈 수 있고 1이면 갈 수 없음
cannot_go[n - 1] = 0
connected = [[] for _ in range(n)]  # connected[a]에는 a에서 갈 수 있는 곳들과 그 거리를 저장
for i in range(m):
    a, b, t = map(int, input().split())
    if cannot_go[a] or cannot_go[b]:
        continue
    connected[a].append((b, t))
    connected[b].append((a, t))
distance = [10000000001] * n  # 출발점(0)으로부터의 거리
distance[0] = 0
q = [(0, 0)]  # q는 우선순위 큐(힙)이고, (노드, 노드까지의 거리)를 넣는다.
while q:
    d, a = heapq.heappop(q)
    if distance[a] < d:  # 먼저 넣어둔 값이 더 안 좋은 값일 수도 있다.
        # ex) 0->1 거리 10, 0->2 거리 3, 2->1 거리 3이면 0에서 출발할 때 10,1을 넣어두지만,
        # 실제로는 0->2->1의 거리 6으로 이미 갱신된 뒤에 꺼내지므로 유효하지 않은 값이다.
        continue
    # 유효한 값을 꺼냈으면, a에서 갈 수 있는 모든 점들에 대해 유효한 최단거리이면 힙에 넣는다.
    for b, t in connected[a]:
        if distance[b] > d + t:
            distance[b] = d + t
            heapq.heappush(q, (d + t, b))

ans = distance[n - 1]
if ans == 10000000001:  # n-1에 도달하지 못한 경우
    ans = -1
print(ans)
