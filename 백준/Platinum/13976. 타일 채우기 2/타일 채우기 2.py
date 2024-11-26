n = int(input())
if n % 2:
    print(0)
else:
    n //= 2
    n %= 500000003
    a = b = 1
    for _ in range(n):
        a, b = b, (4 * b - a) % 1000000007
    print(b)