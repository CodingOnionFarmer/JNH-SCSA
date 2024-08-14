# 최소 스패닝 트리, MST (Minimum Spanning Tree)
# Union-Find를 활용한 Kruskal Algorithm

# V^2은 1억이고, E는 10만이므로, O(ElogV)인 크루스칼이 O(V^2)인 프림보다 나은 경우이다.

import os, io, sys, heapq

sys.setrecursionlimit(10001)

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

v, e = map(int, input().split())
representative = [i for i in range(v + 1)]  # representative[i]는 i가 속한 집합의 대표(최소)원소
edges_queue = []
for i in range(e):
    a, b, c = map(int, input().split())
    edges_queue.append((c, a, b))  # 가중치가 낮은 Edge를 우선으로 뽑는 우선순위 큐
heapq.heapify(edges_queue)


def union(a, b):  # a의 대표와 b의 대표 중 더 작은 대표로 통일(합치기)
    ra = find(a)
    rb = find(b)
    if ra <= rb:
        representative[rb] = ra
        representative[b] = ra
        # a나 b의 대표만 바꾸는 게 아니라, 대표인 ra나 rb의 대표도 바꿔줘야 그룹 내의 다른 원소들도 대표가 바뀐다.
        return
    representative[ra] = rb
    representative[a] = rb
    return


def find(a):  # a가 속한 그룹의 대표 찾기
    r = representative[a]  # 이게 꼭 a가 속한 그룹의 대표가 아닐 수도 있다.
    # representative[i]가 자기 자신인 노드만 대표이기 때문에 재귀적으로 부모 노드 찾아 거슬러 올라가야 되기 때문
    if r == a:  # 본인이 대표이면 반환
        return r
    rr = find(r)  # 찐 대표(real representative) 찾기
    representative[a] = rr  # 다음에 또 재귀적으로 거슬러 올라가서 비효율적으로 찾지 말고 찐 대표로 갱신해둔다.
    return rr


ans = 0
chosen_edges = 0
MST_edges = v - 1
while chosen_edges < MST_edges:
    c, a, b = heapq.heappop(edges_queue)
    if find(a) == find(b):  # a-b로 이었을 때 사이클이 형성되면 안 고른다.
        continue
    chosen_edges += 1
    ans += c
    union(a, b)

print(ans)
