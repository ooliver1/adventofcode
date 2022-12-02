with open("input.txt") as f: print(max(sum(map(int, elf.split("\n"))) for elf in f.read().split("\n\n")))
