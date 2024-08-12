def white_and_blue(r, c, size):
    if size == 1:
        if paper[r][c]:
            return 0, 1
        return 1, 0
    half = size >> 1
    mr = r + half
    mc = c + half
    w = 0
    b = 0
    sw, sb = white_and_blue(r, c, half)
    w += sw
    b += sb
    sw, sb = white_and_blue(r, mc, half)
    w += sw
    b += sb
    sw, sb = white_and_blue(mr, c, half)
    w += sw
    b += sb
    sw, sb = white_and_blue(mr, mc, half)
    w += sw
    b += sb
    if w == 4 and not b:
        return 1, 0
    if not w and b == 4:
        return 0, 1
    return w, b


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = white_and_blue(0, 0, n)
print(white)
print(blue)
