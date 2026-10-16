"""Shorten"""

start = None
end = None
ans = []

while True:
    data = input().split()

    for x in data:
        n = int(x)

        if n == -1:
            if start is not None:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append(f"{start}-{end}")
            print(", ".join(ans))
            break

        if start is None:
            start = n
            end = n
        elif n == end + 1:
            end = n
        else:
            if start == end:
                ans.append(str(start))
            else:
                ans.append(f"{start}-{end}")
            start = n
            end = n

    if n == -1:
        break
