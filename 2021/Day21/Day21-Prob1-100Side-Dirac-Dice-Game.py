# Puzzle Input ----------
puzzle = [10, 6]

test01 = [4, 8]


# Main Code ----------

# Compute the sum of the next three rolls
def next_three_rolls(n: int):
    n -= 1
    return n % 100 + (n + 1) % 100 + (n + 2) % 100 + 3


# Play Dirac Dice
def dirac_dice(positions: list):
    # Players' position and score
    players = positions[:]
    scores = [0, 0]

    # Save the number of rolls
    num_rolls = 1
    while True:
        for index in range(2):
            # Roll the dice for each player
            players[index] = (players[index] + next_three_rolls(num_rolls)) % 10
            scores[index] += players[index] if players[index] != 0 else 10
            num_rolls += 3

            # Stop the game, one player has won!
            if scores[index] >= 1000:
                return scores[(index + 1) % 2] * (num_rolls - 1)


# Tests and Solution ----------
print(dirac_dice(test01))
print(dirac_dice(puzzle))
