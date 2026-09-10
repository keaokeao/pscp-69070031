"""ticket"""
a = input()
b = input()
if a[0] == b[0]:
    if a[2] == b[2] and a[3] == b[3] and a[4] == b[4] and a[5] == b[5] and a[6] == b[6] :
        print("1000000")
    elif a[4] == b[4] and a[5] == b[5] and a[6] == b[6] :
        print("2000")
    elif a[5] == b[5] and a[6] == b[6] :
        print("1000")
    else :
        print("20")
else :
    if a[2] == b[2] and a[3] == b[3] and a[4] == b[4] and a[5] == b[5] and a[6] == b[6] :
        print("100000")
    elif a[4] == b[4] and a[5] == b[5] and a[6] == b[6] :
        print("200")
    elif a[5] == b[5] and a[6] == b[6] :
        print("100")
    else :
        print("0")
