"""ย่อ"""
numbers = []
num = int(input())
while num != -1:
    numbers.append(num)
    num = int(input())
if numbers:
    result = []
    start = numbers[0]
    end = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] == end + 1:
            end = numbers[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")
            start = numbers[i]
            end = numbers[i]
    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")
    print(", ".join(result))