column = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}
knight = ((2, 1), (1, 2))
visited = [False] * 36
valid = True
start = input()
si = ci = column[start[0]]
sj = cj = int(start[1]) - 1
now = ci * 6 + cj
visited[now] = True
for i in range(35):
    point = input()
    ni = column[point[0]]
    nj = int(point[1]) - 1
    move = ni * 6 + nj
    if visited[move] or (abs(ci - ni), abs(cj - nj)) not in knight:
        valid = False
        break
    visited[move] = True
    now = move
    ci = ni
    cj = nj
if (abs(ci - si), abs(cj - sj)) not in knight:
    valid = False
if valid:
    print('Valid')
else:
    print('Invalid')
