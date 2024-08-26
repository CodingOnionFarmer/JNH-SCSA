"""
시작 시간 : 3시 34분
제출 시간 : 3시 58분
"""

# 구현, 시뮬레이션

n, m = map(int, input().split())
city = [list(input().split()) for _ in range(n)]
home = []
hospital = []

# nearest_hospital_and_distance_from_home
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
        nhd_fh[idx_home].append((abs(hmi - hpi) + abs(hmj - hpj), idx_hospital))
    nhd_fh[idx_home].sort()

h = len(hospital)


# depth : 재귀 깊이, 현재 살릴 지 말지 정할 병원의 인덱스 (0 시작, h 도달시 종료)
# occupied : 비트마스킹으로 i번째 병원을 남기면 1, 없애면 0  (2진법으로 h자리 비트)
# save : 남은 살릴 병원 수
# close : 남은 닫을 병원 수
def dfs(depth, occupied, save, close):
    if depth == h:
        global shortest
        saved_hospitals = {idx for idx in range(h) if occupied & (1 << idx)}
        distance = 0
        for hospitals_list in nhd_fh:
            if distance >= shortest:
                return
            for hospital_dist, hospital_idx in hospitals_list:
                if hospital_idx in saved_hospitals:
                    distance += hospital_dist
                    break
        if distance < shortest:
            shortest = distance
        return
    if save:  # depth번 병원 살리기
        dfs(depth + 1, occupied | (1 << depth), save - 1, close)
    if close:  # depth번 병원 폐업하기
        dfs(depth + 1, occupied, save, close - 1)
    return


shortest = 130001  # 100명, 거리100(사실 98), 병원13개가 최대
dfs(0, 0, m, h - m)
print(shortest)
