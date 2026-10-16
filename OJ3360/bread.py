"""หั่นขนมปัง"""

w, h, _, _ = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = [0] + x + [w]
y = [0] + y + [h]

widths = []
heights = []

for i in range(len(x) - 1):
    widths.append(x[i + 1] - x[i])

for i in range(len(y) - 1):
    heights.append(y[i + 1] - y[i])

max1 = 0
max2 = 0

for width in widths:
    for height in heights:
        area = width * height

        if area > max1:
            max2 = max1
            max1 = area
        elif area > max2:
            max2 = area

print(max1, max2)
