import sys

input = sys.stdin.readline

n = int(input())
stack = []
ans = 0
for _ in range(n):
    height = int(input())
    while stack:
        if stack[-1][0] < height:
            ans += stack[-1][1]
            stack.pop()
        else:
            if stack[-1][0] == height and len(stack) == 1:
                break
            ans += 1
            break
    if stack and stack[-1][0] == height:
        ans += stack[-1][1]
        stack[-1][1] += 1
    else:
        stack.append([height, 1])
print(ans)
