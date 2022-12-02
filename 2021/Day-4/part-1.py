with open("input.txt") as f:
    data = f.readlines()

drawn_numbers = data[0].split(",")
boards = [
    [[int(x) for x in line.split()] for line in data[i + 1 : i + 6]]
    for i in range(1, len(data), 6)
]

marked = [[[False for _ in range(5)] for _ in range(5)] for _ in range(len(boards))]
for number in drawn_numbers:
    for i, board in enumerate(boards):
        for row in range(5):
            for col in range(5):
                if boards[i][row][col] == int(number):
                    marked[i][row][col] = True
        if any(all(marked[i][row][col] for col in range(5)) for row in range(5)) or any(
            all(marked[i][col][row] for col in range(5)) for row in range(5)
        ):
            print(f"{number} wins")
            print(board)
            total = sum(
                sum(boards[i][row][col] for col in range(5) if not marked[i][row][col])
                for row in range(5)
            )
            print(f"score: {total * int(number)}")
            exit()
