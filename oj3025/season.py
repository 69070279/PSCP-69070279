"""season"""

month = int(input())
day = int(input())

if month <=3 :
    if month ==3 and day >=21 :
        print("spring")
    else :
        print("winter")
elif month <=6 :
    if month ==6 and day >=21 :
        print("summer")
    else :
        print("spring")
elif month <=9 :
    if month ==9 and day >=21 :
        print("fall")
    else :
        print("summer")
elif month <=12 :
    if month ==12 and day >=21 :
        print("winter")
    else :
        print("fall")
