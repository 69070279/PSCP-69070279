"""[LEARNING LOGS] Giraffe"""

n = int(input())
count = 0
heights = []
for i in range(1, n+1):
    h = int(input())
    heights.append(h)
AMOUNT = len(heights)
for i in range (AMOUNT):
    if len(heights) == 1:
        count += 1
    if not i:
        if len(heights) > 1:
            if heights[i+1] < heights[i]:
                count += 1
    if i == n-1:
        if heights[i-1] < heights[i]:
            count += 1
    if i not in {0, n - 1}:
        if heights[i] > heights[i+1] and heights[i] > heights[i-1]:
            count +=1

print(count)
