"""TAM"""
count = int(input())
total = 0
for _ in range(count) :
    x = input()
    if x == "+" :
        total += 10
    elif x == "-" :
        total -= 5
print(total)
