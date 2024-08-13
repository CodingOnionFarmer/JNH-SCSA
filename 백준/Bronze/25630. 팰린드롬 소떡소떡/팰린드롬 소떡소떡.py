n = int(input())
stst = input()
ans = 0
for i in range(n >> 1):
    if stst[i] != stst[n - 1 - i]:
        ans += 1
print(ans)
