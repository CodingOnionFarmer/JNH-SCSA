"""
240929
민코딩 : 커스텀 메인보드 생산
BOJ : 다리 만들기 2

시작 시간 : 2시 29분
구상 완료 : 2시 34분
제출 완료 : 2시 55분

"""

# 최소 스패닝 트리
# BFS

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

n, m = map(int, input().split())
oob = [[False] * m + [True] for _ in range(n)] + [[True] * m]
board = [list(map(int, input().split())) for _ in range(n)]
piece_num = 2
piece_distance = [[10] * 8 for _ in range(8)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            board[i][j] = piece_num
            q = [(i, j)]
            while q:
                nq = []
                for ci, cj in q:
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if oob[ni][nj] or board[ni][nj] == piece_num:
                            continue
                        if board[ni][nj]:
                            board[ni][nj] = piece_num
                            nq.append((ni, nj))
                        else:
                            ni += di
                            nj += dj
                            if oob[ni][nj] or board[ni][nj]:
                                continue
                            cable = 2
                            ni += di
                            nj += dj
                            while not oob[ni][nj]:
                                num = board[ni][nj]
                                if num:
                                    if num != 1 and num != piece_num:
                                        piece_distance[num][piece_num] = min(piece_distance[num][piece_num], cable)
                                    break
                                ni += di
                                nj += dj
                                cable += 1
                q = nq
            piece_num += 1

candidates = sorted([(piece_distance[i][j], i, j) for i in range(2, piece_num - 1) for j in range(i + 1, piece_num) if
                     piece_distance[i][j] != 10])
head = [i for i in range(piece_num)]
connection = 0
total_length = 0


def find(x):
    if head[x] == x:
        return x
    return find(head[x])


def union(x, y):
    hx = find(x)
    hy = find(y)
    head[hy] = hx


for d, i, j in candidates:
    if find(i) != find(j):
        connection += 1
        total_length += d
        union(i, j)
        if connection == piece_num - 3:
            print(total_length)
            break
else:
    print(-1)
