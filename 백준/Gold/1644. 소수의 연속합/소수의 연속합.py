n = int(input())
if n < 3:
    print(n - 1)
elif n < 8:
    if n == 5:
        print(2)
    else:
        print(n % 2)
else:
    check = [False] * 2 + [True] * (n // 2 + 132)
    primes = []
    for i in range(2, n // 2 + 134):
        if check[i]:
            primes.append(i)
            j = 2
            while i * j <= n // 2 + 133:
                check[i * j] = False
                j += 1
    r = 0
    s = 0
    cnt = 0
    while s < n:
        s += primes[r]
        r += 1
    if s == n or s - 2 == n:
        cnt += 1
    y = r - 1
    x = 2
    s -= 5
    r -= 2
    if r == 1:
        print(cnt)
    else:
        while r > 2:
            while s < n:
                s -= primes[x]
                x += 1
                y += 1
                s += primes[y]
            if s == n:
                cnt += 1
            s -= primes[x]
            x += 1
            r -= 1
        t = len(primes) - 2
        s = primes[t] + primes[t + 1]
        while s > n:
            s -= primes[t + 1]
            t -= 1
            s += primes[t]
        if s == n:
            cnt += 1
        p = 2
        i = 0
        np = True
        while p * p <= n:
            if not n % p:
                np = False
                break
            i += 1
            p = primes[i]
        if np:
            cnt += 1
        print(cnt)
