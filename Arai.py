"""555"""
n = int(input())
max_values = []
total = 0
for _ in range(n):
    a = int(input())
    b = int(input())
    if a >= b:
        max_values.append(a)
        total += a
    else:
        max_values.append(b)
        total += b
if n == 1:
    print(total)
else:
    EXPRESSION = " + ".join(map(str, max_values))
    print(f"{EXPRESSION} = {total}")
