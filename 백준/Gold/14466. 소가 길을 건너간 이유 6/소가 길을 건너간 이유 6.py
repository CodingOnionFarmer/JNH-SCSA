"""
240915
BOJ : 소가 길을 건너간 이유 6

시작 시간 : 4시 18분
구상 완료 : 4시 19분
제출 완료 : 4시 35분

"""


def idx_int(num):
    return int(num) - 1


n, k, r = map(int, input().split())
size = n ** 2

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
adj = [{(i + di) * n + j + dj for di, dj in directions if 0 <= i + di < n and 0 <= j + dj < n} for i
       in range(n) for j in range(n)]

for _ in range(r):
    r1, c1, r2, c2 = map(idx_int, input().split())
    p1 = r1 * n + c1
    p2 = r2 * n + c2
    adj[p1].discard(p2)
    adj[p2].discard(p1)

cow = [0] * size
for _ in range(k):
    r, c = map(idx_int, input().split())
    cow[r * n + c] += 1

visited = [False] * size
ans = 0
for i in range(size):
    if not visited[i]:
        cow_cnt = cow[i]
        visited[i] = True
        q = [i]
        while q:
            nq = []
            for j in q:
                for nj in adj[j]:
                    if not visited[nj]:
                        cow_cnt += cow[nj]
                        visited[nj] = True
                        nq.append(nj)
            q = nq
        ans += cow_cnt * (k - cow_cnt)

ans >>= 1
print(ans)
