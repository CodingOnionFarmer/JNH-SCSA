def rev(number, idx):
    right_digit = (n - k - idx) * 3
    temp = number % (1 << right_digit)
    left_digit = (n - idx) * 3
    temp |= number >> left_digit << left_digit
    rev_num = 0
    number >>= right_digit
    for digit in range(k):
        rev_num <<= 3
        rev_num += number % 8
        number >>= 3
    return temp | (rev_num << right_digit)


n, k = map(int, input().split())
lst = list(map(int, input().split()))
goal = 0

for i in range(n):
    goal <<= 3
    goal |= i

s_num = 0
for d in lst:
    s_num <<= 3
    s_num |= d - 1

visited = {s_num}
q = [s_num]
step = 0

while q and goal not in visited:
    nq = []
    for num in q:
        for i in range(n - k + 1):
            r_num = rev(num, i)
            if r_num not in visited:
                nq.append(r_num)
                visited.add(r_num)
    step += 1
    q = nq

if goal in visited:
    print(step)
else:
    print(-1)
