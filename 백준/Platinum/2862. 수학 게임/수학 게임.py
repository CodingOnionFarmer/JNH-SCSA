n = int(input())
a, b = 1, 1
fib = {1}
while b < n:
    a, b = b, a + b
    fib.add(b)
while n not in fib:
    n -= max(x for x in fib if x < n)
print(n)
