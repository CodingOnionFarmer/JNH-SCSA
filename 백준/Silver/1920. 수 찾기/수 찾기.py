# 이분 탐색, 이진 탐색 (Binary Search)
# Set 자료구조로 바꿔서 하면 O(n)에 되지만,
# 이분 탐색 연습을 위해 정렬(O(nlogn)) 이후 n번 이분 탐색(O(nlogn))하여 찾는다.


n = int(input())
lst = sorted(list(map(int, input().split())))  # 이분 탐색을 위해선 정렬이 필수
m = int(input())
find = list(map(int, input().split()))
result = [0] * m  # 결과를 10만 번 print하기보다는 모아서 print하는 게 함수 호출 횟수가 적어서 성능이 좋다.

for idx, number in enumerate(find):
    start = 0
    end = n - 1
    while start < end:
        mid = (start + end) >> 1
        if lst[mid] >= number:
            end = mid
        else:
            start = mid + 1
    # 이분 탐색이 종료된 후, lst[end](start도 end와 같다)는 number보다 크거나 같은 값 중 최솟값이다.
    # 그러므로 그 값이 number와 같으면 lst에 number가 존재하는 것이고, 아니면 없는 것이다.
    if lst[end] == number:
        result[idx] |= 1
print(*result, sep='\n')
