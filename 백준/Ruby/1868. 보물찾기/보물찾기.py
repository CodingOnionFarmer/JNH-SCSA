import sys
input = sys.stdin.readline

def br(k):  # binary round
    return 1 << (len(bin(k)) - 2)


n = int(input())
graph = {i + 1: set() for i in range(n)}
visited = [0] * (n + 1)
recorded = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)
connected = [0] + [len(graph[i + 1]) for i in range(n)]
# print(connected)
fte = {1: {i for i in graph if len(graph[i]) == 1}}  # from the end
for p in fte[1]:
    visited[p] = 1
first = second = 0
while fte:
    # print(fte)
    m = min(fte)
    # print(m)
    if len(fte[m]) == 1:
        first, second = m, first
    else:
        first = second = m
    for p in fte[m]:
        # print(p, m)
        for cp in graph[p]:
            # print(cp, connected[cp], visited[cp])
            if connected[cp] - visited[cp] > 2:
                visited[cp] += 1
                if visited[cp] == 1:
                    recorded[cp] = m + 1
                elif recorded[cp] + m >= br(m):
                    recorded[cp] = br(m)
                else:
                    cover = br(m ^ (m + recorded[cp] - 1))//2
                    recorded[cp] = m // cover * cover + cover
                # else:
                #     cover = br(m & (recorded[cp] - 1))
                #     recorded[cp] = m // cover * cover + cover
                # print(recorded[cp])
            elif not visited[cp]:
                visited[cp] = 1
                if m + 1 not in fte:
                    fte[m + 1] = {cp}
                else:
                    fte[m + 1].add(cp)
            elif connected[cp] - visited[cp] == 2:
                visited[cp] += 1
                if recorded[cp] + m >= br(m):
                    b = br(m)
                else:
                    cover = br(m ^ (m + recorded[cp] - 1))//2
                    b = m // cover * cover + cover
                # else:
                #     cover = br(m & (recorded[cp] - 1))
                #     # d = br(recorded[cp]) // 2
                #     b = m // cover * cover + cover
                # print(b)
                if b == m:
                    print(1 / 0)
                if b not in fte:
                    fte[b] = {cp}
                else:
                    fte[b].add(cp)
        # print('---------')
    fte.pop(m)
if n == 1:
    print(0)
else:
    print(len(bin(second)) - 2)
    # print(first, second)
    # print(visited)
    # print(recorded)
