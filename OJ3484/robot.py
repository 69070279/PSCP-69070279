"""Sound Checker"""

n, p = input().split()
n = int(n)
p = float(p)

if n < 1 or n > 50 or p < 1 or p > 500:
    print("Data Incorrect")
else:
    tiles = []
    for _ in range(n):
        row = list(map(int, input().split()))
        tiles.append(row)

    row_tiles = []
    row_points = []
    col_tiles = [0] * n
    col_points = [0] * n
    bad_tiles = 0
    bad_points = 0

    for i in range(n):
        count_tiles = 0
        count_points = 0

        for j in range(n):
            value = tiles[i][j]

            if value > 0:
                count_tiles += 1
                bad_tiles += 1

            count_points += value
            bad_points += value

            if value > 0:
                col_tiles[j] += 1
            col_points[j] += value

        row_tiles.append(count_tiles)
        row_points.append(count_points)

    for i in range(n):
        print(*tiles[i], row_tiles[i], row_points[i])

    print(*col_tiles)
    print(*col_points)
    print(bad_tiles, bad_points, f"{bad_points * p:.2f}")
