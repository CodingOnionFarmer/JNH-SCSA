"""
BOJ : 나무 재테크

시작 시간 : 3시 01분
구상 완료 : 3시 07분
테케 틀림 : 3시 37분, 4시 00분(직접 만든 테케로 시간 너무 오래걸림)
1회  오답 : 3시 47분
제출 시간 : 4시 06분
"""

n, m, h = map(int, input().split())
garos = [[0] * (n + 1) for _ in range(h)]
for i in range(m):
    a, b = map(int, input().split())
    garos[a - 1][b - 1] = 1
    garos[a - 1][b] = -1


# started_from_index_i_j = [[j for j in range(n)] for i in range(h + 1)]
# for i in range(h - 1, -1, -1):
#     for j in range(n):
#         started_from_index_i_j[i][j] = started_from_index_i_j[i + 1][j + garos[i][j]]

# 잘 만들었는지 손테케 검증 (3시 19분)
# for line in started_from_index_i_j:
#     print(line)

# for line in garos:
#     print(line)

def check():
    cnt = 0
    for j in range(n):
        now = j
        for i in range(h):
            now += garos[i][now]
        if now != j:
            cnt += 1
    return cnt


best = 4


def dfs(depth):
    global best
    c = check()
    if c > (best - 1 - depth) << 1:
        return
    if c == 0:
        best = min(best, depth)
        return
    if best == depth + 1:
        return
    for i in range(h):
        garo = garos[i]
        for j in range(n - 1):
            if garo[j] or garo[j + 1]:
                continue
            garo[j] = 1
            garo[j + 1] = -1
            dfs(depth + 1)
            garo[j] = 0
            garo[j + 1] = 0
            if best == depth + 1:
                return
    return


dfs(0)
if best == 4:
    best = -1
print(best)
