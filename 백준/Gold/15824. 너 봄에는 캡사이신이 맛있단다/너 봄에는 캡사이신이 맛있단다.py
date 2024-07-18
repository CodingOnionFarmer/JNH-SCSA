n = int(input())
scov = list(map(int, input().split()))
scov.sort()
answer = 0
power_of2_minus1 = [0]
num = 0
for i in range(n):
    num *= 2
    num += 1
    num %= 1000000007
    power_of2_minus1.append(num)
for p in range(1, n):
    answer += (scov[p] - scov[p - 1]) * power_of2_minus1[p] * power_of2_minus1[n - p]
    answer %= 1000000007
print(answer)
