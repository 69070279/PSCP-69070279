"""ink"""

import math

s, n = map(int, input().split())

answer = []

for _ in range(n):
    x, y = map(int, input().split())
    time = 3.1416 * (x ** 2 + y ** 2) / s
    answer.append(math.ceil(time))

for result in answer:
    print(result)
