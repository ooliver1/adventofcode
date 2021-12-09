import itertools

with open("input.txt", "r") as f:
    lines = f.read().splitlines()

entries = [
    tuple(map(lambda s: tuple(map(frozenset, s.split(" "))), l.split(" | ")))
    for l in lines
]

res = 0
defs = dict(
    zip(
        map(
            frozenset,
            (
                "abcefg",
                "cf",
                "acdeg",
                "acdfg",
                "bcdf",
                "abdfg",
                "abdefg",
                "acf",
                "abcdefg",
                "acbdfg",
            ),
        ),
        range(10),
    )
)

for inps, outs in entries:
    for comb in itertools.permutations("abcdefg"):
        wmap = dict(zip("abcdefg", comb))
        digits = {}
        for inp in inps:
            tr = frozenset(wmap[i] for i in inp)
            if tr not in defs:
                break
            digits[inp] = defs[tr]
        if len(digits) == 10:
            res += int("".join(str(digits[o]) for o in outs))
            break

print(res)
