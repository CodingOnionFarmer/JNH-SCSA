board = [list(map(int, input().split())) for _ in range(5)]
position = [[] for _ in range(26)]
for i in range(5):
    for j in range(5):
        position[board[i][j]] = [i, j]
checked = [[False] * 5 for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))
bingo = 0
for idx, num in enumerate(numbers):
    r, c = position[num]
    checked[r][c] = True
    if all(checked[r][i] for i in range(5)):
        bingo += 1
    if all(checked[i][c] for i in range(5)):
        bingo += 1
    if r == c and all(checked[i][i] for i in range(5)):
        bingo += 1
    if r + c == 4 and all(checked[i][4 - i] for i in range(5)):
        bingo += 1
    if bingo >= 3:
        print(idx + 1)
        break
