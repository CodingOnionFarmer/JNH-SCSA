T = int(input())
for tc in range(1, T + 1):
    n, m, k, a, b = map(int, input().split())
    a -= 1
    b -= 1
    ans = 0
    reception_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))

    next_arrive_customer_idx = next_reception_customer_idx = next_repair_customer_idx = 0
    repair_waiting_queue = []

    reception_ends = [-1] * n
    reception_who = [0] * n
    repair_ends = [0] * m

    used_A = [False] * k

    customers_arrival_time = list(map(int, input().split()))
    time = 0
    got_in_repair = 0
    while got_in_repair < k:
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
                    used_A[next_reception_customer_idx] = True
                next_reception_customer_idx += 1

        for repair_id, when_end in enumerate(repair_ends):
            if when_end <= time and next_repair_customer_idx < len(repair_waiting_queue):
                who = repair_waiting_queue[next_repair_customer_idx]
                repair_ends[repair_id] = time + repair_time[repair_id]
                got_in_repair += 1
                if repair_id == b and used_A[who]:
                    ans += who + 1
                next_repair_customer_idx += 1

        time += 1

    if not ans:
        ans -= 1

    print(f'#{tc}', ans)
