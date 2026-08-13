"""divine10"""
N = int(input())

for i in range(N, -1, -1):
    if not i % 10:
        print(i, end=" ")
