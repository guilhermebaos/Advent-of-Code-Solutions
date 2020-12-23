# Puzzle Input
with open('Day23_Input.txt') as puzzle_input:
    starting_cups = list(map(int, list(puzzle_input.read())))

# Add cups up to 1_000_000
for extra_cup in range(max(starting_cups) + 1, 1_000_001):
    starting_cups += [extra_cup]

# The number of cups
number_of_cups = len(starting_cups)

# List where the index is the cup label and the value is the number of the cup next to that one
starting_next_cups = [0 for _ in range(number_of_cups + 1)]
for cup_index, cup_label in enumerate(starting_cups):
    if cup_index == number_of_cups - 1:                                 # Loop around to prevent IndexError
        cup_index = -1
    starting_next_cups[cup_label] = starting_cups[cup_index + 1]        # The cup next to cup_label is at cup_index + 1


# Execute a single move
def move(next_cups, current_cup):
    # Get the numbers of the cups that are picked up
    picks_up = []
    next_to = current_cup                   # Start by picking up the cup next to the current cup
    for _ in range(3):
        next_to = next_cups[next_to]        # This is one of the cups to be picked up, and we also have to pick up
        picks_up += [next_to]               # the cup next to it

    # Get the destination cup
    destination_cup = current_cup - 1       # The destination cup is the current cup minus 1, unless that number is one
    while True:                             # of those that we picked up
        if destination_cup < 1:
            destination_cup += number_of_cups
        if destination_cup not in picks_up:
            break
        destination_cup -= 1

    # Update which cups are next to which
    next_cups[current_cup] = next_cups[picks_up[2]]     # The cup after the ones we picked up is next to the current cup
    next_cups[picks_up[2]] = next_cups[destination_cup] # The cup after the destination cup is now after the last we picked up
    next_cups[destination_cup] = picks_up[0]            # The last cup we picked up is now after the destination cup

    return next_cups, next_cups[current_cup]            # Return the updated next_to list and the next current cup


# Execute 10 Million moves
new_next_cups = starting_next_cups[:]
new_current_cup = starting_cups[0]
for move_number in range(10_000_000):
    new_next_cups, new_current_cup = move(new_next_cups, new_current_cup)

# Get the product
product = new_next_cups[1] * new_next_cups[new_next_cups[1]]

# Show the result
print(product)
