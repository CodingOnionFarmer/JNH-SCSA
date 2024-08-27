n = int(input())
amazing_primes = [2, 3, 5, 7]
odds = (1, 3, 5, 7, 9)
seed_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
is_prime = [False] * 10000
for sp in seed_primes:
    is_prime[sp] = True
for num in range(101, 9998):
    for p in seed_primes:
        if not num % p:
            break
    else:
        is_prime[num] = True
        primes.append(num)

for i in range(min(n - 1, 3)):
    new_ap = []
    for ap in amazing_primes:
        ap *= 10
        for odd in odds:
            if is_prime[ap + odd]:
                new_ap.append(ap + odd)
    amazing_primes = new_ap
for i in range(3, n - 1):
    new_ap = []
    for ap in amazing_primes:
        ap *= 10
        for odd in odds:
            temp = ap + odd
            for p in primes:
                if not temp % p:
                    break
            else:
                new_ap.append(temp)
    amazing_primes = new_ap
print(*amazing_primes, sep='\n')
