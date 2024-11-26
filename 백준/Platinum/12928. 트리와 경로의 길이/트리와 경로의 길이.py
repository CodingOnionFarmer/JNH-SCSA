n, s = map(int, input().split())


def cnt(t):
    ans = 0
    for i in range(2, len(t)):
        ans += i * (i - 1) // 2 * t[i]
    return ans


def exclude(t, p):
    if cnt(t) + n - p > s:
        return True
    nt = list(t)
    nt[-1] -= 1
    for i in range(n - p - 1):
        nt.append(0)
    nt.append(1)
    if cnt(nt) < s:
        return True
    return False


if n < 3:
    if s:
        print(0)
    else:
        print(1)
else:
    dp = [set() for _ in range(n + 1)]
    dp[0].add((0,))
    dp[1].add((1,))
    dp[2].add((0, 2))
    for siz in range(3, n + 1):
        for tup in dp[siz - 1]:
            li = list(tup)
            li[1] += 1
            for j in range(1, len(li) - 1):
                if li[j]:
                    li[j] -= 1
                    li[j + 1] += 1
                    new = tuple(li)
                    if new not in dp[siz] and not exclude(new, siz):
                        dp[siz].add(new)
                    li[j] += 1
                    li[j + 1] -= 1
            li[-1] -= 1
            li.append(1)
            new = tuple(li)
            if new not in dp[siz] and not exclude(new, siz):
                dp[siz].add(new)
    found = False
    # for se in dp:
    #     print(se)
    for tup in dp[n]:
        if cnt(tup) == s:
            # print(tup)
            print(1)
            found = True
            break
    if not found:
        print(0)
