# bfs가 아닌 lca(least common anscestor, 최소공통조상) 알고리즘을 이용한 풀이
# 트리 구조에서 사용할 수 있는 알고리즘이다.
# 전처리 과정에서 dfs를 수행한다.
# 거리를 찾는 쿼리가 1회이므로, Naive Version으로 수행


n = int(input())
a, b = map(int, input().split())
m = int(input())
parent = [i for i in range(n + 1)]
children = [[] for _ in range(n + 1)]
depth = [0] * (n + 1)  # depth는 이 문제에서 항렬과 같은 의미로 생각할 수 있음
for _ in range(m):
    p, c = map(int, input().split())
    parent[c] = p
    children[p].append(c)

for i in range(1, n + 1):  # 각 node의 depth를 찾아서 설정하는 과정
    if parent[i] == i:  # root node에서 dfs 실행, 부모가 없는 노드(어감이 좀 이상하지만)가 root node임
        stack = [child for child in children[i]]
        while stack:
            p = stack.pop()
            depth[p] = depth[parent[p]] + 1
            for c in children[p]:
                stack.append(c)

if depth[a] < depth[b]:
    a, b = b, a  # a가 더 depth가 높도록(항렬이 더 낮도록) 맞춰줌

ans = depth[a] - depth[b]  # depth를 맞추기 전까지는 최소 공통 조상에 도달할 수 없으므로 최소한 이 차이만큼의 촌수는 보장됨
for _ in range(ans):
    a = parent[a]  # 부모를 찾아 올라가면서 depth를 낮춘다.

while a != b and depth[a]:  # 공통 조상을 못 찾았고, 아직 더 올라갈 조상이 (depth만큼) 남은 경우
    a = parent[a]
    b = parent[b]
    ans += 2

if a != b:  # 공통 조상이 없는 경우 (둘 다 시조, root node까지 올라갔는데 그 둘이 다른 경우)
    ans = -1

print(ans)
