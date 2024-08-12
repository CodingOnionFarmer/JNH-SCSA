horizontal = [0] * 9
vertical = [0] * 9
square = [0] * 9

board = [list(map(int, input().split())) for _ in range(9)]
blank = 0
where_blank = []
for i in range(9):
    for j in range(9):
        num = board[i][j]
        if num:
            code = 1 << num
            horizontal[i] += code
            vertical[j] += code
            square[i // 3 * 3 + j // 3] += code
        else:
            blank += 1
            where_blank.append((i, j))

fill_blank = [0] * blank


def dfs(depth):
    if depth == blank:
        return True
    bi, bj = where_blank[depth]
    occupied = horizontal[bi] | vertical[bj] | square[bi // 3 * 3 + bj // 3]
    for number in range(1, 10):
        num_code = 1 << number
        if num_code & occupied:
            continue
        horizontal[bi] |= num_code
        vertical[bj] |= num_code
        square[bi // 3 * 3 + bj // 3] |= num_code
        fill_blank[depth] = number
        if dfs(depth + 1):
            return True
        horizontal[bi] ^= num_code
        vertical[bj] ^= num_code
        square[bi // 3 * 3 + bj // 3] ^= num_code
    return False


dfs(0)

for i in range(blank):
    bi, bj = where_blank[i]
    board[bi][bj] = fill_blank[i]

for line in board:
    print(*line)
