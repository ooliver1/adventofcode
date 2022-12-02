# fmt: off
print((lambda bits: int("".join(max(set(bit), key=bit.count) for bit in bits), base=2) * int("".join(min(set(bit), key=bit.count) for bit in bits), base=2))(tuple(zip(*open("input.txt").readlines())))) # fmt: off
