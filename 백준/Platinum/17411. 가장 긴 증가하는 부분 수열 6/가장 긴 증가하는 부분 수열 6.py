n = int(input())
lst = list(map(int, input().split()))
smallest_head = [lst[0]]
real_heads = [[]]
cases_of_head_accumulative = [[]]
cases_total = [0]

for num in lst:
    if num > smallest_head[-1]:
        smallest_head.append(num)
        if num > real_heads[-1][0]:
            real_heads.append([num])
            cases_of_head_accumulative.append([cases_total[-1]])
            cases_total.append(cases_total[-1])
            continue
        start = 0
        end = len(real_heads[-1]) - 1
        while start < end:
            mid = (start + end + 1) >> 1
            if num <= real_heads[-1][mid]:
                start = mid
                continue
            end = mid - 1
        real_heads.append([num])
        lis_cases = (cases_total[-1] - cases_of_head_accumulative[-1][end]) % 1000000007
        cases_of_head_accumulative.append([lis_cases])
        cases_total.append(lis_cases)
        continue
    if num <= smallest_head[0]:
        smallest_head[0] = num
        real_heads[0].append(num)
        cases_total[0] += 1
        cases_of_head_accumulative[0].append(cases_total[0])
        continue
    start = 0
    end = len(smallest_head) - 1
    while start < end:
        mid = (start + end) >> 1
        if num <= smallest_head[mid]:
            end = mid
            continue
        start = mid + 1
    head_idx = end
    smallest_head[head_idx] = num
    real_heads[head_idx].append(num)
    before_head = head_idx - 1
    if real_heads[before_head][0] < num:
        this_case = cases_total[before_head]
        cases_total[head_idx] += this_case
        cases_total[head_idx] %= 1000000007
        cases_of_head_accumulative[head_idx].append(cases_total[head_idx])
        continue
    start = 0
    end = len(real_heads[before_head]) - 1
    while start < end:
        mid = (start + end + 1) >> 1
        if num <= real_heads[before_head][mid]:
            start = mid
            continue
        end = mid - 1
    this_case = cases_total[before_head] - cases_of_head_accumulative[before_head][end]
    cases_of_head_accumulative[head_idx].append((cases_of_head_accumulative[head_idx][-1] + this_case) % 1000000007)
    cases_total[head_idx] += this_case
    cases_total[head_idx] %= 1000000007

print(len(smallest_head), cases_total[-1])
