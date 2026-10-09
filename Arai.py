"""hotel"""
n = int(input())
x = 0
while x != n :
    c = int(input())
    if c == -1 :
        break
    else :
        x += c
print(x)
