while True:
    tc = list(map(int, input().split()))
    n = tc[0]
    if not n:
        break
    stack = []
    biggest = 0
    for i in range(1, n + 1):
        idx = i
        while stack:
            if stack[-1][0] > tc[i]:
                height, idx = stack.pop()
                if height * (i - idx) > biggest:
                    biggest = height * (i - idx)
            else:
                break
        stack.append((tc[i], idx))
    while stack:
        height, idx = stack.pop()
        if height * (n - idx + 1) > biggest:
            biggest = height * (n - idx + 1)
    print(biggest)
