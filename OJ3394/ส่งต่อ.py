"""ส่งต่อ"""
m = int(input())
n = int(input())
listm = []
listn = []
for _ in range(m) :
    code = int(input())
    listm.append(code)
for _ in range(n) :
    code = int(input())
    listn.append(code)
for _ in listm :
    for i in listn :
        if _ == i :
            print(i)
