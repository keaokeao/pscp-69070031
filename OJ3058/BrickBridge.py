"""คำนวณอิฐ"""
a = int(input())
b = int(input())
goal = int(input())
bb = b * 5
if goal >= bb :
    remain = goal - bb
    if remain <= a :
        print(remain)
    else:
        print(-1)
else:
    remain = goal % 5
    if remain <= a :
        print(remain)
    else:
        print(-1)
