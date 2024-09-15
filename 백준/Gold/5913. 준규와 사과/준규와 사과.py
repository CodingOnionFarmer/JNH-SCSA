"""
240915
BOJ : 준규와 사과

시작 시간 : 2시 38분
구상 완료 : 2시 42분
제출 시간 :

"""

# BFS
# 비트마스킹 (선택)

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

adj = {1 << 5 * i + j: tuple(1 << 5 * (i + di) + j + dj for di, dj in directions if 0 <= i + di < 5 and 0 <= j + dj < 5)
       for i in range(5) for j in range(5)}

start = 16777217
k = int(input())
move = 24 - k >> 1
for _ in range(k):
    i, j = map(int, input().split())
    start |= 1 << (i - 1) * 5 + j - 1

q = {(start, 1, 16777216): 1}  # 튜플을 key로 넣는건 굉장히 무거운데... 더 좋은 방법을 고민해 보는걸로
for _ in range(move - 1):
    nq = {}
    for (bit, j, h), cnt in q.items():  # j 준규 h 해빈
        for nj in adj[j]:
            if bit & nj:
                continue
            nj_bit = bit | nj
            for nh in adj[h]:
                if nj_bit & nh:
                    continue
                nh_bit = nj_bit | nh
                if (nh_bit, nj, nh) in nq:
                    nq[(nh_bit, nj, nh)] += cnt
                else:
                    nq[(nh_bit, nj, nh)] = cnt
    q = nq

# ans = 0
# for (bit, j, h), cnt in q.items():
#     if any(not bit & nj for nj in adj[j]) and any(not bit & nh for nh in adj[h]):
#         ans += cnt
#
# print(ans)

# 한줄로
print(sum(cnt for (bit, j, h), cnt in q.items()
          if any(not bit & nj for nj in adj[j]) and any(not bit & nh for nh in adj[h])))
