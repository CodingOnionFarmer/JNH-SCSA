l = int(input())
n = int(input())
cake = [True] * (l + 1)
most_expect = 0
most_get = 0
ans = [0, 0]
for i in range(n):
    p, k = map(int, input().split())
    expected = k - p + 1
    got = 0
    if expected > most_expect:
        most_expect = expected
        ans[0] = i + 1
    for num in range(p, k + 1):
        if cake[num]:
            got += 1
            cake[num] = False
    if got > most_get:
        most_get = got
        ans[1] = i + 1
print(ans[0])
print(ans[1])
