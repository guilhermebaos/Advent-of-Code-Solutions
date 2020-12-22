# Puzzle Input
with open('Day22_Input.txt') as puzzle_input:
    decks = puzzle_input.read().split('\n\n')

# Separate the decks
deck_player1 = list(map(int, decks[0].split('\n')[1:]))
deck_player2 = list(map(int, decks[1].split('\n')[1:]))

# Get some parameters
number_of_cards = len(deck_player1 + deck_player2)


# Run a instance of combat, returning a list where [0] is the deck of the winner and [1] is the number of the winner
def combat(player1, player2):
    # Previous Configurations
    previous_configurations = []

    # Simulate the rounds
    while True:
        # One of the players has no cards
        len1, len2 = len(player1), len(player2)
        if len1 == 0:
            return [player2, 2]
        elif len2 == 0:
            return [player1, 1]

        # Has this configuration happened before
        if [player1, player2] in previous_configurations:
            return [player1, 1]
        else:
            previous_configurations += [[player1[:], player2[:]]]

        # Cards that are played
        card1 = player1.pop(0)
        card2 = player2.pop(0)

        # Result of the round

        # If they can go into recursive combat, they go into one
        if len1 > card1 and len2 > card2:
            copy_deck1 = player1[:card1]
            copy_deck2 = player2[:card2]

            # The result of this round is decided by the result of the recursive combat
            if combat(copy_deck1, copy_deck2)[1] == 1:
                player1 += [card1, card2]
            else:
                player2 += [card2, card1]

        # If they can't go into recursive combat, the game is decided normally
        else:
            if card1 > card2:
                player1 += [card1, card2]
            else:
                player2 += [card2, card1]


# Calculate the score
score = 0
for index, card_value in enumerate(combat(deck_player1, deck_player2)[0]):
    score += card_value * (number_of_cards - index)

# Show the result
print(score)
