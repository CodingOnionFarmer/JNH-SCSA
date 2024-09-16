"""
240915
BOJ : 숨바꼭질 5

시작 시간 : 5시 36분
구상 완료 : 5시 38분
1회 오답 : 5시 41분 (시간 초과)
2회 오답 : 5시 44분 (시간 초과)
3회 오답 : 5시 57분 (시간 초과)
1일차 소요 시간 : 21분

240916
시작 시간 : 4시 59분
4회 오답 : 5시 27분 (시간 초과)
제출 시간 : 5시 43분
2일차 소요 시간 : 44분
총 소요 시간 : 65분

"""

# 가지치기
# 경우의 수 나누기
# 리팩토링

n, k = map(int, input().split())
# limit_speed = 0
# kk = k
# while kk <= 500000:
#     limit_speed += 1
#     kk += limit_speed
# max_k = kk - limit_speed
# limit_speed -= 1

reach_odd = [False] * 500001
reach_even = [False] * 500001
reach_even[n] = True
q = [n]
step = 0
while k < 500001:
    if step & 1:
        if reach_odd[k]:
            break
    elif reach_even[k]:
        break

    step += 1
    k += step
    nq = []

    if step & 1:
        for pos in q:
            for adj in (pos + 1, pos - 1, pos << 1):
                if 0 <= adj <= 500000 and not reach_odd[adj]:
                    reach_odd[adj] = True
                    nq.append(adj)
    else:
        for pos in q:
            for adj in (pos + 1, pos - 1, pos << 1):
                if 0 <= adj <= 500000 and not reach_even[adj]:
                    reach_even[adj] = True
                    nq.append(adj)
    q = nq

if k > 500000 or step & 1 and not reach_odd[k] or not step & 1 and not reach_even[k]:
    print(-1)
else:
    print(step)
