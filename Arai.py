"""555"""
s = input().strip()
length = len(s)
s_list = [c.lower() for c in s]
if "buu" in "".join(s_list):
    max_u = 0
    for i in range(length):
        if s_list[i] == 'b':
            cnt, j = 0, i + 1
            while j < length and s_list[j] == 'u':
                cnt += 1
                j += 1
            if cnt >= 2 and cnt > max_u:
                max_u = cnt
    print("Yes", max_u)
elif "b" in s_list:
    idx = s_list.index('b')
    print(s[:idx + 1] + "U" * (length - idx - 1))
else:
    print(("BUU" * length)[:length])
