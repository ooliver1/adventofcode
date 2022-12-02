with open("input.txt") as f:
    grt = 0
    array = [int(x) for x in f.read().splitlines()]
    for i, n in enumerate(array):
        if i == 0:
            continue
        if n > array[i - 1]:
            grt += 1
    print(grt)
