# Greedy Algorithm

n = int(input())
seq = list(map(int, input().split()))
lis = [seq[0]]
for num in seq:
    if num > lis[-1]:
        lis.append(num)
    else:
        for idx, sub_num in enumerate(lis):
            if sub_num >= num:
                lis[idx] = num
                break
print(len(lis))
