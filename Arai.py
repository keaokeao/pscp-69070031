"""555"""
import math
n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)
result = math.gcd(*numbers)
print(result)
