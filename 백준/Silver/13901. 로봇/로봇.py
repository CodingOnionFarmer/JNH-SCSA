# 구현, 시뮬레이션

# 조건 꼼꼼히 파악 : 장애물, 벽 뿐만 아니라 이미 지나간 칸도 못 지나간다.
# 지나간 칸을 장애물로 만들어버리면 될 것 같다.

import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

directions = ((), (-1, 0), (1, 0), (0, -1), (0, 1))  # 1위 2아래 3왼쪽 4오른쪽
r, c = map(int, input().split())
room = [[1] * c + [0] for _ in range(r)] + [[0] * c]  # 1이 지나갈 수 있는 곳, 0은 벽
k = int(input())
for obstacle in range(k):
    br, bc = map(int, input().split())
    room[br][bc] = 0
cr, cc = map(int, input().split())  # 현재 위치
cd = 0  # 현재 방향(의 index)
room[cr][cc] = 0
d_order = list(map(int, input().split()))  # 실제 방향은 directions[d_order[cd]]임
while True:
    for try_to_go in range(4):  # 4방향으로 이동 시도
        dr, dc = directions[d_order[cd]]
        nr, nc = cr + dr, cc + dc
        if room[nr][nc]:  # 현재 방향으로 갈 수 있으면 전진하고 시도 끝
            cr, cc = nr, nc
            room[cr][cc] = 0
            break
        cd = (cd + 1) % 4  # 전진 불가능하면 방향 전환
    else:  # 4번 시도 다 실패 시 종료
        break
print(cr, cc)
