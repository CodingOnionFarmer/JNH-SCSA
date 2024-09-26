from collections import deque

T = int(input())
for tc in range(1, T + 1):
    n, m, k, a, b = map(int, input().split())
    a -= 1
    b -= 1
    ans = 0
    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))

    next_arrive_customer_idx = next_reception_customer_idx = 0
    repair_waiting_queue = deque()

    reception_ends = [-1] * n
    reception_who = [0] * n
    repair_ends = [0] * m

    used_A = [False] * k

    customers_arrival_time = list(map(int, input().split()))
    time = 0
    got_in_repair = 0
    while got_in_repair < k:
        # print('---------------------')
        # if time == 30:
        #     break
        while next_arrive_customer_idx < k:
            if customers_arrival_time[next_arrive_customer_idx] == time:
                next_arrive_customer_idx += 1
                continue
            break

        for reception_id, when_end in enumerate(reception_ends):
            if when_end == time:
                repair_waiting_queue.append(reception_who[reception_id])
                when_end = reception_ends[reception_id] = -1
            if when_end < time and next_reception_customer_idx < next_arrive_customer_idx:
                reception_who[reception_id] = next_reception_customer_idx
                reception_ends[reception_id] = time + reception_time[reception_id]
                if reception_id == a:
                    # print('a', next_reception_customer_idx)
                    used_A[next_reception_customer_idx] = True
                next_reception_customer_idx += 1

        for repair_id, when_end in enumerate(repair_ends):
            if when_end <= time and repair_waiting_queue:
                who = repair_waiting_queue.popleft()
                repair_ends[repair_id] = time + repair_time[repair_id]
                got_in_repair += 1
                if repair_id == b and used_A[who]:
                    # print('b', who)
                    ans += who + 1

        # print('시간', time)
        # print(next_arrive_customer_idx, '도착예정')
        # print(next_reception_customer_idx, '접수예정')
        # print(reception_ends)
        # print(repair_waiting_queue)
        # print(repair_ends)

        time += 1

    if not ans:
        ans -= 1

    print(f'#{tc}', ans)
