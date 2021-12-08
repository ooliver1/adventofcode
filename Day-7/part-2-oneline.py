# fmt: off
print((lambda data: min([sum([(abs(i - pos) + 1) * abs(i - pos) // 2 for pos in data]) for i in range(2000)]))([int(pos) for pos in open("input.txt").read().split(",")]))
