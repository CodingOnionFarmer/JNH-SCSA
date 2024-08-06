a, b, c = int(input()), int(input()), int(input())
num = a * b * c
digit = [0] * 10
while num:
    digit[num % 10] += 1
    num //= 10

for i in range(10):
    print(digit[i])
