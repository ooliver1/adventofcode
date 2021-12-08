# fmt: off
print((lambda data: sum(1 for p in [a for _, b in data for a in b] if len(p) in (2, 3, 4, 7)))([(a.split(), b.split()) for a, b in [line.strip().split(" | ") for line in open("input.txt").readlines()]]))
