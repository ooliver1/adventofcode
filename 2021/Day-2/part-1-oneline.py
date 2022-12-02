# fmt: off
print((lambda ins: sum(int(a[1]) for a in ins if a[0] == "forward") * (sum(int(a[1]) for a in ins if a[0] == "up") + (-1 * sum(int(a[1]) for a in ins if a[0] == "down"))) * -1)([a.split(" ") for a in open("input.txt").readlines()]))
