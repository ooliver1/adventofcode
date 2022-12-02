with open("input.txt") as f:
    pos = 0
    dep = 0
    for i in f:
        a, b = i.split(" ")
        if a == "forward":
            pos += int(b)
        elif a == "up":
            dep -= int(b)
        elif a == "down":
            dep += int(b)
    print(pos * dep)
