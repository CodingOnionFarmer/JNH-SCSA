str1, str2 = input(), input()
n, m = len(str1), len(str2)
length = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(m):
        if str1[i] == str2[j]:
            length[i][j] = length[i - 1][j - 1] + 1
        else:
            length[i][j] = max(length[i - 1][j], length[i][j - 1])
print(length[n - 1][m - 1])
result = []
x, y = n - 1, m - 1
while length[x][y]:
    if length[x - 1][y] == length[x][y]:
        x -= 1
    elif length[x][y - 1] == length[x][y]:
        y -= 1
    else:
        result.append(str1[x])
        x -= 1
        y -= 1
result.reverse()
print(*result, sep='')
