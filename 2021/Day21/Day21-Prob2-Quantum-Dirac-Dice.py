# Puzzle Input ----------
puzzle = [10, 6]
test01 = [4, 8]


# Main Code ----------

# Global variables
wins = [0, 0]
frequency = dict()


# See how many ways to have the three dice sum to the same total there are
def get_role_frequency():
    global frequency

    for x in range(1, 4):
        for y in range(1, 4):
            for z in range(1, 4):
                total = sum((x, y, z))
                frequency[total] = frequency.get(total, 0) + 1


def recursive_dice_rolls(players: list, scores: list, turn: int, dice_roll: int, roles: list, multiplier: int):
    global wins, frequency

    # See the results of this turn
    players[turn] = (players[turn] + dice_roll) % 10
    scores[turn] += players[turn] if players[turn] != 0 else 10

    # Stop the game, one player has won!
    if scores[turn] >= 21:
        wins[turn] += multiplier
    else:
        # Play again with every different total dice sum
        for next_roll in range(3, 10):
            recursive_dice_rolls(players[:], scores[:], (turn + 1) % 2, next_roll, roles[:] + [next_roll], multiplier * frequency[next_roll])


def dirac_dice(positions: list):

    # Reset globals
    global wins, frequency
    wins = [0, 0]
    frequency = dict()

    # Players' position and score
    players = positions[:]
    scores = [0, 0]

    # See how many ways to have the three dice sum to the same total there are
    get_role_frequency()

    # Start a game with each possible dice sum
    for next_roll in range(3, 10):
        recursive_dice_rolls(players[:], scores[:], 0, next_roll, [next_roll], frequency[next_roll])
    return max(wins)


# Tests and Solution ----------
print(dirac_dice(test01))
print(dirac_dice(puzzle))
