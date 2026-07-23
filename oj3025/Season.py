"""หาฤดูกาล"""
month = int(input())
day = int(input())
if not month % 3 :
    if month == 3 :
        if day >= 21 :
            print("spring")
        else :
            print("winter")
    elif month == 6 :
        if day >= 21 :
            print("summer")
        else :
            print("spring")
    elif month == 9 :
        if day >= 21 :
            print("fall")
        else :
            print("summer")
    elif month == 12 :
        if day >= 21 :
            print("winter")
        else :
            print("fall")
else :
    if month < 3 :
        print("winter")
    elif month < 6 :
        print("spring")
    elif month < 9 :
        print("summer")
    elif month < 12 :
        print("fall")
