directions = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
players_position = [(0, 0)] * (m + 1)
monopoly = [line[:] + [0] for line in board] + [[0] * n]
when_monopoly = [[-k] * n + [1001] for _ in range(n)] + [[1001] * n]
for i in range(n):
    for j in range(n):
        if board[i][j]:
            players_position[board[i][j]] = (i, j)
            when_monopoly[i][j] = 1
players_direction = [0] + list(map(int, input().split()))
players_direction_priority = [[]] + [[[]] + [list(map(int, input().split())) for _ in range(4)] for _ in range(m)]
alive = {player for player in range(1, m + 1)}


def move(p):
    x, y = players_position[p]
    d = players_direction[p]
    d_to_my_monopoly = 0
    for nd in players_direction_priority[p][d]:
        dx, dy = directions[nd]
        nx, ny = x + dx, y + dy
        if when_monopoly[nx][ny] <= turn - k:
            players_position[p] = (nx, ny)
            players_direction[p] = nd
            other_p = temp[nx][ny]
            if other_p:
                if other_p > p:
                    dead.append(other_p)
                    temp[nx][ny] = p
                else:
                    dead.append(p)
            else:
                temp[nx][ny] = p
            return
        if not d_to_my_monopoly and monopoly[nx][ny] == p:
            d_to_my_monopoly = nd

    dx, dy = directions[d_to_my_monopoly]
    nx, ny = x + dx, y + dy
    temp[nx][ny] = p
    players_position[p] = (nx, ny)
    players_direction[p] = d_to_my_monopoly
    return


for turn in range(1, 1001):
    dead = []
    temp = [[0] * n for _ in range(n)]
    for player in alive:
        move(player)
    for dead_player in dead:
        alive.remove(dead_player)
    for player in alive:
        px, py = players_position[player]
        monopoly[px][py] = player
        when_monopoly[px][py] = turn + 1
    if len(alive) == 1:
        print(turn)
        break
    board = temp
else:
    print(-1)