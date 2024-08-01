n, m = map(int, input().split())
if n > m:
    n, m = m, n
length = 1
bit_dp = [[1], [0]]
# 한 줄 단위로 생각한다.
# 1은 밑으로 튀어나온 상태, 0은 안 튀어나온 상태이다.
# 윗줄에서 밑줄 순으로 탐색하므로, 위에서 튀어나온 상태(1)인 곳은 0이 되고,
# 단독으로 안 튀어나온 곳(0)은 1이 되고,
# 같이 안 튀어나온 곳(00)은 가로로 두면 묶어서 00이 될 수 있다.

while length < n:
    one_more_bit = [[] for _ in range(2 << length)]
    for bit in range(1 << length):
        if bit & 1:  # bit가 1로 끝남
            for next_line in bit_dp[bit]:
                one_more_bit[bit << 1].append((next_line << 1) + 1)  # 0으로 끝나는 것은 1밖에 안됨
                one_more_bit[(bit << 1) + 1].append(next_line << 1)  # 1로 끝나는 것은 0밖에 안됨
        else:  # bit가 0으로 끝남
            for next_line in bit_dp[bit]:
                one_more_bit[bit << 1].append((next_line << 1) + 1)  # 0으로 끝나는 것은 1로 끝날 수 있음
                one_more_bit[(bit << 1) + 1].append(next_line << 1)  # 1로 끝나는 것은 0밖에 안됨
                if next_line & 1:
                    # 0으로 끝나는데 맨오른쪽에 세로 도미노를 둬서 next_line은 1로 끝나는 경우
                    one_more_bit[bit << 1].append(next_line >> 1 << 2)
                    # 추가된 빈 칸(0)으로 가로 도미노로 바꿔서 다음 줄이 00으로 끝나게 할 수 있음
    bit_dp = one_more_bit
    length += 1

dp_size = 1 << n
dp = [0] * dp_size
dp[0] = 1  # 맨 윗줄보다 위에 가상의 000000으로 들어온 거라고 생각하기
for _ in range(m):
    next_dp = [0] * dp_size
    for i in range(dp_size):
        if dp[i]:
            for next_line in bit_dp[i]:
                next_dp[next_line] += dp[i]
    dp = next_dp
print(dp[0] % 9901)  # 맨 마지막 줄에서 밑이 울퉁불퉁하지 않고 000000으로 마감되어야 함
