# Puzzle Input
with open('Day22_Input.txt') as puzzle_input:
    decks = puzzle_input.read().split('\n\n')

# Separate the decks
player1 = list(map(int, decks[0].split('\n')[1:]))
player2 = list(map(int, decks[1].split('\n')[1:]))

# Get some parameters
number_of_cards = len(player1 + player2)
winner_card = max(player1 + player2)

# See who's going to win
if winner_card in player1:
    winner_deck = player1
else:
    winner_deck = player2

# Simulate the rounds
while len(winner_deck) != number_of_cards:
    # Cards that are played
    card1 = player1.pop(0)
    card2 = player2.pop(0)

    # Result of the round
    if card1 > card2:
        player1 += [card1, card2]
    else:
        player2 += [card2, card1]


# Calculate the score
score = 0
for index, card_value in enumerate(winner_deck):
    score += card_value * (number_of_cards - index)

# Show the result
print(score)
