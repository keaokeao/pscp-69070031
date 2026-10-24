"""Prime"""
n = int(input())
is_prime = True
if n <= 1:
    is_prime = False
elif n <= 3:
    is_prime = True
elif not n % 2  or not n % 3 :
    is_prime = False
else:
    limit = int(n ** 0.5)
    i = 5
    while i <= limit:
        if not n % i or not n % (i + 2) :
            is_prime = False
            break
        i += 6
if is_prime:
    print("YES")
else:
    print("NO")
