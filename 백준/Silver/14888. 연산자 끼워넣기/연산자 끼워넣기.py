# dfs, 백트래킹, 브루트포스
# 현재까지의 값으로 가지치기를 하기는 어렵다.
# 쓸 수 있는 연산자의 개수가 남아 있을 때만 쓰는 식으로 모든 경우의 수를 다 탐색했다.


n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))
smallest = 1_000_000_000
biggest = -smallest


# depth번째 연산자를 뭐 넣을 지 결정하는 자리
# 그 왼쪽에 있는 식의 값 result
# 그 외에 4가지는 남은 +,-,*,// 연산자의 개수
def dfs(depth, result, plus, minus, multiply, divide):
    if depth == n:  # 종료조건
        global smallest, biggest
        if result < smallest:
            smallest = result
        if result > biggest:
            biggest = result
        return
    number = numbers[depth]  # 연산자를 넣어서 연산할 수
    # 연산자가 남아있는 것에 대해서 각각 실행해준다.
    if plus:
        dfs(depth + 1, result + number, plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, result - number, plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, result * number, plus, minus, multiply - 1, divide)
    if divide:  # 나눗셈 연산자는 Python과 규칙이 다르므로 경우를 나누어 실행해준다.
        if result >= 0:
            dfs(depth + 1, result // number, plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, -(-result // number), plus, minus, multiply, divide - 1)
    return


dfs(1, numbers[0], *operators)
print(biggest)
print(smallest)
