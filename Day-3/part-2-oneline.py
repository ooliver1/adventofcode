# fmt: off
print(int(((lambda a: lambda v: a(a, v))(lambda f, stuff: f(f, [[digits for digits in stuff[0] if digits[stuff[1]] == (max({v[stuff[1]] for v in stuff[0]}, key=[v[stuff[1]] for v in stuff[0]].count) if [v[stuff[1]] for v in stuff[0]].count("0") != [v[stuff[1]] for v in stuff[0]].count("1") else "1")], stuff[1] + 1]) if len([digits for digits in stuff[0]if digits[stuff[1]] == (max({v[stuff[1]] for v in stuff[0]}, key=[v[stuff[1]] for v in stuff[0]].count) if [v[stuff[1]] for v in stuff[0]].count("0") != [v[stuff[1]] for v in stuff[0]].count("1") else "1")]) != 0 and stuff[1] < 12 else stuff[0]))([list(open("input.txt").readlines()), 0])[0], base=2) * int(((lambda a: lambda v: a(a, v))(lambda f, stuff: f(f, [[digits for digits in stuff[0] if digits[stuff[1]] == (min({v[stuff[1]] for v in stuff[0]}, key=[v[stuff[1]] for v in stuff[0]].count) if [v[stuff[1]] for v in stuff[0]].count("0") != [v[stuff[1]] for v in stuff[0]].count("1") else "0")], stuff[1] + 1]) if len([digits for digits in stuff[0] if digits[stuff[1]] == (min({v[stuff[1]] for v in stuff[0]}, key=[v[stuff[1]] for v in stuff[0]].count) if [v[stuff[1]] for v in stuff[0]].count("0") != [v[stuff[1]] for v in stuff[0]].count("1") else "0")]) != 0 and stuff[1] < 12 else stuff[0]))([list(open("input.txt").readlines()), 0])[0], base=2))
