n, k = map(int, input().split())
digit = len(str(n))
nines = 10 ** (digit - 1) - 1
total_length = (n - nines) * digit
n = nines - 1
digit -= 1
while digit:
    small_nines = nines // 10
    total_length += (nines - small_nines) * digit
    nines = small_nines
    digit -= 1
if k > total_length:
    print(-1)
else:
    digit = 1
    digit_numbers = 9
    counted = 0
    while digit * digit_numbers + counted < k:
        counted += digit * digit_numbers
        digit += 1
        digit_numbers *= 10
    what_number = (k - counted - 1) // digit + 1
    number = 10 ** (digit - 1) - 1 + what_number
    what_idx = (k - counted - 1) % digit
    answer = str(number)[what_idx]
    print(answer)
