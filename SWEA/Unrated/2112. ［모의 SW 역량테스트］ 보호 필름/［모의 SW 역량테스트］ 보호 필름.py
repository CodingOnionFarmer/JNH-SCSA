# 비트마스킹, BFS, 가지치기


def check(drug_ternary_bit):
    temp = film[:]
    for i in range(d):
        if drug_ternary_bit % 3:
            temp[i] = drug_layer[drug_ternary_bit % 3]
        drug_ternary_bit //= 3
    adj_exclusive = [temp[i] ^ temp[i + 1] for i in range(d - 1)]
    failed = full
    for i in range(d - k + 1):
        ae_accumulative = 0
        for j in range(i, i + k - 1):
            ae_accumulative |= adj_exclusive[j]
        failed &= ae_accumulative
    if failed:
        return False
    return True


def solve():
    if check(0):
        print(f'#{tc}', 0)
        return
    q = [(0, -1, 0)]
    for drug_layers in range(1, k):
        nq = []
        for dtb, last_layer, last_drug_rev in q:
            for next_layer in range(last_layer + 1, d):
                for drug in (1, 2):
                    if (next_layer < k - 1 or last_layer > d - k) and last_drug_rev == drug:
                        continue
                    next_dtb = dtb + three[next_layer] * drug
                    if check(next_dtb):
                        print(f'#{tc}', drug_layers)
                        return
                    nq.append((next_dtb, next_layer, 3 - drug))
        q = nq
    print(f'#{tc}', k)
    return


T = int(input())
for tc in range(1, T + 1):
    d, w, k = map(int, input().split())
    film = []
    for _ in range(d):
        line = list(map(int, input().split()))
        num = 0
        for char in line:
            num <<= 1
            num |= char
        film.append(num)
    if k == 1:
        print(f'#{tc}', 0)
        continue
    full = (1 << w) - 1
    three = tuple(3 ** i for i in range(d))
    drug_layer = (0, 0, full)
    solve()
