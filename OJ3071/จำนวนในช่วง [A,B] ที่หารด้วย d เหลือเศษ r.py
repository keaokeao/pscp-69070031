"""หาจำนวน"""
a = int(input())
b = int(input())
d = int(input())
r = int(input())
n = 0

while a <= b :
    if a % d == r :
        n += 1
    a += 1
print(n)
