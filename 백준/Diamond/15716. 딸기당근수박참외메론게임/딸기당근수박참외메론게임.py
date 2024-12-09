n, b = map(int, input().split())
k, x = input().split()
x = int(x)
lst = list(input().split())
same = []
for i in range(len(lst)):
    if lst[i] == k:
        same.append(i)
nt = sum(n - i for i in same)


# l<=b
def cnt(l):
    m = l // n
    ans = m * nt
    ans += (m ** 2 - m) // 2 * len(same) * n
    ans += len(same) * (l % n) * m
    ans += sum(max(0, l % n - i) for i in same)
    return ans


def bs(l, h, f):
    m = (l + h) // 2
    if l == m:
        if m <= b:
            v = cnt(m)
        else:
            v = cycle - cnt(2 * (b - 1) - m + 1)
            if not same[0]:
                v += 1
        if v >= f:
            return m
        return h
    if m <= b:
        v = cnt(m)
    else:
        v = cycle - cnt(2 * (b - 1) - m + 1)
        if not same[0]:
            v += 1
    if v >= f:
        return bs(l, m, f)
    return bs(m, h, f)


half_cycle = cnt(b - 1)
cycle = cnt(b) + cnt(b - 1)
if not same[0]:
    cycle -= 1
if cycle:
    order = (x - 1) // cycle * 2 * (b - 1)
    x = (x - 1) % cycle + 1
    order += bs(1, 2 * (b - 1), x)
    print(order)
else:
    print(x)