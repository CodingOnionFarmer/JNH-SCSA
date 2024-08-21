import heapq

n, m, s, e = map(int, input().split())
# graph[i][j][c]는 i에서 j로 가는 요금 c인 도로 중 최소 시간 t
graph = [[] for _ in range(n + 1)]
for road in range(m):
    p, r, c, t = map(int, input().split())
    graph[p].append((r, c, t))
    graph[r].append((p, c, t))

good_ways = [set() for _ in range(n + 1)]  # good_ways[i]에는 i도시로 가는 효율적인 비용-시간 쌍을 넣는다.
good_ways[s].add(0)
q = [(0, 0, s)]

while q:
    cost, time, city = heapq.heappop(q)
    if cost * 10000 + time not in good_ways[city]:
        continue
    for adj, c, t in graph[city]:
        nc, nt = cost + c, time + t
        if not good_ways[adj]:
            good_ways[adj].add(nc * 10000 + nt)
            heapq.heappush(q, (nc, nt, adj))
            continue
        good = False
        was_good_but_bad = set()
        for gct in good_ways[adj]:
            gc, gt = gct // 10000, gct % 10000
            if nc == gc:
                if nt < gt:
                    was_good_but_bad.add(gct)
                    good = True
                else:
                    good = False
                    break
            elif nc < gc:
                good = True
                if nt <= gt:
                    was_good_but_bad.add(gct)
            else:
                if nt < gt:
                    good = True
                else:
                    good = False
                    break
        for bad in was_good_but_bad:
            good_ways[adj].remove(bad)
        if good:
            good_ways[adj].add(nc * 10000 + nt)
            heapq.heappush(q, (nc, nt, adj))
print(len(good_ways[e]))
