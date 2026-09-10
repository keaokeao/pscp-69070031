"""555"""
inputs = input().split(" ")
x = int(inputs[0])
k = inputs[1]
for i in range(x):
    row_chars = []
    for j in range(x):
        if i == j or i + j == x - 1:
            if k == '#':
                row_chars.append('#')
            else:
                center = x // 2
                distance = abs(i - center)
                char_code = ord(k) + center - distance
                row_chars.append(chr(char_code))
        else:
            row_chars.append('-')
    print("".join(row_chars))
