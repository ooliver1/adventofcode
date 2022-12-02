with open("input.txt") as f: print(sum(sorted(sum(map(int, elf.split("\n"))) for elf in f.read().split("\n\n"))[-3:]))
