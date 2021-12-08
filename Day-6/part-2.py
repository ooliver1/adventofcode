with open("input.txt") as f:
    data = [int(a) for a in f.readlines()[0].split(",")]

# times = [0 for _ in range(9)]
# for t in data:
# times[t] += 1
# print(times)

# currentday = 0

for _ in range(256):
    # times.append(times[currentday])
    # times[currentday + 6] += times[currentday]
    # currentday += 1
    toadd = 0
    for i, t in enumerate(data):
        if t == 0:
            toadd += 1
            data[i] = 6
        else:
            data[i] = t - 1
    for _ in range(toadd):
        data.append(8)


# print(sum(times[-(i + 1)] for i in range(9)))
print(len(data))
