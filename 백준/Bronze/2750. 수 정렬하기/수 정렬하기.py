# 병합 정렬 (Merge Sort)

n = int(input())
numbers = [int(input()) for _ in range(n)]


def merge_sort(start, end):  # 인덱스 start부터 end까지 재귀적으로 병합정렬한다.
    if start == end:  # 종료 조건
        return
    mid = (start + end) // 2
    merge_sort(start, mid)  # 하부 호출(왼쪽)
    merge_sort(mid + 1, end)  # 하부 호출(오른쪽)
    
    # 하부 호출을 한 뒤, 그 결과물을 이용해서 단위 동작
    # 정렬된 상태의 두 리스트를 병합하여 O(n)에 정렬한다.
    # 병합은 약 logn번 이루어지므로, 병합 정렬의 전체 시간복잡도는 O(nlogn)이다.
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


merge_sort(0, n - 1)
print(*numbers, sep='\n')
