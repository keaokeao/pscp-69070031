"""ลีลาศ"""
text = input().strip()
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
lonely_letters = []
for char, count in counts.items():
    if count % 2 != 0:
        lonely_letters.append(char)
if lonely_letters:
    print("".join(lonely_letters))
else:
    print("fully paired")
