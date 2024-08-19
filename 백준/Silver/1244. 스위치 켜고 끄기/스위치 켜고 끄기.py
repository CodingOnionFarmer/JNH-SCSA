n = int(input())
switches = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    order, number = map(int, input().split())
    if order == 1:
        for i in range(number - 1, n, number):
            switches[i] ^= 1
    else:
        switches[number - 1] ^= 1
        left = number - 2
        right = number
        while left >= 0 and right < n:
            if switches[left] ^ switches[right]:
                break
            switches[left] ^= 1
            switches[right] ^= 1
            left -= 1
            right += 1
for line in range(0, n, 20):
    print(*switches[line:min(line + 20, n)])
