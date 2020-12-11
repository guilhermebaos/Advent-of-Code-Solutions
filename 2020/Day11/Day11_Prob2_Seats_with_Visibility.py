# Puzzle Input
with open('Day11_Input.txt') as puzzle_input:
    seats_grid = puzzle_input.read().split('\n')

# Convert strings to lists
seats_grid = list(map(list, seats_grid))

# Grid constants
col_len = len(seats_grid[0])            # Number of columns
row_len = len(seats_grid)               # Number of rows
dia_len = col_len + row_len - 1         # Number os diagonals

# Organize seats by direction and index them, also convert 'L' to 0 and '#' to 1
seats_binary = []                                   # List of seats in 0s and 1s

vertical = [[] for _ in range(col_len)]             # Lists of seats by orientation
horizontal = [[] for _ in range(row_len)]
diagonal_lt_rb = [[] for _ in range(dia_len)]           # Note: lt_rb is left-top to right-bottom
diagonal_lb_rt = [[] for _ in range(dia_len)]           # Note: lb_rt is left-bottom to right-top

index = 0                                           # Index of current seat
for y, row in enumerate(seats_grid):
    for x, seat in enumerate(row):                  # Go through every grid position
        if seat == 'L':                             # If it is a seat:
            seats_binary += [0]                         # Add it to the binary list
            vertical[x] += [index]                      # Add to it's correspondent list in every direction, the index
            horizontal[y] += [index]                    # can be deduced by plotting the coordinates on a plane,
            diagonal_lt_rb[y - x] += [index]            # each direction has a unique definition based on x and y and
            diagonal_lb_rt[y + x] += [index]            # if to seats are next to each other in a certain direction,
            index += 1                                  # there is visibility
seats_len = index                                   # Number of seats

# See the connections
connections = [[] for _ in range(seats_len)]        # Create the connections list
for line_collection in [vertical] + [horizontal] + [diagonal_lt_rb] + [diagonal_lb_rt]:     # For ALL directions:
    for line in line_collection:                                    # For every line:
        for position, seat_index in enumerate(line):                    # For every seat:
            if position > 0:                                                # If possible:
                connections[seat_index] += [line[position - 1]]                 # Add the previous seat to it's connect
            if position < len(line) - 1:                                    # If possible:
                connections[seat_index] += [line[position + 1]]                 # Add the next seat to it's connections

# Apply the rules
change = True                   # Has there been changes in the grid
while change:
    change = False
    new_seats = []                                          # New seat grid
    for current_seat, receive in enumerate(connections):    # Go through the seat's connections
        occupied = 0
        for seat_index in receive:                          # See the number of occupied seats it can see
            occupied += seats_binary[seat_index]

        # Apply the rules, based on what the selected seat is and in the number of occupied seats nearby
        seat_value = seats_binary[current_seat]
        if seat_value == 0 and occupied == 0:       # If the seat is empty and all it's neighbors are too:
            new_seats += [1]                            # Change it to occupied
            if not change:
                change = True                       # Flag that there has been a change
        elif seat_value == 1 and occupied > 4:      # If the seat is occupied and more 3 of it's neighbors are too:
            new_seats += [0]                            # Change it to empty
            if not change:
                change = True                           # Flag that there has been a change
        else:
            new_seats += [seat_value]                   # Otherwise, keep the seat the same
    seats_binary = new_seats[:]

# Count the total number of occupied seats
occupied = seats_binary.count(1)

print(occupied)
