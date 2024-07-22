n = int(input())
numbers = [int(input()) for _ in range(n)]
k = int(input())
ten_remainder = [0] * (50 * n)
r = 1
for i in range(50 * n):
    ten_remainder[i] = r
    r *= 10
    r %= k
num_remainder = [numbers[i] % k for i in range(n)]  # 나머지
dp = [[0] * k for _ in range(1 << n)]  # dp[100111][3]은 0,1,2,5번째 수들을 붙여서 나머지가 3인 경우의 수
size = [len(str(numbers[i])) for i in range(n)]
dp_size = [0] * (1 << n)
cnt_one = [[] for _ in range(n + 1)]
for i in range(1 << n):
    one = 0
    temp = i
    for j in range(n):
        if temp & 1:
            one += 1
            dp_size[i] += size[j]
        temp >>= 1
    cnt_one[one].append(i)
dp[0][0] = 1
for c in range(n):  # c는 1의개수
    for b in cnt_one[c]:  # 1이 c개인 이진수 b
        for i in range(n):  # i번째 수가 포함 안된것들에 붙여서 dp 확장
            if not b & (1 << i):
                for j in range(k):  # 나머지가 j였던것에 추가
                    dp[b | (1 << i)][(j + ten_remainder[dp_size[b]] * num_remainder[i]) % k] += dp[b][j]
de = sum(dp[(1 << n) - 1])
nu = dp[(1 << n) - 1][0]
if not nu:
    print('0/1')
else:
    for prime in (2, 3, 5, 7, 11, 13):
        while not de % prime and not nu % prime:
            de //= prime
            nu //= prime
    print(f'{nu}/{de}')
