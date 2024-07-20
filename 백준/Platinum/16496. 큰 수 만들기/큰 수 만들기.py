n = int(input())
numbers = list(input().split())
if all(not int(num) for num in numbers):
    print(0)
else:
    separated = [[10] * 21 for _ in range(n)]
    for i in range(n):
        digit = len(numbers[i])
        separated[i][20] = digit
        for j in range(20):
            separated[i][j] = int(numbers[i][j % digit])
    separated.sort(reverse=True)
    for i in range(n):
        for j in range(separated[i][20]):
            print(separated[i][j], end='')
