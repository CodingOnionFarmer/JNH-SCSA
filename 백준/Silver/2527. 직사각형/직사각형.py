for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    x_position = list({x1, p1, x2, p2})
    y_position = list({y1, q1, y2, q2})
    x_position.sort()
    y_position.sort()
    x1 = x_position.index(x1)
    p1 = x_position.index(p1)
    x2 = x_position.index(x2)
    p2 = x_position.index(p2)
    y1 = y_position.index(y1)
    q1 = y_position.index(q1)
    y2 = y_position.index(y2)
    q2 = y_position.index(q2)
    dots = [[False] * 4 for _ in range(4)]
    for i in range(x1, p1 + 1):
        for j in range(y1, q1 + 1):
            dots[i][j] = True
    overlapped = []
    for i in range(x2, p2 + 1):
        for j in range(y2, q2 + 1):
            if dots[i][j]:
                overlapped.append((i, j))
    if not overlapped:
        print('d')
    elif len(overlapped) == 1:
        print('c')
    elif overlapped[0][0] == overlapped[-1][0] or overlapped[0][1] == overlapped[-1][1]:
        print('b')
    else:
        print('a')
