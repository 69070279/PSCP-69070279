"""bill"""

food = int(input())
service = food * 0.10

if service < 50:
    service = 50
elif service > 1000:
    service = 1000

total = food + service
total = total * 1.07

print(f"{total:.2f}")
