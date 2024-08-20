# 구현, 시뮬레이션

directions = ((0, 1), (1, 0), (0, -1), (-1, 0))  # 상 우 하 좌
turn_left = (3, 0, 1, 2)
turn_right = (1, 2, 3, 0)
for tc in range(int(input())):
    leftmost = rightmost = upmost = downmost = 0
    order = input()
    cx, cy, cd = 0, 0, 0
    for ch in order:
        if ch == 'F':
            dx, dy = directions[cd]
            cx += dx
            cy += dy
            leftmost = min(leftmost, cx)
            rightmost = max(rightmost, cx)
            upmost = max(upmost, cy)
            downmost = min(downmost, cy)
        elif ch == 'B':
            dx, dy = directions[cd]
            cx -= dx
            cy -= dy
            leftmost = min(leftmost, cx)
            rightmost = max(rightmost, cx)
            upmost = max(upmost, cy)
            downmost = min(downmost, cy)
        elif ch == 'L':
            cd = turn_left[cd]
        else:
            cd = turn_right[cd]
    print((upmost - downmost) * (rightmost - leftmost))
