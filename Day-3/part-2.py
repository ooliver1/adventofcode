def rating(mode=None):
    values = open("input.txt").read().splitlines()
    z = 0
    o = 0
    for i in range(0, len(values[0])):
        for digits in values:
            if digits[i] == "0":
                z += 1
            elif digits[i] == "1":
                o += 1
        if mode == "o2":
            if z > o:
                values = [digits for digits in values if digits[i] == "0"]
            else:
                values = [digits for digits in values if digits[i] == "1"]
        elif mode == "co2":
            if z > o:
                values = [digits for digits in values if digits[i] == "1"]
            else:
                values = [digits for digits in values if digits[i] == "0"]
        z = 0
        o = 0
        if len(values) == 1:
            return values[0]
    return values[0]


print(int(rating("co2"), 2) * int(rating("o2"), 2))
