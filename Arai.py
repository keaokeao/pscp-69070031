"""555"""
col,amo = input().split(" ")
amo = int(amo)
group = amo // 3
mod = amo % 3
R = "Red Green Blue "
G = "Green Blue Red "
B = "Blue Red Green "
if col == "R" :
    if mod == 2 :
        print(f"{R * group}Red Green")
    elif mod == 1 :
        print(f"{R * group}Red")
    else :
        print(R * group)
elif col == "G" :
    if mod == 2 :
        print(f"{G * group}Green Blue")
    elif mod == 1 :
        print(f"{G * group}Green")
    else :
        print(G * group)
elif col == "B" :
    if mod == 2 :
        print(f"{B * group}Blue Red")
    elif mod == 1 :
        print(f"{B * group}Blue")
    else :
        print(B * group)
