height = [int(input()) for _ in range(9)]
height.sort()
ans = sum(height) - 100
p, q = 0, 8
while height[p] + height[q] != ans:
    if height[p] + height[q] < ans:
        p += 1
    else:
        q -= 1
for i in range(9):
    if i != p and i != q:
        print(height[i])
