# 퀵 정렬 (Quick Sort)
# index 기반으로 원본 리스트를 변화시키며 정렬하는 방식

n = int(input())
numbers = [int(input()) for _ in range(n)]


def quick_sort(start, end):  # start 인덱스부터 end 인덱스까지 퀵 정렬
    if start >= end:  # 종료 조건
        return
    pivot = numbers[start]  # 단위 동작
    p = start
    q = end
    while p < q:  # pivot보다 작거나 같은 건 왼쪽, 큰 건 오른쪽에 두면서 중간에서 만나기 기법
        while numbers[p] <= pivot and p < q:
            p += 1
        while numbers[q] > pivot:
            q -= 1
        if p < q:
            numbers[p], numbers[q] = numbers[q], numbers[p]
    numbers[start] = numbers[q]
    numbers[q] = pivot  # pivot을 기준으로 더 왼쪽에 있으면 작거나 같은 것, 오른쪽에 있으면 큰 것이다.
    quick_sort(start, q - 1)  # 하부 호출
    quick_sort(q + 1, end)


quick_sort(0, n - 1)
print(*numbers, sep='\n')
