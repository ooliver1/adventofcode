"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you notice
the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly
wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air
conditioning, leather seats, an extra cup holder, and the ability to pick
up and move multiple crates at once.

Again considering the example above, the crates begin in the same
configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3 means
that those three moved crates stay in the same order, resulting in this
new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain their
order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now
it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally
different order: MCD.

Before the rearrangement process finishes, update your simulation so that
the Elves know where they should stand to be ready to unload the final
supplies. After the rearrangement procedure completes, what crate ends up
on top of each stack?
"""

with open("input.txt") as f:
    data = f.read()


stack_data, moves = data.split("\n\n")
stack_letters = stack_data.splitlines()[:-1]
stacks = [
    [c for c in stack[::-1] if c != " "]
    for stack in zip(
        *[[line[i] for i in range(1, len(line), 4)] for line in stack_letters]
    )
]


for i, move in enumerate(moves.splitlines()):
    amount, direction = move.removeprefix("move ").split(" from ")
    from_, to = direction.split(" to ")

    amount = int(amount)
    from_ = int(from_)
    to = int(to)

    from_stack = stacks[from_ - 1]
    taken, new_stack = from_stack[-amount:], from_stack[:-amount]

    stacks[from_ - 1] = new_stack
    stacks[to - 1] = stacks[to - 1] + taken


print("".join(stack[-1] for stack in stacks))
