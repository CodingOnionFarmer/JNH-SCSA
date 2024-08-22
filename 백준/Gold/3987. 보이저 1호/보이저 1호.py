# 구현, 시뮬레이션

# 문제 서술이 굉장히 모호하다. 아주아주 맘에 안 든다.
# 문제 제한 조건에 시작점이 빈 칸이라는 서술이 없는데도,
# 시작점이 블랙홀이거나 행성이면 어쩌라는 건지 아무 말이 없다.
# 당연하게도 테케 중에도 없다.

# 시작점이 블랙홀이라 즉시 끝나서 답이 0일 수도 있는 건가?
# 그리고, 행성에서 시작해서 위로 쏘면 위로 쏴지는건가? 아니면 즉시 꺾여서 왼쪽이나 오른쪽으로 쏴지는건가?
# 일단 블랙홀에서 시작하면 즉시 끝나고, 행성에서 시작하면 쏘는 즉시 꺾인 방향으로 나간다고 생각해야겠다.
# 이것 때문에 틀리면 아주 화날 것 같다.....

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 위 오른 아래 왼
turn1 = (3, 2, 1, 0)
turn2 = (1, 0, 3, 2)

n, m = map(int, input().split())
galaxy = [list(input()) + ['C'] for _ in range(n)] + [['C'] * m]
pr, pc = map(int, input().split())
pr -= 1
pc -= 1
Voyager = False
longest_lifetime = 0
best = 0
d = ['U', 'R', 'D', 'L']
for i in range(4):
    if Voyager:
        break
    cr, cc, cd = pr, pc, i
    lifetime = 0
    visited = set()  # (r*m + c)*4 + d로 위치,방향을 정수 하나(100만 이하)로 요약한다.
    while True:
        now = galaxy[cr][cc]
        if now == 'C':
            break
        code = (cr * m + cc) * 4 + cd  # 패딩쳐놓은 C(외부)가 있으므로 C부터 검사하고 방문점 비교하기
        if code in visited:
            Voyager = True
            best = i
            break
        visited.add(code)
        if now == '\\':  # \앞에 \붙여줘야 됨에 유의
            cd = turn1[cd]
        elif now == '/':
            cd = turn2[cd]
        dr, dc = directions[cd]
        cr += dr
        cc += dc
        lifetime += 1
    if longest_lifetime < lifetime:
        longest_lifetime = lifetime
        best = i

print(d[best])
if Voyager:
    print('Voyager')
else:
    print(longest_lifetime)
