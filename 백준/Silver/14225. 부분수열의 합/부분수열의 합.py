n = int(input())
seq = sorted(list(map(int, input().split())))
s = 0
for num in seq:
    if num > s + 1:
        print(s + 1)
        break
    s += num
else:
    print(s + 1)
