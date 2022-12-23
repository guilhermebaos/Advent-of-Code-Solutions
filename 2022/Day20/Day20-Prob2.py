# Solution for Problem 2 Day 20 of AoC 2022!

# Puzzle Input ----------
with open('Day20-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day20-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")


# Code ------------------
def solution_day20_prob2(puzzle_in: list):
    coords = list(map(int, puzzle_in))
    len_coords = len(coords)

    # Multiply by the decryption key
    decryption_key = 811589153
    coords = list(map(lambda x: x * decryption_key, coords))

    between = dict()
    for index, num in enumerate(coords):
        between[index] = [(index - 1) % len_coords, (index + 1) % len_coords]

    # Mix the message 10 times
    for _ in range(10):
        for index, num in enumerate(coords):
            if num == 0:
                continue

            # Moves to the right
            move = num % (len_coords - 1)

            # Do the moves
            old_left, old_right = between[index]
            new_right = old_right
            for _ in range(move):
                new_right = between[new_right][1]

            # Update to the new position
            new_left = between[new_right][0]
            between[index] = [new_left, new_right]

            # Update old position's neighboors
            between[old_left][1] = old_right
            between[old_right][0] = old_left

            # Update new position's neighboors
            between[new_left][1] = index
            between[new_right][0] = index

    # Find the sum of the groove coordinates
    marker = coords.index(0)
    total = 0
    for move in range(3000):
        marker = between[marker][1]
        if move % 1000 == 999:
            total += coords[marker]
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day20_prob2(test01))
print("\nSolution:")
print(solution_day20_prob2(puzzle))
