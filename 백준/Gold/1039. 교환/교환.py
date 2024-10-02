# DFS
# Greedy

n, k = map(int, input().split())
digits = []
while n:
    digits.append(n % 10)
    n //= 10
digits.reverse()
d = len(digits)
maximal_arr = sorted(digits, reverse=True)
diff_cnt = 0
has_same_num = False
before = -1
end_flag = False
for i, digit in enumerate(maximal_arr):
    if digit == before:
        has_same_num = True
    before = digit
    if digit != digits[i]:
        diff_cnt += 1


def dfs(depth):
    global best
    if depth == k:
        if digits > best:
            best = digits[:]
        return
    global end_flag
    if end_flag:
        return
    for i in range(d):
        if digits[i] != maximal_arr[i]:
            for j in range(i + 1, d):
                if digits[j] == maximal_arr[i]:
                    digits[i], digits[j] = digits[j], digits[i]
                    dfs(depth + 1)
                    digits[i], digits[j] = digits[j], digits[i]
            break
    else:
        end_flag = True
        if k - depth & 1 and not has_same_num:
            best = maximal_arr[:]
            best[-1], best[-2] = best[-2], best[-1]
            return
        best = maximal_arr[:]
        return


if d == 1 or d == 2 and not maximal_arr[1]:
    print(-1)
else:
    if diff_cnt <= k + 1 and has_same_num:
        ans = 0
        for digit in maximal_arr:
            ans *= 10
            ans += digit
        print(ans)
    else:
        best = [0] * d
        dfs(0)
        ans = 0
        for digit in best:
            ans *= 10
            ans += digit
        print(ans)
