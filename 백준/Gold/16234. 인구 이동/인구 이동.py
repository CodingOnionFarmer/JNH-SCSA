"""
BOJ : 인구 이동
코드트리 : 토스트 계란틀

시작 시간 : 3시 01분
"""

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
n, l, r = map(int, input().split())
eggs = [list(map(int, input().split())) + [201] for _ in range(n)] + [[201] * n]
area = []
area_average = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        visited[i][j] = True
        check = eggs[i][j]
        if any(l <= abs(eggs[i + di][j + dj] - check) <= r for di, dj in directions):
            temp_area = [(i, j)]
            temp_size = 1
            temp_egg = check
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    check = eggs[ci][cj]
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if l <= abs(eggs[ni][nj] - check) <= r and not visited[ni][nj]:
                            temp_size += 1
                            temp_egg += eggs[ni][nj]
                            visited[ni][nj] = True
                            nq.append((ni, nj))
                            temp_area.append((ni, nj))
                q = nq
            area.append(temp_area)
            area_average.append(temp_egg // temp_size)

move = 0
while area:
    move += 1
    for idx, one_area in enumerate(area):
        egg = area_average[idx]
        for i, j in one_area:
            eggs[i][j] = egg
    area = []
    area_average = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            visited[i][j] = True
            check = eggs[i][j]
            if any(l <= abs(eggs[i + di][j + dj] - check) <= r for di, dj in directions):
                temp_area = [(i, j)]
                temp_size = 1
                temp_egg = check
                q = [(i, j)]
                while q:
                    nq = []
                    for ci, cj in q:
                        check = eggs[ci][cj]
                        for di, dj in directions:
                            ni, nj = ci + di, cj + dj
                            if l <= abs(eggs[ni][nj] - check) <= r and not visited[ni][nj]:
                                temp_size += 1
                                temp_egg += eggs[ni][nj]
                                visited[ni][nj] = True
                                nq.append((ni, nj))
                                temp_area.append((ni, nj))
                    q = nq
                area.append(temp_area)
                area_average.append(temp_egg // temp_size)

print(move)
