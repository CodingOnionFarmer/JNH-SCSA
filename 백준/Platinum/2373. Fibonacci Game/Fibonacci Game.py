n = int(input())
a, b = 1, 1
fib = {1}
while b < n:
    a, b = b, a + b
    fib.add(b)
if n in fib:
    print(-1)
else:
    while n not in fib:
        n -= max(x for x in fib if x < n)
    print(n)