with open("input.txt") as f:
    pos = 0
    dep = 0
    aim = 0
    for i in f:
        a, b = i.split(" ")
        if a == "forward":
            pos += int(b)
            dep += aim * int(b)
        elif a == "up":
            aim -= int(b)
        elif a == "down":
            aim += int(b)
    print(pos * dep)
