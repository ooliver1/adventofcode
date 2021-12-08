with open("input.txt") as f:
    data = [line.strip().split(" | ") for line in f.readlines()]

data = [(a.split(), b.split()) for a, b in data]
print(sum(1 for p in [a for _, b in data for a in b] if len(p) in (2, 3, 4, 7)))
