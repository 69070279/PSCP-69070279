"""castle"""

n = int(input())

row = 1

while n > row * row:
    row += 1

position = n - (row - 1) ** 2

if not position % 2:
    print(row * 2 - 3)
else:
    print(row * 2 - 2)
