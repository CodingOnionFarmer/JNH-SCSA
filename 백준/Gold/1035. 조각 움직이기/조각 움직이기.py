directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

adj = [0] * 25
adj_digit = [[] for _ in range(25)]
for i in range(5):
    for j in range(5):
        num = i * 5 + j
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 5 and 0 <= nj < 5:
                adj[num] |= 1 << (ni * 5 + nj)
                adj_digit[num].append(ni * 5 + nj)

connected = {1 << h for h in range(25)}


def dfs(depth, number, head):
    if depth == 5:
        return
    for digit in range(head + 1, 25):
        bit = 1 << digit
        if bit & number:
            continue
        if adj[digit] & number:
            added = bit | number
            if added in connected:
                continue
            connected.add(added)
            dfs(depth + 1, added, head)


for h in range(25):
    dfs(1, 1 << h, h)

# 단위 테스트
# for c in connected:
#     check_board = [[0] * 5 for _ in range(5)]
#     for i in range(5):
#         for j in range(5):
#             if 1 << i * 5 + j & c:
#                 check_board[i][j] = 1
#     print('=============================')
#     for line in check_board:
#         print(line)

board = 0
for i in range(5):
    line = input()
    for j in range(5):
        board <<= 1
        if line[j] == '*':
            board |= 1


def solve():
    q = [board]
    visited = {board}
    move = 0
    while True:
        nq = []
        for moved_board in q:
            if moved_board in connected:
                print(move)
                return
            for digit in range(25):
                bit = 1 << digit
                if bit & moved_board:
                    for ad in adj_digit[digit]:
                        adj_bit = 1 << ad
                        if adj_bit & moved_board:
                            continue
                        new_board = moved_board ^ bit | adj_bit
                        if new_board not in visited:
                            visited.add(new_board)
                            nq.append(new_board)
        move += 1
        q = nq


solve()
