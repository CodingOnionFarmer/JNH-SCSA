# dfs
# 가지치기 요소는 많지 않고, set을 이용해서 중복 제거는 쉽게 할 수 있다.
# set에 str으로 넣는 것과 int로 변환해서 넣는 것 중 뭐가 더 효율적인지는 생각해 봐야 한다.

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
numbers = set()
chosen = [False] * n


def make(depth, made):
    if depth == k:
        numbers.add(made)
        return
    for idx, card in enumerate(cards):
        if not chosen[idx]:
            chosen[idx] = True
            make(depth + 1, made + card)
            chosen[idx] = False
    return


make(0, '')

print(len(numbers))
