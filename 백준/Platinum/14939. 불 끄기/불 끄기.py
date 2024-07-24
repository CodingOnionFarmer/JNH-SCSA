bulbs = [input() for _ in range(10)]
bit_bulbs = [0] * 10
for i in range(10):
    for bulb in bulbs[i]:
        bit_bulbs[i] <<= 1
        if bulb == 'O':
            bit_bulbs[i] += 1
press_cnt = [0] * 1024
actual_result = [0] * 1024
for trial in range(1024):
    check = 1
    if trial & check:
        press_cnt[trial] += 1
        actual_result[trial] = 3
    check <<= 1
    for digit in range(8):
        if trial & check:
            press_cnt[trial] += 1
            actual_result[trial] ^= 7 << digit
        check <<= 1
    if trial & check:
        press_cnt[trial] += 1
        actual_result[trial] ^= 3 << 8
best = 101
for trial in range(1024):
    before_line = 0
    next_line = trial
    ans = 0
    for i in range(10):
        ans += press_cnt[next_line]
        before_line, next_line = next_line, actual_result[next_line] ^ (bit_bulbs[i] ^ before_line)
    if not next_line and ans < best:
        best = ans
if best == 101:
    best = -1

print(best)
