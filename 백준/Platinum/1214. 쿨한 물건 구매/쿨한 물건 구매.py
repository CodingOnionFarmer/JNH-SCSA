def minimum_pay(price, big, small):
    payed_big = price // big
    remain = price % big
    if not remain:
        return price
    payed_big_only = big - remain
    if not remain % small:
        return price
    rremains = {remain % small}
    for i in range(payed_big):
        remain += big
        rremain = remain % small
        if not rremain:
            return price
        if rremain in rremains:
            return price + min(payed_big_only, small - max(rremains))
        rremains.add(rremain)
    return price + min(payed_big_only, small - max(rremains))


d, p, q = map(int, input().split())
if q > p:
    p, q = q, p

print(minimum_pay(d, p, q))
