blank = 0
where_blank = []
real_blank = []
star_num = [0] * 12
num_occupied = 0
# lines = ((0, 2, 5, 7), (7, 8, 9, 10), (10, 6, 3, 0), (1, 2, 3, 4), (4, 6, 9, 11), (11, 8, 5, 1))
of_which_lines = ((0, 2), (3, 5), (0, 3), (2, 3), (3, 4), (0, 5), (2, 4), (0, 1), (1, 5), (1, 4), (1, 2), (4, 5))
lines_remain_cnt = [4] * 6
lines_sum = [0] * 6
idx = 0
magic_star = [list(input()) for _ in range(5)]
for i in range(5):
    for j in range(9):
        char = magic_star[i][j]
        if char == '.':
            continue
        if char == 'x':
            blank += 1
            where_blank.append(idx)
            real_blank.append((i, j))
        else:
            num = ord(char) - 65
            star_num[idx] = num
            num_occupied += 1 << num
            for line in of_which_lines[idx]:
                lines_remain_cnt[line] -= 1
                lines_sum[line] += num
        idx += 1


def dfs(depth, occupied):
    if depth == blank:
        return True
    fill = where_blank[depth]
    for number in range(12):
        if (1 << number) & occupied:
            continue
        line1, line2 = of_which_lines[fill]
        if lines_remain_cnt[line1] == 1 and lines_sum[line1] + number != 22:
            continue
        if lines_remain_cnt[line2] == 1 and lines_sum[line2] + number != 22:
            continue
        lines_remain_cnt[line1] -= 1
        lines_remain_cnt[line2] -= 1
        lines_sum[line1] += number
        lines_sum[line2] += number
        star_num[fill] = number
        if dfs(depth + 1, (1 << number) | occupied):
            return True
        lines_remain_cnt[line1] += 1
        lines_remain_cnt[line2] += 1
        lines_sum[line1] -= number
        lines_sum[line2] -= number
    return False


dfs(0, num_occupied)
for idx, (i, j) in enumerate(real_blank):
    num = star_num[where_blank[idx]]
    char = chr(num + 65)
    magic_star[i][j] = char
for line in magic_star:
    print(*line, sep='')
