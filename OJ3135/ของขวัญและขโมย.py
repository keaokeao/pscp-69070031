"""งงนะ"""
n, k, t = map(int, input().split(" "))
total = 1
now = 1
while now != t :
    now = now + k
    total += 1
    if now > n :
        now = now - n
    if now == 1 :
        total -= 1
        break
print(total)
