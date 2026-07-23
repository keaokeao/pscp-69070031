"""ผสมสี"""
first = input()
second = input()

if first == "Red" :
    if second == "Yellow" :
        print("Orange")
    elif second == "Blue" :
        print("Violet")
    elif second == "Red" :
        print("Red")
    else :
        print("Error")
elif first == "Yellow" :
    if second == "Red" :
        print("Orange")
    elif second == "Blue" :
        print("Green")
    elif second == "Yellow" :
        print("Yellow")
    else :
        print("Error")
elif first == "Blue" :
    if second == "Red" :
        print("Violet")
    elif second == "Yellow" :
        print("Green")
    elif second == "Blue" :
        print("Blue")
    else :
        print("Error")
else :
    print("Error")
