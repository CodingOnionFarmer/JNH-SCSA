"""
시작 시간 : 3시 01분
제출 시간 : 3시 23분

"""

# tetra_minos = set()
# directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
# visited = set()
#
#
# def build_mino(depth, blocks):
#     if depth == 4:
#         tetra_minos.add(blocks)
#         return
#     if blocks in visited:
#         return
#     visited.add(blocks)
#     adj = set()
#     for ci, cj in blocks:
#         for di, dj in directions:
#             ni, nj = ci + di, cj + dj
#             if ni < 0 or (not ni and nj <= 0) or (ni, nj) in blocks:
#                 continue
#             adj.add((ni, nj))
#     for ni, nj in adj:
#         build_mino(depth + 1, tuple(sorted(list(blocks + ((ni, nj),)))))
#
#
# build_mino(1, ((0, 0),))
# print(tetra_minos)
# print(len(tetra_minos))
#
# tetra_minos = tuple([mino[1:] for mino in tetra_minos])
# print(tetra_minos)

# 검증 완료

tetra_minos = (
    ((0, 1), (1, 1), (1, 2)), ((0, 1), (0, 2), (0, 3)), ((1, 0), (1, 1), (2, 1)), ((0, 1), (0, 2), (1, 0)),
    ((1, -1), (1, 0), (1, 1)), ((0, 1), (1, 0), (1, 1)), ((1, 0), (2, -1), (2, 0)), ((0, 1), (0, 2), (1, 1)),
    ((1, 0), (1, 1), (1, 2)), ((1, 0), (2, 0), (2, 1)), ((0, 1), (0, 2), (1, 2)), ((1, -1), (1, 0), (2, -1)),
    ((1, -2), (1, -1), (1, 0)), ((1, 0), (2, 0), (3, 0)), ((1, 0), (1, 1), (2, 0)),
    ((1, -1), (1, 0), (2, 0)), ((0, 1), (1, -1), (1, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 1), (1, 0), (2, 0))
)

n, m = map(int, input().split())
board = [list(map(int, input().split())) + [0, 0, 0] for _ in range(n)] + [[0] * (m + 3) for _ in range(3)]
most = 0
for i in range(n):
    for j in range(m):
        temp = board[i][j]
        for (di1, dj1), (di2, dj2), (di3, dj3) in tetra_minos:
            temp_sum = temp + board[i + di1][j + dj1] + board[i + di2][j + dj2] + board[i + di3][j + dj3]
            if temp_sum > most:
                most = temp_sum
print(most)
