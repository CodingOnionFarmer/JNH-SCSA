n = int(input())
ramen = list(map(int, input().split()))
cost = sum(ramen) * 3
one = 0
two = 0
for i in range(n):
    r = ramen[i]
    new_two = min(one, r)
    cost -= new_two
    r -= new_two
    three = min(two, r)
    cost -= three
    one = r - three
    two = new_two
print(cost)
