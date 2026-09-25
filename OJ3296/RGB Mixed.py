"""สี"""
color1 = [int(x) for x in input().split()]
color2 = [int(x) for x in input().split()]
mixed_color = []
for i in range(3):
    avg = (color1[i] + color2[i]) // 2
    mixed_color.append(str(avg))
print(" ".join(mixed_color))
