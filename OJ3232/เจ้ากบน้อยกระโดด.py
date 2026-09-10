"""frog"""
x,y = map(int, input().split(" "))
far = 0
count = 0
while far < y :
    far += x
    x -= 2
    count += 1
    if x <= 0 and far < y :
        count = -1
        break
print(count)
