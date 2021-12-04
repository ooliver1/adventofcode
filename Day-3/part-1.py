with open("input.txt") as f:
    lines = f.readlines()
    gamma = int(
        "".join(max(set(bit), key=list(bit).count) for bit in zip(*lines)), base=2
    )
    epsilon = int(
        "".join(min(set(bit), key=list(bit).count) for bit in zip(*lines)), base=2
    )
    print(gamma * epsilon)
