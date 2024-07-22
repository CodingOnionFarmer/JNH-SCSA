n = int(input())

ans = 0
p = 1
s = 1
while s <= n:
    if not (n - s) % p:
        ans += 1
    p += 1
    s += p
print(ans)
