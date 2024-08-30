"""
BOJ : 연구소 3

시작 시간 : 9시 50분
구상 완료 : 9시 54분
테케 틀림 : 10시 10분
제출 시간 :

"""

n, m = map(int, input().split())
lab = []
for _ in range(n):
    line = list(map(int, input().split()))
    for num in line:
        lab.append(num)
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
adj = [[(i + di) * n + j + dj for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n] for i in range(n) for j
       in range(n)]
v = 0
viruses = []
empty = 0
for idx in range(n ** 2):
    if lab[idx] == 2:
        v += 1
        viruses.append(idx)
    elif not lab[idx]:
        empty += 1

min_time = 2501
for code in range(1 << v):
    active_v = 0
    q = []
    for i in range(v):
        if code & (1 << i):
            active_v += 1
            q.append((viruses[i]))
    if active_v != m:
        continue
    visited = [False] * (n ** 2)
    time = 0
    visited_empty = 0
    while q and visited_empty < empty and time < min_time:
        time += 1
        nq = []
        for cur in q:
            for nex in adj[cur]:
                if visited[nex] or lab[nex] == 1:
                    continue
                visited[nex] = True
                nq.append(nex)
                if not lab[nex]:
                    visited_empty += 1
        q = nq
    if visited_empty == empty:
        # print(time)
        # print(bin(code))
        # for i in range(v):
        #     if code & (1 << i):
        #         print(viruses[i])
        min_time = time
        if min_time < 2:
            break

if min_time == 2501:
    min_time = -1
print(min_time)
