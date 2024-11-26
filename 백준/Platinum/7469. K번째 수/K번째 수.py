import sys


def ms(arr1, arr2):
    merged = []
    end = len(arr1)
    p1 = p2 = 0
    while p1 < end and p2 < end:
        if arr1[p1] < arr2[p2]:
            merged.append(arr1[p1])
            p1 += 1
        else:
            merged.append(arr2[p2])
            p2 += 1
    while p1 < end:
        merged.append(arr1[p1])
        p1 += 1
    while p2 < end:
        merged.append(arr2[p2])
        p2 += 1
    return merged


def lt(k, part):  # number of numbers in a part lower than k
    hi = len(part) - 1
    lo = 0
    mid = (hi + lo) // 2
    while lo < mid < hi:
        if part[mid] > k:
            hi = mid
        else:
            lo = mid
        mid = (hi + lo) // 2
    if mid < len(part) - 1 and part[mid + 1] < k:
        return mid + 2
    if part[mid] < k:
        return mid + 1
    return mid


input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
pieces = {1: [[arr[i]] for i in range(n)]}
l = n // 2
r = 1
while l:
    pieces[2 * r] = [ms(pieces[r][2 * i], pieces[r][2 * i + 1]) for i in range(l)]
    l //= 2
    r *= 2
# print(pieces)
for q in range(m):
    i, j, k = map(int, input().split())
    p = i - 1
    j -= 1
    k -= 1
    parts = []
    pl = 1  # parts length
    while pl <= j - p + 1:
        if p % (2 * pl):
            parts.append(pieces[pl][p // pl])
            p += pl
        pl *= 2
    # print(parts, pl)
    while p <= j and pl:
        if pl > j - p + 1:
            pl //= 2
        else:
            parts.append(pieces[pl][p // pl])
            p += pl
    answer = 0
    for x in range(len(parts)):
        lo = 0
        hi = len(parts[x]) - 1
        mid = (lo + hi) // 2
        found = False
        while lo < mid < hi:
            s = sum(lt(parts[x][mid], parts[y]) for y in range(len(parts)) if y != x)
            if s + mid == k:
                found = True
                answer = parts[x][mid]
                break
            elif s + mid > k:
                hi = mid
                mid = (lo + hi) // 2
            else:
                lo = mid
                mid = (lo + hi) // 2
        if not found:
            if mid < len(parts[x]) - 1 and sum(
                    lt(parts[x][mid + 1], parts[y]) for y in range(len(parts)) if y != x) + mid + 1 == k:
                found = True
                answer = parts[x][mid + 1]
            elif sum(lt(parts[x][mid], parts[y]) for y in range(len(parts)) if y != x) + mid == k:
                found = True
                answer = parts[x][mid]
            elif mid and sum(lt(parts[x][mid - 1], parts[y]) for y in range(len(parts)) if y != x) + mid - 1 == k:
                found = True
                answer = parts[x][mid - 1]
        if found:
            break
    print(answer)
