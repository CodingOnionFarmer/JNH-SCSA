# Dynamic Programming
# 포함 배제의 원리

dp09 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp08 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]
dp19 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
dp18 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 0]

n = int(input())
for i in range(n - 1):
    new_dp09 = [0] * 10
    new_dp08 = [0] * 10
    new_dp19 = [0] * 10
    new_dp18 = [0] * 10
    new_dp09[0] = dp09[1]
    new_dp09[9] = dp09[8]
    new_dp08[0] = dp08[1]
    new_dp08[8] = dp08[7]
    new_dp19[1] = dp19[2]
    new_dp19[9] = dp19[8]
    new_dp18[1] = dp18[2]
    new_dp18[8] = dp18[7]
    for j in range(1, 9):
        new_dp09[j] = (dp09[j - 1] + dp09[j + 1]) % 1000000000
    for j in range(1, 8):
        new_dp08[j] = (dp08[j - 1] + dp08[j + 1]) % 1000000000
    for j in range(2, 9):
        new_dp19[j] = (dp19[j - 1] + dp19[j + 1]) % 1000000000
    for j in range(2, 8):
        new_dp18[j] = (dp18[j - 1] + dp18[j + 1]) % 1000000000
    dp09 = new_dp09
    dp08 = new_dp08
    dp19 = new_dp19
    dp18 = new_dp18
print((sum(dp09) - sum(dp08) - sum(dp19) + sum(dp18)) % 1000000000)
