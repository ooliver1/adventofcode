# fmt: off
print((lambda ins: (sum(int(a[1]) * ((-1 * sum(int(c[1]) for c in ins[:i] if c[0] == "up")) + sum(int(d[1]) for d in ins[:i] if d[0] == "down")) for i, a in enumerate(ins) if a[0] == "forward") * sum(int(b[1]) for b in ins if b[0] == "forward")))([a.split() for a in open("input.txt").readlines()]))
