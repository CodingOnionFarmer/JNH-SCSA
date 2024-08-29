# 언어 : PyPy3
# 메모리 : 111364KB
# 시간 : 124ms
# 시도횟수 : 1회

# BFS, DFS, 백트래킹, 완전탐색, 그래프 탐색

"""
1. 비트연산을 활용하여, 2^n - 2가지(한 쪽이 원소가 0개인 경우 제외)의 그룹 나누기 경우의 수를 완전탐색한다.
    -> 비트가 0인 쪽과 1인 쪽 두 그룹으로 나누는 것이다.

2. 두 그룹의 인구수 차이가 현재 최소치보다 크거나 같으면 판정할 필요 없이 가지치기한다.

3. 최소치 갱신할 가능성이 있으면, 두 그룹이 각각 하나의 연결된 집합인지 판정한다.
    -> 이를 판정하기 위해, 각 그룹에서 대표 원소 아무거나 하나씩 뽑고, BFS 순회로 방문 가능한 모든 점을 방문처리한다.
    -> 방문처리도 비트마스킹을 활용했다.
    -> 두 그룹의 대표 원소에서 출발해서 순회 한 번씩을 끝마치고 난 뒤, 미방문 점이 없으면 두 그룹 다 연결되어 있는 것이다.

4. 최소치를 갱신했는데 그게 1 이하이면 뒤에 더 볼 필요 없이 종료한다.
"""

# 지역구의 수
n = int(input())

# 각 지역구의 인구수와 총 인구수
popularity = list(map(int, input().split()))
total = sum(popularity)

# graph[i]에 j가 있으면, i와 j가 연결된 것
graph = [[] for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    if lst[0]:
        for j in lst[1:]:
            graph[i].append(j - 1)

# 방문처리를 비트마스킹으로 하고, 그게 full = 111...1(1이 n개)이면, 모든 점을 방문한 것이다.
full = (1 << n) - 1
best = 1001

# 대칭성이 있으므로, 마지막 지역구는 그룹0으로 고정해도 됨 -> 범위 조정
for code in range(1, 1 << n - 1):
    # code가 0111011이면, 2,6번 지역구가 그룹0, 0,1,3,4,5번 지역구가 그룹1이다.
    # 두 그룹의 인구수를 다 셀 필요는 없다(총 인구수 total을 세어 놨으므로)
    group1_popularity = sum(popularity[i] for i in range(n) if (1 << i) & code)
    diff = abs(total - (group1_popularity << 1))

    # 최소 기록 갱신 불가능한 경우는 가지치기
    if diff >= best:
        continue

    # 그룹0 bfs 순회하면서 방문처리
    q = [n - 1]
    visited = 1 << n - 1
    while q:
        nq = []
        for area in q:
            for connected_area in graph[area]:
                if not code & (1 << connected_area) and not visited & (1 << connected_area):
                    nq.append(connected_area)
                    visited |= 1 << connected_area
        q = nq

    # 그룹1 bfs 순회하면서 방문처리
    q = []
    for i in range(n):
        if (1 << i) & code:
            q.append(i)
            break
    visited |= 1 << q[0]
    while q:
        nq = []
        for area in q:
            for connected_area in graph[area]:
                if code & (1 << connected_area) and not visited & (1 << connected_area):
                    nq.append(connected_area)
                    visited |= 1 << connected_area
        q = nq

    # 모든 점을 방문했어야, 각 그룹이 잘 연결된 상태이다.
    if visited == full:
        # 갱신 가능한 경우에만 탐색했으므로, 반드시 갱신
        best = diff
        # 현재 최소값이 더 갱신 불가능한 값이면 조기 종료
        if best < 2:
            break

# 초기값(불가능한 값)이 전혀 갱신되지 않았으면 두 연결된 그룹으로 나누는 경우가 아예 없는 것이다.
if best == 1001:
    best = -1
print(best)
