"""Temperature"""

tem = float(input())
unit1 = input().lower()
unit2 = input().lower()
newtem = 0

if unit1 == "k":
    newtem = tem - 273.15
elif unit1 == "r":
    newtem = (tem - 491.67) * 5/9
elif unit1 =="f":
    newtem =(tem - 32) * 5/9
elif unit1 == "c":
    newtem = tem

if unit2 =="k":
    print(f"{(newtem + 273.15):.2f}")
elif unit2 =="r":
    print(f"{(newtem + 273.15) * 9/5:.2f}")
elif unit2 =="f":
    print(f"{(newtem * 9/5 +32):.2f}")
else:
    print(f"{newtem:.2f}")
