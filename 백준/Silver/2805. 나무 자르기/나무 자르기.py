# 누적 합(Prefix Sum), 이분 탐색(Binary Search)

# 아이디어 : 나무를 높이 순으로 정렬 후, 각 나무의 높이의 누적 합을 구해둔다.
# 나무 길이의 총합에서 i번째 나무까지의 누적 합을 빼고,
# 거기서 또 (i번째 나무의 높이) * (남은 나무의 수)만큼을 빼면,
# i번째 나무의 높이로 i보다 높은 나무(i+1부터 n-1번까지)들을 다 잘랐을 때 얻는 나무의 길이이다.
# 이를 이분 탐색으로 찾고, 얻은 나무 길이의 초과분을 (i+1번부터 n-1번까지 나무의 수)로 나눠서 그 만큼은 덜 잘라도 된다.


n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))
prefix_sum = [0] * n
total = 0
for idx, tree in enumerate(trees):
    total += tree
    prefix_sum[idx] = total
start = 0
end = n - 1
while start < end:
    mid = (start + end + 1) >> 1
    cut = total - prefix_sum[mid] - (n - mid - 1) * trees[mid]
    # cut의 관점에서는 인덱스에 대해 내림차순이다.
    # (더 높은 나무 높이로 자르면 자른 총 길이가 줄어드므로)
    if cut < m:
        end = mid - 1
    else:
        start = mid

# 예외처리할 것 : 찾은 나무가 처음이자 마지막 나무이거나 첫 나무일 경우
if end == n - 1:  # n이 1일 때는 zerodivisionerror를 피하기 위해 예외처리한다.
    print(trees[end] - m)
else:
    height = trees[end]  # 자르려는 기준 나무의 높이 (end+1번 나무 높이로 자르면 모자라다)
    cut = total - prefix_sum[end] - (n - end - 1) * trees[end]  # 그 나무 높이로 잘랐을 때 총량
    if cut >= m:
        height += (cut - m) // (n - end - 1)  # 총량 초과분을 자르는 나무 개수로 나눠서 그 만큼 높이는 덜 잘라도 된다.
    else:  # cut이 m보다 적으면, (당연히 end=0이고) 처음 나무보다도 낮은 높이로 잘라야 될 경우이므로 예외처리가 필요하다.
        height += (cut - m) // n
        # height -= (m - cut) // n으로 하면 다른 결과가 나올 수 있으므로 주의해야 한다!!
        # m - cut이 n의 배수가 아니면 m보다 모자라게 자르게 되기 때문이다.
    print(height)
