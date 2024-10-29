while True:
    n, m = map(int, input().split())
    if not n:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    cs_by_line = [[0] * m for _ in range(n)]
    for i, line in enumerate(board):
        s = 0
        for j, digit in enumerate(line):
            if digit:
                s += 1
                cs_by_line[i][j] = s
                continue
            s = 0
    biggest_rect = 0
    for j in range(m):
        stack = []  # (가로길이, 시작 행) 튜플 넣어놓기
        for i in range(n):
            cs = cs_by_line[i][j]
            csi = i
            while stack:
                last = stack[-1][0]
                if last > cs:
                    last, si = stack.pop()
                    csi = si
                    if last * (i - si) > biggest_rect:
                        biggest_rect = last * (i - si)
                    continue
                if last == cs:
                    break
                stack.append((cs, csi))
                break
            if cs and not stack:
                stack.append((cs, csi))
        for width, si in stack:
            if width * (n - si) > biggest_rect:
                biggest_rect = width * (n - si)
    print(biggest_rect)
