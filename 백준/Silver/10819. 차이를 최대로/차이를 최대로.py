# greedy
# 작은거 절반, 큰거 절반으로 나눠서 번갈아 배치하는 게 우월전략이다.
# 맨 끝에 오는 건 한 번만 비교되므로, 차가 가장 적은 조합으로 와야 한다.

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
S = 0
B = 0
for i in range(n >> 1):
    S += numbers[i]
    B += numbers[n - i - 1]

ans = (B - S) << 1
mid = n >> 1
if n & 1:
    ans -= min(numbers[mid] - numbers[mid - 1], numbers[mid + 1] - numbers[mid])
else:
    ans -= numbers[mid] - numbers[mid - 1]
print(ans)
