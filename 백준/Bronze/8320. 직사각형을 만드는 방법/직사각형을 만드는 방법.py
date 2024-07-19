n = int(input())
ans = 0
for i in range(1, n + 1):
    if n // i < i:
        break
    ans += n // i - i + 1
print(ans)
