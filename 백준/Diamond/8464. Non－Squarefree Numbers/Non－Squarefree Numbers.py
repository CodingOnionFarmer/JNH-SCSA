k = int(input())
isprime = [False] * 2 + [True] * 199999
prime = []
for n in range(2, 200001):
    if isprime[n]:
        prime.append(n)
        for i in range(n ** 2, 200001, n):
            isprime[i] = False


def check(n):
    p = 0
    while prime[p] ** 2 <= n:
        if not n % prime[p] ** 2:
            return True
        p += 1
    return False


def bs(lo, hi, find):
    # print('이분탐색실행')
    # print(lo, hi, find)
    mid = (lo + hi) // 2
    order = 0
    p = 0
    while prime[p] ** 2 <= mid:
        order += mid // prime[p] ** 2
        p += 1
    p = 0
    # print('1차통과')
    while prime[p] ** 2 * prime[p + 1] ** 2 <= mid:
        q = p + 1
        while prime[p] ** 2 * prime[q] ** 2 <= mid:
            order -= mid // (prime[p] ** 2 * prime[q] ** 2)
            q += 1
        p += 1
    p = 0
    # print('2차통과')
    while prime[p] ** 2 * prime[p + 1] ** 2 * prime[p + 2] ** 2 <= mid:
        q = p + 1
        while prime[p] ** 2 * prime[q] ** 2 * prime[q + 1] ** 2 <= mid:
            r = q + 1
            while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 <= mid:
                order += mid // (prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2)
                r += 1
            q += 1
        p += 1
    p = 0
    # print('3차통과')
    while prime[p] ** 2 * prime[p + 1] ** 2 * prime[p + 2] * prime[p + 3] ** 2 <= mid:
        q = p + 1
        while prime[p] ** 2 * prime[q] ** 2 * prime[q + 1] ** 2 * prime[q + 2] ** 2 <= mid:
            r = q + 1
            while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[r + 1] ** 2 <= mid:
                s = r + 1
                while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 <= mid:
                    order -= mid // (prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2)
                    s += 1
                r += 1
            q += 1
        p += 1
    p = 0
    # print('4차통과')
    while prime[p] ** 2 * prime[p + 1] ** 2 * prime[p + 2] * prime[p + 3] ** 2 * prime[p + 4] ** 2 <= mid:
        q = p + 1
        while prime[p] ** 2 * prime[q] ** 2 * prime[q + 1] ** 2 * prime[q + 2] ** 2 * prime[q + 3] ** 2 <= mid:
            r = q + 1
            while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[r + 1] ** 2 * prime[r + 2] ** 2 <= mid:
                s = r + 1
                while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[s + 1] ** 2 <= mid:
                    t = s + 1
                    while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[t] ** 2 <= mid:
                        order += mid // (prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[t] ** 2)
                        t += 1
                    s += 1
                r += 1
            q += 1
        p += 1
    p = 0
    # print('5차통과')
    while prime[p] ** 2 * prime[p + 1] ** 2 * prime[p + 2] * prime[p + 3] ** 2 * prime[p + 4] ** 2 * prime[
        p + 5] ** 2 <= mid:
        q = p + 1
        while prime[p] ** 2 * prime[q] ** 2 * prime[q + 1] ** 2 * prime[q + 2] ** 2 * prime[q + 3] ** 2 * prime[
            q + 4] ** 2 <= mid:
            r = q + 1
            while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[r + 1] ** 2 * prime[r + 2] ** 2 * prime[
                r + 3] ** 2 <= mid:
                s = r + 1
                while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[s + 1] ** 2 * prime[
                    s + 2] ** 2 <= mid:
                    t = s + 1
                    while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[t] ** 2 * prime[
                        t + 1] ** 2 <= mid:
                        u = t + 1
                        while prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[t] ** 2 * prime[
                            u] ** 2 <= mid:
                            order -= mid // (
                                    prime[p] ** 2 * prime[q] ** 2 * prime[r] ** 2 * prime[s] ** 2 * prime[t] ** 2 *
                                    prime[u] ** 2)
                            u += 1
                        t += 1
                    s += 1
                r += 1
            q += 1
        p += 1
    # print(order)
    if order == find:
        while not check(mid):
            mid -= 1
        return mid
    if order > find:
        return bs(lo, mid, find)
    if hi - mid == 1:
        return hi
    return bs(mid, hi, find)


print(bs(k, 4 * k, k))
