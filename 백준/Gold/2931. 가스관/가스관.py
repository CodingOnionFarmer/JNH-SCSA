dir_r = (0, 1, 0, -1)
dir_c = (1, 0, -1, 0)

opposite = (2, 3, 0, 1)

blocks = {
    '|': (1, 3),
    '-': (0, 2),
    '+': (0, 1, 2, 3),
    '1': (0, 1),
    '2': (0, 3),
    '3': (2, 3),
    '4': (1, 2)
}

r, c = map(int, input().split())
europe = [input() for _ in range(r)]


def solve():
    for i in range(r):
        for j in range(c):
            if europe[i][j] == '.':
                adj_gas = []
                for d in range(4):
                    ni, nj = i + dir_r[d], j + dir_c[d]
                    if ni < r and nj < c:
                        adj = europe[ni][nj]
                        if adj in blocks and opposite[d] in blocks[adj]:
                            adj_gas.append(d)
                if adj_gas:
                    check = tuple(adj_gas)
                    for block in blocks:
                        if blocks[block] == check:
                            print(i + 1, j + 1, block)
                            return


solve()
