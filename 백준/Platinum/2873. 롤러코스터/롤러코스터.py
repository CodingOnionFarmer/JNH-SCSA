import os, io

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

r, c = map(int, input().split())
pleasure = [list(map(int, input().split())) for _ in range(r)]
move = []
if r & 1:
    for right_left in range(r >> 1):
        move.append('R' * (c - 1))
        move.append('D')
        move.append('L' * (c - 1))
        move.append('D')
    move.append('R' * (c - 1))
elif c & 1:
    for down_up in range(c >> 1):
        move.append('D' * (r - 1))
        move.append('R')
        move.append('U' * (r - 1))
        move.append('R')
    move.append('D' * (r - 1))
else:
    br = 0
    bc = 1
    lowest = pleasure[0][1]
    for i in range(r):
        is_i_even = 1 - (i & 1)
        for j in range(c >> 1):
            jj = (j << 1) + is_i_even
            if pleasure[i][jj] < lowest:
                br = i
                bc = jj
                lowest = pleasure[i][jj]
    if br & 1:
        for down_up in range(bc >> 1):
            move.append('D' * (r - 1))
            move.append('R')
            move.append('U' * (r - 1))
            move.append('R')
        move.append('RDLD' * (br >> 1))
        move.append('RD')
        move.append('DLDR' * ((r - br) >> 1))
        for up_down in range((c - bc - 2) >> 1):
            move.append('R')
            move.append('U' * (r - 1))
            move.append('R')
            move.append('D' * (r - 1))
    else:
        for right_left in range(br >> 1):
            move.append('R' * (c - 1))
            move.append('D')
            move.append('L' * (c - 1))
            move.append('D')
        move.append('DRUR' * (bc >> 1))
        move.append('DR')
        move.append('RURD' * ((c - bc) >> 1))
        for left_right in range((r - br - 2) >> 1):
            move.append('D')
            move.append('L' * (c - 1))
            move.append('D')
            move.append('R' * (c - 1))
print(*move, sep='')
