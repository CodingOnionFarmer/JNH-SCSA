import heapq

n, m, k, t, p = map(int, input().split())
mosquitoes = [list(map(int, input().split())) for _ in range(k)]
distance = [[0] * k for _ in range(k)]
for i in range(k - 1):
    for j in range(i + 1, k):
        distance[i][j] = distance[j][i] = abs(mosquitoes[i][0] - mosquitoes[j][0]) + abs(
            mosquitoes[i][1] - mosquitoes[j][1])
max1 = max2 = 0


def dfs(now, cnt, moved):
    global max1
    if max1 == k:
        return
    if cnt == k:
        max1 = k
        return
    if cnt > max1:
        max1 = cnt
    for mos in range(k):
        if not visited[mos] and moved + distance[now][mos] <= t:
            visited[mos] = True
            dfs(mos, cnt + 1, moved + distance[now][mos])
            visited[mos] = False
    return


visited = [False] * k
for mo in range(k):
    visited[mo] = True
    dfs(mo, 1, 0)
    visited[mo] = False

for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt = 0
        for mo in range(k):
            dist = abs(i - mosquitoes[mo][0]) + abs(j - mosquitoes[mo][1])
            if p >= dist * mosquitoes[mo][2]:
                cnt += 1
        if cnt > max2:
            max2 = cnt

print(max1, max2)
