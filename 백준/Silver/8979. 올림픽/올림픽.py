import sys

input = sys.stdin.readline

n, k = map(int, input().split())
medals = []

for i in range(n):
    nation, g, s, b = map(int, input().split())
    if nation == k:
        gold = g
        silver = s
        bronze = b
    else:
        medals.append((g, s, b))
rank = 1
for g, s, b in medals:
    if g > gold:
        rank += 1
        continue
    if g == gold:
        if s > silver:
            rank += 1
            continue
        if s == silver:
            if b > bronze:
                rank += 1
                continue
            pass
        pass
    pass
print(rank)
