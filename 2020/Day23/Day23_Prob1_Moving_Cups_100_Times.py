# Puzzle Input
with open('Day23_Input.txt') as puzzle_input:
    starting_cups = list(map(int, list(puzzle_input.read())))

# The number of cups
number_of_cups = len(starting_cups)


# Execute a single move
def move(cups, current_cup):
    # Get the current cup's index and reorganize the cups list
    current_index = cups.index(current_cup)
    cups = cups[current_index:] + cups[:current_index]

    # Get the cups which are picked up
    print(cups)
    picks_up = []
    for delta_index in range(3):
        picks_up += [cups.pop(1)]
    print(picks_up, cups)

    # Get the destination cup's label and index
    destination_cup = current_cup - 1
    while True:
        if destination_cup < 1:
            destination_cup += number_of_cups
        if destination_cup not in picks_up:
            break
        destination_cup -= 1
    destination_index = cups.index(destination_cup)
    print(destination_cup)

    # Put the picked up cups next to the destination cup
    for delta_index, cup in zip(range(3), picks_up):
        cups.insert(destination_index + delta_index + 1, cup)

    # Return the new order for the cups and the next current cup
    next_current_cup = cups[1]
    return cups, next_current_cup


# Execute 100 moves
new_cups = starting_cups[:]
new_current_cup = starting_cups[0]
for move_number in range(100):
    print(f'\n-=- Move {move_number + 1} -=-')
    new_cups, new_current_cup = move(new_cups, new_current_cup)     # Update the lists and do another move


# Get the order, starting at the cup with the label 1 and excluding it
start = new_cups.index(1)
order = new_cups[start + 1:] + new_cups[:start]
order = ''.join(list(map(str, order)))

# Show the result
print(order)
