"""555"""
n = int(input().strip())
def get_primes_up_to(limit):
    """ลิสปิ๊ม"""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [num for num, is_prime in enumerate(sieve) if is_prime]
primes_list = get_primes_up_to(n)
if n in primes_list:
    print("Yes")
    print(" ".join(map(str, primes_list)))
else:
    print("No")
