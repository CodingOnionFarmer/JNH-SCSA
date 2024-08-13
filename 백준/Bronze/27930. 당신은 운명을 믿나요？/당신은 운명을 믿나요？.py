y = 'YONSEI'
k = 'KOREA'
s = input()
p1 = 0
p2 = 0
for char in s:
    if char == y[p1]:
        p1 += 1
        if p1 == 6:
            print(y)
            break
    if char == k[p2]:
        p2 += 1
        if p2 == 5:
            print(k)
            break
