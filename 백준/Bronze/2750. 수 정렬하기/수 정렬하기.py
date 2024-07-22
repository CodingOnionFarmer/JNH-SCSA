n = int(input())
numbers = [int(input()) for _ in range(n)]


def quick_sort(start, end):
    if start == end:
        return
    mid = (start + end) // 2
    quick_sort(start, mid)
    quick_sort(mid + 1, end)
    p1 = start
    p2 = mid + 1
    temp = []
    while p1 <= mid and p2 <= end:
        if numbers[p1] <= numbers[p2]:
            temp.append(numbers[p1])
            p1 += 1
        else:
            temp.append(numbers[p2])
            p2 += 1
    while p1 <= mid:
        temp.append(numbers[p1])
        p1 += 1
    while p2 <= end:
        temp.append(numbers[p2])
        p2 += 1
    for i in range(end - start + 1):
        numbers[start + i] = temp[i]
    return


quick_sort(0, n - 1)
for num in numbers:
    print(num)
