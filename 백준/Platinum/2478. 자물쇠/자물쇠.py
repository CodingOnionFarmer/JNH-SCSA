n = int(input())
locked = list(map(int, input().split())) * 2
start = 0

if locked[0] % n + 1 != locked[n - 1]:
    for i in range(n):
        if locked[i] == locked[i + 1] % n + 1:
            start = i
            break
else:
    for i in range(n - 1, -1, -1):
        if locked[i] % n + 1 != locked[i - 1]:
            start = i
            break

end = 2 * n - 1
for i in range(start + 1, 2 * n - 1):
    if locked[i] % n + 1 != locked[i - 1]:
        end = i - 1
        break

if not start and end == 2 * n - 1:
    p, q = 1, n
    if locked[n - 2] > 1:
        first_move = locked[n - 2] - 1
        second_move = 1
    else:
        first_move = n - 1
        second_move = 2
elif end >= n - 1:
    if locked[end] > 1:
        first_move = locked[end] - 1
        p, q = 1, end - start + 1
        second_move = n - start
    else:
        first_move = n - 1
        p, q = 2, end - start + 2
        second_move = n - start + 1
else:
    if locked[start] < n:
        first_move = locked[start]
        p, q = n - (end - start), n
        second_move = n - 1 - end
    elif end < n - 2:
        first_move = n - 2 - end
        p, q = start + 2, end + 2
        second_move = 1
    else:
        first_move = locked[end] - 1
        p, q = 1, end - start + 1
        second_move = n - start

print(first_move)
print(p, q)
print(second_move)
