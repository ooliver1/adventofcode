with open("input.txt") as f: (ITEMS := {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}, print(sum(((3 if (ITEMS[me] == ITEMS[opponent]) else 6 if (ITEMS[me] == ITEMS[opponent] + 1 or ITEMS[me] == ITEMS[opponent] - 2) else 0) + ITEMS[me]) for opponent, me in map(lambda r: r.split(), f.read().splitlines()))))