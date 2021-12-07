with open("input.txt") as f:
    data = [int(a) for a in f.readlines()[0].split(",")]

for _ in range(80):
    toadd = 0
    for i, t in enumerate(data):
        if t == 0:
            toadd += 1
            data[i] = 6
        else:
            data[i] = t - 1
    for _ in range(toadd):
        data.append(8)

print(len(data))
