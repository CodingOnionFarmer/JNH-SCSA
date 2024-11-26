from collections import deque

p, f = map(int, input().split())
pumps = list(map(int, input().split()))
pNow = 0
fNow = 0
now = 0
pumpsOnLeft = []
fireTrucks = list(map(int, input().split()))
connectedTrucksOnLeft = deque()
hose = 0
while pNow < p or fNow < f:
    if fNow == f:
        if not connectedTrucksOnLeft:
            break
        hose += pumps[pNow] - connectedTrucksOnLeft.popleft()
        pNow += 1
    elif pNow == p:
        connectedTrucksOnLeft.append(fireTrucks[fNow])
        hose += connectedTrucksOnLeft.popleft() - pumpsOnLeft.pop()
        fNow += 1
    elif pumps[pNow] <= fireTrucks[fNow]:
        if not connectedTrucksOnLeft:
            pumpsOnLeft.append(pumps[pNow])
            now = pNow + 1
        else:
            lastTruck = connectedTrucksOnLeft.pop()
            if len(pumpsOnLeft) > len(connectedTrucksOnLeft):
                pumpsOnLeft[-len(connectedTrucksOnLeft) - 1] += 2 * (pumps[pNow] - lastTruck)
            hose += pumps[pNow] - lastTruck
        pNow += 1
    else:
        connectedTrucksOnLeft.append(fireTrucks[fNow])
        if now == p:
            hose += connectedTrucksOnLeft.popleft() - pumpsOnLeft.pop()
        else:
            if pumpsOnLeft:
                left = connectedTrucksOnLeft[0] - pumpsOnLeft[-1]
                right = pumps[now] - connectedTrucksOnLeft[0]
                if left <= right:
                    hose += left
                    connectedTrucksOnLeft.popleft()
                    pumpsOnLeft.pop()
                else:
                    now += 1
            else:
                now += 1
        fNow += 1
print(hose)
