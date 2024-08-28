# reverse의 lds(감소하는부분수열)를 만들어서 뒤에서부터 세면 역으로 사전순으로 세어진다.

n, k = map(int, input().split())
lst = list(map(int, input().split()))
lst.reverse()
biggest_head = [lst[0]]
heads = [[lst[0]]]
bh = [[]]  # before head, 시작과 끝 둘 다 필요하므로 튜플로 넣기
ch = [[1]]  # case of head
cha = [[1]]  # case of head accumulative
for num in lst[1:]:
    # 마지막 위치의 마지막 머리보다 작으면, lds의 길이를 늘리는 해당 인덱스 최초의 멤버가 된다.
    if num < biggest_head[-1]:
        biggest_head.append(num)
        heads.append([num])
        # 직전 위치의 모두보다(제일 첫번째 것보다) 작을 경우
        if num < heads[-2][0]:
            bh.append([(0, len(heads[-2]) - 1)])
            ch.append([cha[-1][-1]])
            cha.append([ch[-1][0]])
        # 그렇지 않으면 누적합의 차(= 구간 합)로 해 줘야 됨
        else:
            b_left = 0
            b_right = len(heads[-2]) - 1
            while b_left < b_right:
                b_mid = (b_left + b_right) >> 1
                if heads[-2][b_mid] <= num:
                    b_left = b_mid + 1
                else:
                    b_right = b_mid
            bh.append([(b_right, len(heads[-2]) - 1)])
            ch.append([cha[-1][-1] - cha[-1][b_right - 1]])
            cha.append([ch[-1][0]])

    # 그렇지 않으면 기존 lds 어딘가에 편입
    else:
        left = 0
        right = len(biggest_head) - 1
        while left < right:
            mid = (left + right) >> 1
            if num < biggest_head[mid]:
                left = mid + 1
            else:
                right = mid
        # left = mid = right 번째에 편입됨.
        biggest_head[right] = num
        heads[right].append(num)
        if not right:
            ch[0].append(0)
            cha[0].append(cha[0][-1] + 1)
        # 0번째가 아닌 곳에 편입되면, 그 왼쪽에 몇 번째부터가 num보다 컸는지 따져봐야 됨.
        else:
            b_left = 0
            b_right = len(heads[right - 1]) - 1
            while b_left < b_right:
                b_mid = (b_left + b_right) >> 1
                if heads[right - 1][b_mid] <= num:
                    b_left = b_mid + 1
                else:
                    b_right = b_mid

            bh[right].append((b_right, len(heads[right - 1]) - 1))
            if b_right:
                ch[right].append(cha[right - 1][-1] - cha[right - 1][b_right - 1])
                cha[right].append(cha[right][-1] + ch[right][-1])
            else:
                ch[right].append(cha[right - 1][-1])
                cha[right].append(cha[right][-1] + ch[right][-1])

# 뒤에서 앞으로 찾을 차례, 이분탐색 안해도 됨
if k > cha[-1][-1]:
    print(-1)
else:
    ans = []
    sj, ej = 0, len(heads[-1]) - 1
    for idx in range(len(biggest_head) - 1, 0, -1):
        chi = ch[idx]
        hei = heads[idx]
        line = sj
        while k > chi[line]:
            k -= chi[line]
            line += 1
        ans.append(hei[line])

        while hei[sj] < hei[line]:
            sj += 1
        while hei[line] < hei[ej]:
            ej -= 1
        for j in range(sj, line):
            k += chi[j]
        cut = 0
        same = ej - sj + 1
        while same > 1 and k >= (chi[sj] - cut) * same:
            k -= (chi[sj] - cut) * same
            cut = chi[sj]
            same -= 1
            sj += 1
        k = (k - 1) // same + 1 + cut
        sj, ej = bh[idx][sj]
    ans.append(heads[0][sj + k - 1])
    print(*ans)
