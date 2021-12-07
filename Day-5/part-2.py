with open("input.txt") as f:
    data = f.readlines()

counted = [[0 for _ in range(1000)] for _ in range(1000)]

for line in data:
    one, two = line.split(" -> ")
    x1, y1 = one.split(",")
    x2, y2 = two.split(",")
    if int(x1) == int(x2):
        top, bottom = min(int(y1), int(y2)), max(int(y1), int(y2))
        for y in range(top, bottom + 1):
            counted[int(y)][int(x1)] += 1
    elif int(y1) == int(y2):
        left, right = min(int(x1), int(x2)), max(int(x1), int(x2))
        for x in range(left, right + 1):
            counted[int(y1)][int(x)] += 1
    else:
        xdir = 1 if int(x1) < int(x2) else -1
        ydir = 1 if int(y1) < int(y2) else -1
        x = int(x1)
        y = int(y1)
        while (x != int(x2)) and (y != int(y2)):
            counted[int(y)][int(x)] += 1
            x += xdir
            y += ydir
        counted[int(y)][int(x)] += 1

print(sum(point >= 2 for row in counted for point in row))
