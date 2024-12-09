import sys

input = sys.stdin.readline
print = sys.stdout.write

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)] + [['X'] * (c + 1)]
drop_stacks = [[] for _ in range(c)]
for j in range(c):
    for i in range(r):
        if board[i][j] == 'X':
            break
        drop_stacks[j].append((i, j))
n = int(input())
for _ in range(n):
    sj = int(input()) - 1
    ci, cj = drop_stacks[sj][-1]
    while board[ci][cj] == 'O':
        drop_stacks[sj].pop()
        ci, cj = drop_stacks[sj][-1]
    while True:
        below = board[ci + 1][cj]
        if below == '.':
            ci += 1
            drop_stacks[sj].append((ci, cj))
            continue
        if below == 'X':
            board[ci][cj] = 'O'
            drop_stacks[sj].pop()
            break
        if board[ci][cj - 1] == '.' and board[ci + 1][cj - 1] == '.':
            ci += 1
            cj -= 1
            drop_stacks[sj].append((ci, cj))
            continue
        if board[ci][cj + 1] == '.' and board[ci + 1][cj + 1] == '.':
            ci += 1
            cj += 1
            drop_stacks[sj].append((ci, cj))
            continue
        board[ci][cj] = 'O'
        drop_stacks[sj].pop()
        break

board.pop()
for line in board:
    print(''.join(line))
