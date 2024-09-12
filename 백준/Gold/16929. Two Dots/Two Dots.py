import sys

sys.setrecursionlimit(2501)

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
directions_except_before = ((0, 1, 3), (0, 1, 2), (1, 2, 3), (0, 2, 3), (0, 1, 2, 3))

n, m = map(int, input().split())
board = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for char in line:
        board[i].append(ord(char))
    board[i].append(0)
board.append([0] * m)
visited = [[False] * m for _ in range(n)]


def dfs(num, ci, cj, bd):
    for d in directions_except_before[bd]:
        di, dj = directions[d]
        ni, nj = ci + di, cj + dj
        if board[ni][nj] == num:
            if visited[ni][nj]:
                return True
            visited[ni][nj] = True
            if dfs(num, ni, nj, d):
                return True


def solve():
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                visited[i][j] = True
                if dfs(board[i][j], i, j, 4):
                    print('Yes')
                    return
    print('No')
    return


solve()
