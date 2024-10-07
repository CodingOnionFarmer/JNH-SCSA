directions = ((-1, 0), (0, -1), (1, 0), (0, 1))
eight_d = ((0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1))
ccw = (7, 0, 1, 2, 3, 4, 5, 6)

m, t = map(int, input().split())
monsters = [[[0] * 8 for _ in range(4)] for _ in range(4)]
dead_body = [[-3] * 4 for _ in range(4)]
oob = [[False] * 4 + [True] for _ in range(4)] + [[True] * 5]
for _ in range(m):
    r, c, d = map(int, input().split())
    r -= 1
    c -= 1
    d -= 1
    monsters[r][c][d] += 1
    
pi, pj = map(int, input().split())
pi -= 1
pj -= 1
    
for turn in range(t):
    copy_monsters = [[block[:] for block in line] for line in monsters]
    temp = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            for d, cnt in enumerate(monsters[i][j]):
                if not cnt:
                    continue
                for rotate_ccw_45 in range(8):
                    di, dj = eight_d[d]
                    ni, nj = i + di, j + dj
                    if oob[ni][nj] or (ni == pi and nj == pj) or dead_body[ni][nj] >= turn - 2:
                        d = ccw[d]
                        continue
                    temp[ni][nj][d] += cnt
                    break
                else:
                    temp[i][j][d] += cnt
    temp_cnt = [[sum(block) for block in line] for line in temp]
    most_kill = -1
    best_move = ((0, 0), (0, 0), (0, 0))

    for move1 in range(4):
        di1, dj1 = directions[move1]
        ni1, nj1 = pi + di1, pj + dj1
        if oob[ni1][nj1]:
            continue
        for move2 in range(4):
            di2, dj2 = directions[move2]
            ni2, nj2 = ni1 + di2, nj1 + dj2
            if oob[ni2][nj2]:
                continue
            for move3 in range(4):
                di3, dj3 = directions[move3]
                ni3, nj3 = ni2 + di3, nj2 + dj3
                if oob[ni3][nj3]:
                    continue
                kill = sum(temp_cnt[i][j] for i, j in {(ni1, nj1), (ni2, nj2), (ni3, nj3)})
                if kill > most_kill:
                    most_kill = kill
                    best_move = ((ni1, nj1), (ni2, nj2), (ni3, nj3))
    for i, j in best_move:
        if any(temp[i][j]):
            dead_body[i][j] = turn
            temp[i][j] = [0] * 8
    pi, pj = best_move[2]
    monsters = [[[copy_monsters[i][j][d] + temp[i][j][d] for d in range(8)] for j in range(4)] for i in range(4)]

print(sum(sum(sum(block) for block in line) for line in monsters))