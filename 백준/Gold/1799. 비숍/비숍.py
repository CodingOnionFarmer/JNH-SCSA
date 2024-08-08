n = int(input())
is_n_odd = n & 1
half = n >> 1
size = n * n
board = [list(map(int, input().split())) for _ in range(n)]


def dfs_even(depth, bishops, left_diagonal, right_diagonal):
    if depth == n:
        return bishops
    ban = left_diagonal | right_diagonal
    most = 0
    is_depth_even = 1 - (depth & 1)
    is_depth_even_and_n_odd = is_depth_even & is_n_odd
    for bit in range(1 << (half + is_depth_even)):
        if not bit & ban:
            temp_bishops = bishops
            for i in range(half + is_depth_even_and_n_odd):
                if (1 << i) & bit:
                    if not board[depth][2 * i + 1 - is_depth_even]:
                        break
                    temp_bishops += 1
            else:
                next_left_diagonal = left_diagonal | bit
                next_right_diagonal = right_diagonal | bit
                if is_depth_even:
                    next_left_diagonal >>= 1
                else:
                    next_right_diagonal <<= 1
                temp_most = dfs_even(depth + 1, temp_bishops, next_left_diagonal, next_right_diagonal)
                if temp_most > most:
                    most = temp_most
    return most


def dfs_odd(depth, bishops, left_diagonal, right_diagonal):
    if depth == n:
        return bishops
    ban = left_diagonal | right_diagonal
    most = 0
    is_depth_odd = depth & 1
    is_depth_odd_and_n_odd = is_depth_odd & is_n_odd
    for bit in range(1 << (half + is_depth_odd_and_n_odd)):
        if not bit & ban:
            temp_bishops = bishops
            for i in range(half + is_depth_odd):
                if (1 << i) & bit:
                    if not board[depth][2 * i + 1 - is_depth_odd]:
                        break
                    temp_bishops += 1
            else:
                next_left_diagonal = left_diagonal | bit
                next_right_diagonal = right_diagonal | bit
                if is_depth_odd:
                    next_left_diagonal >>= 1
                else:
                    next_right_diagonal <<= 1
                temp_most = dfs_odd(depth + 1, temp_bishops, next_left_diagonal, next_right_diagonal)
                if temp_most > most:
                    most = temp_most
    return most


print(dfs_even(0, 0, 0, 0) + dfs_odd(0, 0, 0, 0))
