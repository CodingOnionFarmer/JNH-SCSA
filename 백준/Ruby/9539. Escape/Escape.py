import os, io, sys, heapq
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
print = sys.stdout.write


def find(x):
    if head[x] == x:
        return x
    hx = find(head[x])
    head[x] = hx
    return hx


fail = 'trapped\n'
success = 'escaped\n'
T = int(input())
for tc in range(T):
    n, t = map(int, input().split())
    chambers = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(n + 1)]
    for corridors in range(n - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    loss = chambers[:]  # 순간적으로 보는 최대 손해
    gain = chambers[:]  # loss를 빼고 결과적으로 얻는 이득
    head = [i for i in range(n + 1)]
    parent = [0] * (n + 1)
    child = [[] for _ in range(n + 1)]
    mq = [1]  # monsters q
    visited = [False] * (n + 1)
    visited[1] = True
    while mq:
        nmq = []
        for monster in mq:
            q = [monster]
            while q:
                nq = []
                for c in q:
                    for nc in graph[c]:
                        if visited[nc]:
                            continue
                        visited[nc] = True
                        if chambers[nc] >= 0:
                            head[nc] = monster
                            nq.append(nc)
                            gain[monster] += chambers[nc]
                        else:
                            nmq.append(nc)
                            parent[nc] = monster
                            child[monster].append(nc)
                q = nq
        mq = nmq

    ec = head[t]  # 그 몬스터로 가야만 / 갈 수 있으면 나갈 수 있음(필요충분)
    root_route = [ec]  # 목적지까지 가는 일직선 경로에 있는 것들
    node = ec
    while node != 1:
        node = parent[node]
        root_route.append(node)
    root_route.reverse()
    branch = [[] for _ in range(len(root_route) - 1)]
    for idx, node in enumerate(root_route[:-1]):
        q = [c for c in child[node] if c != root_route[idx + 1]]
        while q:
            nq = []
            for c in q:
                branch[idx].append(c)
                for cc in child[c]:
                    nq.append(cc)
            q = nq

    q = []  # 얘는 우선순위큐임 (흑자인 것만, 최대로 잃는 게 적은 것부터)
    nowHp = 0

    for idx, node in enumerate(root_route[:-1]):
        l, g = loss[node], gain[node]
        if l + nowHp < 0:
            print(fail)
            break
        nowHp += g
        head[node] = 1
        for c in branch[idx]:
            if loss[c] < 0 <= gain[c]:
                heapq.heappush(q, (-chambers[c], c))
        while q:
            cl, c = heapq.heappop(q)  # cl은 loss지만 양수
            if cl > nowHp:  # 지속 불가능 상태
                heapq.heappush(q, (cl, c))
                break
            cg = gain[c]
            ph = find(parent[c])  # parent의 head
            head[c] = ph
            if ph == 1:  # 시작점과 연결됨
                nowHp += cg
            else:
                if gain[ph] >= 0:
                    gain[ph] += cg
                else:
                    lost = gain[ph]  # 적자였음
                    loss[ph] = min(loss[ph], lost - cl)
                    gain[ph] += cg
                    if gain[ph] >= 0:
                        heapq.heappush(q, (-loss[ph], ph))
    else:
        if loss[ec] + nowHp >= 0:
            print(success)
        else:
            print(fail)
