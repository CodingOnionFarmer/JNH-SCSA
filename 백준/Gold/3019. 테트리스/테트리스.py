c, p = map(int, input().split())
height = list(map(int, input().split()))
if p == 1:
    ans = c
    # kmp가 스쳐지나갔지만 100에 4짜리니까 그냥 하기
    for i in range(c - 3):
        if height[i] == height[i + 1] == height[i + 2] == height[i + 3]:
            ans += 1
    print(ans)
else:
    ans = 0
    # 2칸짜리
    if p in (2, 6, 7):  # 2,6,7
        for i in range(c - 1):
            if height[i] == height[i + 1]:
                ans += 1
        if p == 6:
            for i in range(c - 1):
                if height[i] == height[i + 1] + 2:
                    ans += 1
        elif p == 7:
            for i in range(c - 1):
                if height[i] == height[i + 1] - 2:
                    ans += 1
    else:  # 3,4,5
        if p & 1:  # 3,5
            for i in range(c - 1):
                if height[i] == height[i + 1] + 1:
                    ans += 1
        if p > 3:  # 4,5
            for i in range(c - 1):
                if height[i] == height[i + 1] - 1:
                    ans += 1

    # 3칸짜리
    if p > 4:  # 5,6,7
        for i in range(c - 2):
            if height[i] == height[i + 1] == height[i + 2]:
                ans += 1
        if p == 5:
            for i in range(c - 2):
                if height[i] == height[i + 1] + 1 == height[i + 2]:
                    ans += 1
        elif p == 6:
            for i in range(c - 2):
                if height[i] + 1 == height[i + 1] == height[i + 2]:
                    ans += 1
        else:  # 7
            for i in range(c - 2):
                if height[i] == height[i + 1] == height[i + 2] + 1:
                    ans += 1
    elif p == 3:
        for i in range(c - 2):
            if height[i] == height[i + 1] == height[i + 2] - 1:
                ans += 1
    elif p == 4:
        for i in range(c - 2):
            if height[i] - 1 == height[i + 1] == height[i + 2]:
                ans += 1

    print(ans)
