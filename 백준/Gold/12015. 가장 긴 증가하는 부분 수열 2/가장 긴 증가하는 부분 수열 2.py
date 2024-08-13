n = int(input())
seq = list(map(int, input().split()))
lis = [seq[0]]


def binary_search(start, end, target):
    if start == end:
        return end
    mid = (start + end) >> 1
    if lis[mid] >= target:
        return binary_search(start, mid, target)
    return binary_search(mid + 1, end, target)


for num in seq:
    if num > lis[-1]:
        lis.append(num)
    else:
        idx = binary_search(0, len(lis) - 1, num)
        lis[idx] = num
print(len(lis))
