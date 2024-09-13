"""
BOJ : 청소년 상어

시작 시간 : 9시 38분
구상 완료 : 9시 42분
제출 시간 : 10시 22분


"""

# 브루트포스, 백트래킹

directions = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))

board = [[()] * 5 for _ in range(5)]
where_is_the_fish = [None for _ in range(17)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = (line[j << 1], line[j << 1 | 1] - 1)
        where_is_the_fish[line[j << 1]] = (i, j)

alive = [True] * 17
ans = board[0][0][0]
alive[ans] = False
board[0][0] = [-1, board[0][0][1]]


def fish_move(brd):
    temp = [[fish[:] for fish in line] for line in brd]
    originally_where = where_is_the_fish[:]
    for f in range(1, 17):
        if alive[f]:
            fi, fj = where_is_the_fish[f]
            fd = temp[fi][fj][1]
            for turn in range(8):
                di, dj = directions[fd]
                ni, nj = fi + di, fj + dj
                if not temp[ni][nj] or temp[ni][nj][0] == -1:
                    fd = (fd + 1) % 8
                    continue
                if temp[ni][nj][0] == 0:
                    temp[fi][fj] = (0, 0)
                    temp[ni][nj] = (f, fd)
                    where_is_the_fish[f] = (ni, nj)
                else:
                    temp[fi][fj], temp[ni][nj] = temp[ni][nj], (f, fd)
                    where_is_the_fish[f] = (ni, nj)
                    where_is_the_fish[temp[fi][fj][0]] = (fi, fj)
                break
    return temp, originally_where


def dfs(brd, si, sj, score):
    moved_brd, before_moved_where = fish_move(brd)
    can_move = []
    d = moved_brd[si][sj][1]
    di, dj = directions[d]
    for dist in range(1, 4):
        ni, nj = si + di * dist, sj + dj * dist
        if not moved_brd[ni][nj]:
            break
        if moved_brd[ni][nj][0]:
            can_move.append(dist)
    if not can_move:
        global ans
        if score > ans:
            ans = score
        for i in range(17):
            where_is_the_fish[i] = before_moved_where[i]
        return
    moved_brd[si][sj] = (0, 0)
    for dist in can_move:
        ni, nj = si + di * dist, sj + dj * dist
        fish, nd = moved_brd[ni][nj]
        moved_brd[ni][nj] = (-1, nd)
        alive[fish] = False
        dfs(moved_brd, ni, nj, score + fish)
        moved_brd[ni][nj] = (fish, nd)
        alive[fish] = True
    for i in range(17):
        where_is_the_fish[i] = before_moved_where[i]
    return


dfs(board, 0, 0, ans)
print(ans)
