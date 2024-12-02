import sys, heapq

input = sys.stdin.readline

n, m, k = map(int, input().split())
s, d = map(int, input().split())
dist_and_cost = [[] for _ in range(n + 1)]
dist_and_cost[s].append((0, 0))
road = [{} for _ in range(n + 1)]
for _ in range(m):
    a, b, w = map(int, input().split())
    if b not in road[a] or road[a][b] > w:
        road[a][b] = road[b][a] = w
q = [(0, 0, s)]  # 거리, 비용, 정점
visited = [[False] * 1000 for _ in range(n + 1)]
while q:
    dist, cost, city = heapq.heappop(q)
    nd = dist + 1
    if nd == 1000:
        break
    for adj, wage in road[city].items():
        nc = cost + wage
        if visited[adj][nd]:
            if dist_and_cost[adj][-1][0] == nd:
                if dist_and_cost[adj][-1][1] > nc:
                    dist_and_cost[adj][-1] = (nd, nc)
                    heapq.heappush(q, (nd, nc, adj))
            else:
                if all(more_cost > nc for less_dist, more_cost in dist_and_cost[adj]):
                    dist_and_cost[adj].append((nd, nc))
                    heapq.heappush(q, (nd, nc, adj))
        else:
            visited[adj][nd] = True
            if all(more_cost > nc for less_dist, more_cost in dist_and_cost[adj]):
                dist_and_cost[adj].append((nd, nc))
                heapq.heappush(q, (nd, nc, adj))
dnc_to_destination = dist_and_cost[d]
dist, cost = dnc_to_destination[-1]
idx = len(dnc_to_destination) - 1
answer = [cost]
increment = 0
for _ in range(k):
    increment += int(input())
    if idx:
        new_idx = idx
        for ni, (nd, nc) in enumerate(dnc_to_destination[:idx]):
            if cost + dist * increment > nc + nd * increment:
                new_idx = ni
                dist, cost = nd, nc
                continue
        idx = new_idx
    answer.append(cost + dist * increment)
print(*answer, sep='\n')
