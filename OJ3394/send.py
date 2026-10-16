"""Send Message"""

n, s = map(int, input().split())
students = []

for _ in range(n):
    students.append(int(input()))

visited = set()
current = s

while current and current not in visited:
    visited.add(current)
    current = students[current - 1]

print(len(visited))
