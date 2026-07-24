"""color"""

def rgb():
    """ผสมแม่สี"""
    col1=input()
    col2=input()
    if col1 =="Red" and col2=="Blue":
        print("Violet")
    elif col1 =="Blue" and col2=="Red":
        print("Violet")
    elif col1 =="Red" and col2 == "Yellow":
        print("Orange")
    elif col1 =="Yellow" and col2 == "Red":
        print("Orange")
    elif col1 =="Blue" and col2 == "Yellow":
        print("Green")
    elif col1 =="Yellow" and col2 == "Blue":
        print("Green")
    elif col1 =="Red" and col2 == "Red":
        print("Red")
    elif col1 =="Blue" and col2 == "Blue":
        print("Blue")
    elif col1 =="Yellow" and col2 == "Yellow":
        print("Yellow")
    else:
        print("Error")
rgb()
