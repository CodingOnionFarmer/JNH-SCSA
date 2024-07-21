n = int(input())
ans = [0] * 10
size = len(str(n))
numbers = [(i + 1) * 10 ** i for i in range(size)]
remainder = 0
for i in range(size):
    r = n % 10
    n //= 10
    for num in range(10):
        ans[num] += n * 10 ** i
        if num < r:
            ans[num] += 10 ** i
        elif num == r:
            ans[num] += remainder + 1
    remainder += r * 10 ** i
    ans[0] -= 10 ** i
print(*ans)
