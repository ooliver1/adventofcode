with open("input.txt") as f:
    grt = 0
    array = [int(x) for x in f.read().splitlines()]
    sliding = []
    for i, n in enumerate(array):
        if i + 2 >= len(array):
            break
        window = n + array[i + 1] + array[i + 2]
        sliding.append(window)
        if i == 0:
            continue
        if window > sliding[-2]:
            grt += 1
    print(grt)
