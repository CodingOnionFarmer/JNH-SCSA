routes = [
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40],
    [10, 13, 16, 19, 25, 30, 35, 40],
    [20, 22, 24, 25, 30, 35, 40],
    [30, 28, 27, 26, 25, 30, 35, 40]
]
real_point = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [5, 21, 22, 23, 24, 25, 26, 20],
    [10, 27, 28, 24, 25, 26, 20],
    [15, 29, 30, 31, 24, 25, 26, 20]
]
point_occupied = [False] * 32
where_route = [0] * 4
where_idx = [0] * 4
best_score = 0

move_order = list(map(int, input().split()))


def dfs(depth, score, departed_units):
    global best_score
    if score + 40 * (10 - depth) <= best_score:
        return
    if depth == 10:
        best_score = score
        return
    move = move_order[depth]
    for unit in range(departed_units):
        r, i = where_route[unit], where_idx[unit]
        if r == 4:
            continue
        point = real_point[r][i]
        point_occupied[point] = False
        if i + move >= len(routes[r]):
            where_route[unit] = 4
            dfs(depth + 1, score, departed_units)
            where_route[unit] = r
            point_occupied[point] = True
        else:
            ni = i + move
            nr = r
            if not nr and ni in (5, 10, 15):
                nr = ni // 5
                ni = 0
            moved_point = real_point[nr][ni]
            if point_occupied[moved_point]:
                point_occupied[point] = True
                continue
            point_occupied[moved_point] = True
            where_route[unit] = nr
            where_idx[unit] = ni
            dfs(depth + 1, score + routes[nr][ni], departed_units)
            where_route[unit] = r
            where_idx[unit] = i
            point_occupied[moved_point] = False
            point_occupied[point] = True
    if departed_units < 4:
        if move == 5:
            r = 1
            i = 0
        else:
            r = 0
            i = move
        point = real_point[r][i]
        if not point_occupied[point]:
            point_occupied[point] = True
            where_route[departed_units] = r
            where_idx[departed_units] = i
            dfs(depth + 1, score + routes[r][i], departed_units + 1)
            point_occupied[point] = False
            where_route[departed_units] = 0
            where_idx[departed_units] = 0


dfs(0, 0, 0)
print(best_score)