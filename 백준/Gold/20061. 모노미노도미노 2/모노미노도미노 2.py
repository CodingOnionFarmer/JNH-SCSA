import sys

input = sys.stdin.readline

yellow = 0
red = 0
score = 0
y_type = (0, 65536, 196608, 1114112)
r_type = (0, 65536, 1114112, 196608)
check = (15, 240, 3840, 61440)
erase_down = (0, 15, 255, 4095)
over_check = 65536

k = int(input())
for _ in range(k):
    t, x, y = map(int, input().split())
    y_bit = (1 << y) * y_type[t]
    r_bit = (1 << x) * r_type[t]

    for down in range(4):
        if y_bit >> 4 & yellow:
            break
        y_bit >>= 4
    yellow |= y_bit
    erase = []
    for i, check_bit in enumerate(check):
        if yellow & check_bit == check_bit:
            erase.append(i)
    while erase:
        score += 1
        i = erase.pop()
        yellow = (yellow & erase_down[i]) | (yellow >> (i * 4 + 4) << (i * 4))
    while yellow >= over_check:
        yellow >>= 4

    for down in range(4):
        if r_bit >> 4 & red:
            break
        r_bit >>= 4
    red |= r_bit
    erase = []
    for i, check_bit in enumerate(check):
        if red & check_bit == check_bit:
            erase.append(i)
    while erase:
        score += 1
        i = erase.pop()
        red = (red & erase_down[i]) | (red >> (i * 4 + 4) << (i * 4))
    while red >= over_check:
        red >>= 4

blocks = 0
for _ in range(16):
    blocks += yellow & 1
    yellow >>= 1
    blocks += red & 1
    red >>= 1

print(score)
print(blocks)