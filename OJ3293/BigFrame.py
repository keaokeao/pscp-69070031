"""กรอบ"""
lines = []
lines = []
for _ in range(5):
    lines.append(input())
max_len = 0
for l in lines:
    if len(l) > max_len:
        max_len = len(l)
if max_len < 2:
    inner_width = 2
else:
    inner_width = max_len
border_len = inner_width + 4
border = "*" * border_len
print(border)
for l in lines:
    spaces_needed = inner_width - len(l)
    padded = l + (" " * spaces_needed)
    print("* " + padded + " *")
print(border)
