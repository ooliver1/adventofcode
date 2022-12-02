with open("input.txt", "r") as f:
    data = [int(pos) for pos in f.read().split(",")]

diff = []

for i in range(2000):
    diff.append(0)
    for pos in data:
        diff[i] += abs(pos - i)

print(min(diff))
