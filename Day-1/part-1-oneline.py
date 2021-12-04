# fmt: off
(lambda numbers: print(len([i for i, num in enumerate(numbers) if i != 0 and num > numbers[i-1]])))([int(i) for i in open("input1.txt").readlines()])
