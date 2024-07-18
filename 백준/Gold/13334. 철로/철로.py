import sys

input = sys.stdin.readline

n = int(input())
home_and_office = []
for i in range(n):
    home_and_office.append(list(map(int, input().split())))
rail = int(input())
start = []
end = []
for i in range(n):
    home_and_office[i].sort()
    if home_and_office[i][1] - home_and_office[i][0] <= rail:
        start.append(max(-100000000, home_and_office[i][1] - rail))
        end.append(home_and_office[i][0])
start.sort()
end.sort()
start_idx = -1
end_idx = -1
m = len(start)
start.append(100000001)
end.append(100000001)
answer = 0
while start_idx < m and end_idx < m:
    if start_idx - end_idx > answer:
        answer = start_idx - end_idx
    if start[start_idx + 1] <= end[end_idx + 1]:
        start_idx += 1
    else:
        end_idx += 1
print(answer)
