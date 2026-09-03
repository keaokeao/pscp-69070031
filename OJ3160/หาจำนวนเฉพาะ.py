"""เฉพาะ"""
start, end = map(int, input().split())

primes = []

for num in range(start, end + 1):
    if num <= 1:
        continue
    total = 0
    for i in range(2, int(num**0.5) + 1):
        if not num % i:
            total += 1
            break
    if not total :
        primes.append(num)
    else:
        pass
if primes :
    print(*(primes))
print(f"Total primes: {len(primes)}")
