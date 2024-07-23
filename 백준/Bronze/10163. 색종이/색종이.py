n = int(input())
x_comp = [0] * 1002  # x,y 좌표 압축하기 위한 것
y_comp = [0] * 1002
papers = [list(map(int, input().split())) for _ in range(n)]
xs = set()
ys = set()
for i in range(n):
    xs.add(papers[i][0])
    papers[i][2] += papers[i][0]
    xs.add(papers[i][2])
    ys.add(papers[i][1])
    papers[i][3] += papers[i][1]
    ys.add(papers[i][3])
xl = list(xs)
yl = list(ys)
xl.sort()
yl.sort()
for idx, x in enumerate(xl):
    x_comp[x] = idx
for idx, y in enumerate(yl):
    y_comp[y] = idx
nx = len(xl)
ny = len(yl)
compressed_papers = [[-1] * (ny - 1) for _ in range(nx - 1)]
cp_size = [[(xl[i + 1] - xl[i]) * (yl[j + 1] - yl[j]) for j in range(ny - 1)] for i in range(nx - 1)]
papers_area = [0] * (n + 1)
for p in range(n):
    for cx in range(x_comp[papers[p][0]], x_comp[papers[p][2]]):
        for cy in range(y_comp[papers[p][1]], y_comp[papers[p][3]]):
            compressed_papers[cx][cy] = p
for cx in range(nx - 1):
    for cy in range(ny - 1):
        papers_area[compressed_papers[cx][cy]] += cp_size[cx][cy]
papers_area.pop()
for area in papers_area:
    print(area)
