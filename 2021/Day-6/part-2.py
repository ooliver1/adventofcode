with open("input.txt") as f:
    data = [int(a) for a in f.readlines()[0].split(",")]

times = [0 for _ in range(9)]
for t in data:
    times[t] += 1

for _ in range(256):
    before = times[0]
    times = times[1:] + [0]
    times[8] += before
    times[6] += before


print(sum(times))
