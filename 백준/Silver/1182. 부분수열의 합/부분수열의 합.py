# 재귀함수, 깊이 우선 탐색 이용
# 예외처리 함정 하나 있음 (맨 뒤쪽)


n, s = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0


def dfs(idx, total):  # idx번 인덱스의 원소 탐색 중, 그 전까지 누적 합 total
    if idx == n:  # 모든 원소 탐색 끝
        if total == s:  # 정답 처리
            global cnt
            cnt += 1
        return
    dfs(idx + 1, total)  # idx번째 원소 미포함하고 다음 탐색
    dfs(idx + 1, total + numbers[idx])  # idx번째 원소 포함하고 다음 탐색
    return


dfs(0, 0)

# 아무것도 안 고르고 합이 0으로 정답처리된 경우 예외처리해야 한다.
# '크기가 양수인 부분수열 중에서' <- 문제를 잘 읽어야 한다.
if not s:
    cnt -= 1
print(cnt)
