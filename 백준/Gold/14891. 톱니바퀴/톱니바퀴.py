"""
시작 시간 : 3시 26분
제출 시간 : 4시 25분

"""


def clockwise(number):
    head = number & 1
    return (head << 7) | (number >> 1)


def counter_clockwise(number):
    tail = number & 128
    return ((number ^ tail) << 1) | (tail >> 7)


def is_connected(left, right):
    return ((left >> 4) ^ right) & 2


saw = []
rotate = [None, clockwise, counter_clockwise]
connected = []
for i in range(4):
    temp = input()
    num = 0
    for digit in temp:
        num <<= 1
        num |= int(digit)
    saw.append(num)

connected = [is_connected(saw[i], saw[i + 1]) for i in range(3)]

k = int(input())
for order in range(k):
    idx, r = map(int, input().split())
    idx -= 1
    saw[idx] = rotate[r](saw[idx])
    if not idx:
        for j in range(3):
            r = -r
            if not connected[j]:
                break
            saw[j + 1] = rotate[r](saw[j + 1])
    elif idx == 1:
        if connected[0]:
            saw[0] = rotate[-r](saw[0])
        for j in range(1, 3):
            r = -r
            if not connected[j]:
                break
            saw[j + 1] = rotate[r](saw[j + 1])
    elif idx == 2:
        if connected[2]:
            saw[3] = rotate[-r](saw[3])
        for j in range(1, -1, -1):
            r = -r
            if not connected[j]:
                break
            saw[j] = rotate[r](saw[j])
    else:
        for j in range(2, -1, -1):
            r = -r
            if not connected[j]:
                break
            saw[j] = rotate[r](saw[j])
    connected = [is_connected(saw[i], saw[i + 1]) for i in range(3)]

score = (saw[3] >> 7 << 3) | (saw[2] >> 7 << 2) | (saw[1] >> 7 << 1) | (saw[0] >> 7)
print(score)
