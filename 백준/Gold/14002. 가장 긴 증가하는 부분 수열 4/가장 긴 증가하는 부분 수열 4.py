n = int(input())
seq = list(map(int, input().split()))
lis = [seq[0]]
before = [{}]


# index_dict = {}


def binary_search(start, end, target):
    if start == end:
        return end
    mid = (start + end) >> 1
    if lis[mid] >= target:
        return binary_search(start, mid, target)
    return binary_search(mid + 1, end, target)


for num in seq:
    if num > lis[-1]:
        before.append({})
        before[-1][num] = lis[-1]
        lis.append(num)
        # index_dict[num] = idx
    else:
        idx = binary_search(0, len(lis) - 1, num)
        lis[idx] = num
        if idx and num not in before[idx]:
            before[idx][num] = lis[idx - 1]

ans = len(lis)
real_lis = [0] * ans
now = lis[-1]
real_lis[-1] = now
for i in range(ans - 2, -1, -1):
    now = before[i+1][now]
    real_lis[i] = now

print(len(lis))
print(*real_lis)
