with open("input.txt", "r") as f:
    data = [int(pos) for pos in f.read().split(",")]

diff = []

for i in range(2000):
    print(i)
    diff.append(0)
    for pos in data:
        diff[i] += (abs(i - pos) + 1) * abs(i - pos) // 2

print(min(diff))
