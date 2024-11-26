n, b, c = map(int, input().split())
ramen = list(map(int, input().split()))
cost = sum(ramen) * b
if b > c:
    one = 0
    two = 0
    d = b-c
    for i in range(n):
        r = ramen[i]
        new_two = min(one, r)
        cost -= new_two * d
        r -= new_two
        three = min(two, r)
        cost -= three * d
        one = r - three
        two = new_two
print(cost)
