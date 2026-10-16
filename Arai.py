"""555"""
text_input = input().strip()
filtered_nums = []
for x in text_input.split():
    clean_x = x.lstrip('-')
    if clean_x.isdigit():
        num = int(x)
        if not num % 3 or not num % 5 :
            filtered_nums.append(num)
if not filtered_nums:
    print("Nope")
else:
    filtered_nums.reverse()
    for num in filtered_nums:
        print(num)
