import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def dfs(node, path_length):
    global longest, endpoints
    visited[node] = True
    next_nodes = [point for point in graph[node] if not visited[point]]
    if len(next_nodes) > 1:
        branches = [dfs(point, graph[node][point]) for point in next_nodes]
        branches.sort(reverse=True)
        if branches[0][0] + branches[1][0] > longest:
            longest = branches[0][0] + branches[1][0]
            endpoints = (branches[0][1], branches[1][1])
        return path_length + branches[0][0], branches[0][1]
    if next_nodes:
        return dfs(next_nodes[0], path_length + graph[node][next_nodes[0]])
    return path_length, node


def clean_path(node, endpoint):
    if node == endpoint:
        return True
    visited[node] = True
    next_nodes = [point for point in graph[node] if not visited[point]]
    if next_nodes:
        going_right = False
        for point in next_nodes:
            if going_right:
                visited[point] = True
            if clean_path(point, endpoint):
                going_right = True
        visited[node] = not going_right
        return going_right
    return False


n, m, l = map(int, input().split())
graph = [{} for _ in range(n)]
visited = [False] * n
longest_all = []
endpoints_all = []
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a][b] = t
    graph[b][a] = t
for node in range(n):
    if not visited[node]:
        longest = 0
        endpoints = ()
        pl, ep = dfs(node, 0)  # path_length, endpoint
        if pl > longest:
            longest = pl
            endpoints = (node, ep)
        if not longest:
            if graph[node]:
                for another_node in graph[node]:
                    longest = graph[node][another_node]
                    endpoints = (node, another_node)
            else:
                endpoints = (node, node)
        longest_all.append(longest)
        endpoints_all.append(endpoints)
if len(endpoints_all) == 1:
    print(longest_all[0])
else:
    longer_cuts = []
    visited = [False] * n
    for i in range(len(endpoints_all)):
        path_length = longest_all[i]
        if not path_length:
            longer_cuts.append(0)
        else:
            ep1, ep2 = endpoints_all[i]
            clean_path(ep1, ep2)
            shorter_than_half = 0
            longer_than_half = 0
            now = ep1
            found = False
            while not found:
                visited[now] = True
                for point in graph[now]:
                    if not visited[point]:
                        if shorter_than_half + graph[now][point] > path_length // 2:
                            longer_than_half = shorter_than_half + graph[now][point]
                            longer_cuts.append(min(longer_than_half, path_length - shorter_than_half))
                            found = True
                        else:
                            shorter_than_half += graph[now][point]
                            now = point
                        break
    longer_cuts.sort(reverse=True)
    longest_all.sort(reverse=True)
    if len(endpoints_all) == 2:
        print(max(longest_all[0], longer_cuts[0] + longer_cuts[1] + l))
    else:
        print(max(longest_all[0], longer_cuts[0] + longer_cuts[1] + l, longer_cuts[1] + longer_cuts[2] + 2 * l))
