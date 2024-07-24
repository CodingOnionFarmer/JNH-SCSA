n = int(input())
paper = [0] * 100
for i in range(n):
    x, y = map(int, input().split())
    for j in range(y, y + 10):
        paper[j] |= 1023 << x
ans = 0
for num in paper:
    for _ in range(100):
        if num & 1:
            ans += 1
        num >>= 1
print(ans)
