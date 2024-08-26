d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))
hole_size = []
smallest = 1_000_000_000
for size in oven:
    if size < smallest:
        smallest = size
    hole_size.append(smallest)
bottom = d
for size in pizza:
    bottom -= 1
    while bottom >= 0 and hole_size[bottom] < size:
        bottom -= 1
    if bottom == -1:
        print(0)
        break
else:
    print(bottom + 1)
