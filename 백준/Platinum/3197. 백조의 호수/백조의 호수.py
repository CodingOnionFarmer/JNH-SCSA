directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

r, c = map(int, input().split())
lake = [list(input()) for _ in range(r)]
representative = [i * c + j for i in range(r) for j in range(c)]
area_size = [1] * (r * c)
will_melt = set()
swan = []

for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append(i * c + j)
        if lake[i][j] != 'X' and representative[i * c + j] == i * c + j:
            parent = i * c + j
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if ni < 0 or ni >= r or nj < 0 or nj >= c:
                            continue
                        if lake[ni][nj] == 'X':
                            will_melt.add(ni * c + nj)
                        elif representative[ni * c + nj] != parent:
                            representative[ni * c + nj] = parent
                            nq.append((ni, nj))
                            area_size[parent] += 1
                q = nq


def find(a):
    if representative[a] == a:
        return a
    ra = find(representative[a])
    representative[a] = ra
    return ra


def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    sa, sb = area_size[ra], area_size[rb]
    if sa > sb:
        representative[rb] = ra
        area_size[ra] += sb
        return
    representative[ra] = rb
    area_size[rb] += sa
    return


day = 0
while find(swan[0]) != find(swan[1]):
    # print('---------------------')
    # print(day, '번째 날')
    # for line in lake:
    #     print(line)
    day += 1
    will_melt_next_day = set()
    for ice in will_melt:
        i, j = ice // c, ice % c
        lake[i][j] = '.'
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= r or nj < 0 or nj >= c:
                continue
            if lake[ni][nj] == 'X':
                if ni * c + nj not in will_melt:
                    will_melt_next_day.add(ni * c + nj)
                continue
            union(ni * c + nj, ice)
    will_melt = will_melt_next_day

print(day)
