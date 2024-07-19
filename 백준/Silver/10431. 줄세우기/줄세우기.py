p = int(input())
for tc in range(1, p + 1):
    tall = list(map(int, input().split()))
    ans = 0
    for i in range(1, 21):
        for j in range(1, i):
            if tall[i] < tall[j]:
                ans += 1
    print(tc, ans)
