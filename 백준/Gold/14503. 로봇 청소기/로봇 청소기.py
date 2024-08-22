# 구현, 시뮬레이션

# 내면의 평화 찾기
# Inner Peace

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북 동 남 서

n, m = map(int, input().split())
cr, cc, cd = map(int, input().split())
room = [list(map(int, input().split())) + [1] for _ in range(n)] + [[1] * m]
cleaned = 0
while True:
    if not room[cr][cc]:
        room[cr][cc] = 2
        cleaned += 1
    nd = cd
    for rotate in range(4):
        nd = (nd - 1) % 4
        dr, dc = directions[nd]
        nr, nc = cr + dr, cc + dc
        if not room[nr][nc]:
            cr, cc, cd = nr, nc, nd
            break
    else:
        bd = (cd + 2) % 4
        br, bc = directions[bd]
        nr, nc = cr + br, cc + bc
        if room[nr][nc] == 1:
            break
        cr, cc = nr, nc
print(cleaned)
