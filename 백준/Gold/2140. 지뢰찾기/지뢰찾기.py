# ?

n = int(input())
if n < 3:
    print(0)
elif n == 3:
    top_line = int(input())
    if top_line:
        print(1)
    else:
        print(0)
else:
    top_line = list(map(int, list(input())))
    leftmost = top_line[0]
    rightmost = top_line[-1]
    mine = leftmost + rightmost + (n - 4) ** 2
    left = leftmost
    left_left = 0
    for j in range(1, n - 3):
        left_left, left = left, top_line[j] - left - left_left
        mine += left
    leftmost_up = 0
    rightmost_up = 0
    for i in range(1, n - 3):
        ith_line = input()
        leftmost_up, leftmost = leftmost, int(ith_line[0]) - leftmost - leftmost_up
        mine += leftmost
        rightmost_up, rightmost = rightmost, int(ith_line[-1]) - rightmost - rightmost_up
        mine += rightmost
    input()
    input()
    bottom_line = list(map(int, list(input())))
    leftmost = bottom_line[0]
    rightmost = bottom_line[-1]
    mine += leftmost + rightmost
    left = leftmost
    left_left = 0
    for j in range(1, n - 3):
        left_left, left = left, bottom_line[j] - left - left_left
        mine += left
    print(mine)
