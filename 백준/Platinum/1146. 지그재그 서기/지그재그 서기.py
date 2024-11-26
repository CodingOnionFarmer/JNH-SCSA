n = int(input())
if n == 1:
    print(1)
else:
    dp = [2, 2]
    for i in range(2, n + 1):
        m = 0
        for j in range(i // 2):
            c = dp[j] * dp[i - j - 1] // 2
            for k in range(j):
                c *= i - 1 - k
                c //= k + 1
            m += c
        if i % 2:
            c = dp[i // 2] ** 2 // 4
            for k in range(i // 2):
                c *= i - 1 - k
                c //= k + 1
            m += c
        dp.append(m % 1000000)
    print(dp[n])
