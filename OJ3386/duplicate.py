"""du"""

m = int(input())
n = int(input())

a = set()
b = set()

for _ in range(m):
    a.add(int(input()))

for _ in range(n):
    b.add(int(input()))

ans = sorted(a & b, reverse=True)

if ans:
    for i in ans:
        print(i)
else:
    print("Nope")
