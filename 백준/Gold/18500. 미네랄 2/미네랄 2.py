"""
24.09.30 (월)

BOJ : 미네랄 2

특이사항 : 스터디 문제로 선정한 적 있는데, 풀다가 말았음

1회차 (현재)
목표 풀이 시간 : 30분 이내  (풀다 만 것 고려)

시작 시간 : 4시 37분
구상 완료 : 4시 38분
제출 완료 : 5시 17분
"""

directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

r, c = map(int, input().split())
cave = [[0 if char == '.' else 1 for char in input()] for _ in range(r)]
adj = [[[(i + di, j + dj) for di, dj in directions if 0 <= i + di < r and 0 <= j + dj < c] for j in range(c)] for i in
       range(r)]
n = int(input())
left = 1
shoot_range = ((c - 1, -1, -1), (c,))  # 우->좌, 좌->우
shoot_height = list(map(int, input().split()))
for height in shoot_height:
    sr = r - height  # shoot row
    for j in range(*shoot_range[left]):
        if cave[sr][j]:
            hc = j  # hit column
            break
    else:
        left ^= 1
        continue
    left ^= 1
    cave[sr][hc] = 0
    visited = [[False] * c for _ in range(r)]
    for ar, ac in adj[sr][hc]:
        if cave[ar][ac] and not visited[ar][ac]:
            q = [(ar, ac)]
            cluster = [(ar, ac)]
            visited[ar][ac] = True
            on_the_ground = ar == r - 1
            while q:
                nq = []
                for cr, cc in q:
                    for nr, nc in adj[cr][cc]:
                        if not cave[nr][nc] or visited[nr][nc]:
                            continue
                        if nr == r - 1:
                            on_the_ground = True
                        nq.append((nr, nc))
                        cluster.append((nr, nc))
                        visited[nr][nc] = True
                q = nq
            drop = r
            if not on_the_ground:
                for cr, cc in cluster:
                    cave[cr][cc] += 1
                for cr, cc in cluster:
                    if not cave[cr + 1][cc]:
                        depth = 1
                        cr += 2
                        while cr < r and not cave[cr][cc]:
                            depth += 1
                            cr += 1
                        if cr < r and cave[cr][cc] == 2:
                            continue
                        if depth < drop:
                            drop = depth
                for cr, cc in cluster:
                    cave[cr][cc] -= 2
                    cave[cr + drop][cc] += 1
                break

final_cave = [['x' if cave[i][j] else '.' for j in range(c)] for i in range(r)]
for line in final_cave:
    print(*line, sep='')
