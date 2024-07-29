import sys

input = sys.stdin.readline
print = sys.stdout.write

sys.setrecursionlimit(10001)
v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
scc = []
stack = []
in_stack = [False] * (v + 1)
parameter = 0
visited_order = [-1] * (v + 1)


def dfs(node):
    global parameter
    parameter += 1
    visited_order[node] = parameter  # 각 노드는 dfs 탐색에서 방문 순의 id를 가짐
    stack.append(node)
    in_stack[node] = True

    parent_node_order = visited_order[node]
    for next_node in graph[node]:
        if visited_order[next_node] == -1:
            parent_node_order = min(parent_node_order, dfs(next_node))
        elif in_stack[next_node]:
            parent_node_order = min(parent_node_order, visited_order[next_node])

    # scc의 한 컴포넌트의 부모 노드에 해당하는 노드에서만 실행됨
    if parent_node_order == visited_order[node]:
        component = []
        while stack:
            node_in_component = stack.pop()
            in_stack[node_in_component] = False
            component.append(node_in_component)
            if node == node_in_component:
                break
        scc.append(component)

    # 여기서 return하는 값은 node가 속한 강한연결 컴포넌트의 부모(대표원소)의 id값
    return parent_node_order


for n in range(1, v + 1):
    if visited_order[n] == -1:
        dfs(n)
for component in scc:
    component.sort()
    component.append(-1)
scc.sort()
print(str(len(scc)) + '\n')
for component in scc:
    ans = ' '.join(map(str, component))
    print(ans + '\n')
