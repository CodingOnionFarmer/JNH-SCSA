n, m = map(int, input().split())
city = [list(input().split()) for _ in range(n)]
home = []
hospital = []

nhd_fh = []
for i in range(n):
    for j in range(n):
        if city[i][j] == '1':
            home.append((i, j))
            nhd_fh.append([])
        elif city[i][j] == '2':
            hospital.append((i, j))

for idx_home, (hmi, hmj) in enumerate(home):
    for idx_hospital, (hpi, hpj) in enumerate(hospital):
        nhd_fh[idx_home].append((abs(hmi - hpi) + abs(hmj - hpj), 1<<idx_hospital))
    nhd_fh[idx_home].sort()

h = len(hospital)


def dfs(depth, occupied, save, close):
    if depth == h:
        global shortest
        distance = 0
        for hospitals_list in nhd_fh:
            if distance >= shortest:
                return
            for hospital_dist, hospital_idx_bit in hospitals_list:
                if hospital_idx_bit & occupied:
                    distance += hospital_dist
                    break
        if distance < shortest:
            shortest = distance
        return
    if save:
        dfs(depth + 1, occupied | (1 << depth), save - 1, close)
    if close:
        dfs(depth + 1, occupied, save, close - 1)
    return


shortest = 10001
dfs(0, 0, m, h - m)
print(shortest)
