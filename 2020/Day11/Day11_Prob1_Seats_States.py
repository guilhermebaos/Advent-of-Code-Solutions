# Puzzle Input
with open('Day11_Input.txt') as puzzle_input:
    seats_grid = puzzle_input.read().split('\n')

# Convert strings to lists
seats_grid = list(map(list, seats_grid))

# Apply the rules
change = True                   # Has there been changes in the grid
col_len = len(seats_grid)       # Number of rows
row_len = len(seats_grid[0])    # Number of items in a row
while change:
    change = False
    new_seats = []                          # New seat grid
    for y, row in enumerate(seats_grid):    # Go through every row
        new_seats += [[]]                   # Add a new row to the new grid
        for x, seat in enumerate(row):      # Go through every seat
            if seat != '.':                 # If seat is not floor:
                occupied = 0                                # Set occupied seats nearby to 0
                enough_occupied = False                     # If more than 4 seats are occupied, we don't need more info
                for delta_y in [-1, 0, 1]:                  # for every seat above and below
                    for delta_x in [-1, 0, 1]:              # For every seat to the left and to the right:
                        if delta_x != 0 or delta_y != 0:            # If the seat selected isn't itself:
                            test_y = y + delta_y                        # Coordinates of the seat
                            test_x = x + delta_x
                            if -1 < test_y < col_len and -1 < test_x < row_len:     # If the seat is valid
                                if seats_grid[test_y][test_x] == '#':               # If the seat is occupied
                                    occupied += 1                                       # Add 1 to occupied
                                    if occupied == 4:               # If more than 4 seats are occupied,
                                        enough_occupied = True      # it doesn't matter(See below)
                                        break
                    if enough_occupied:
                        break

                # Apply the rules, based on what the selected seat is and in the number of occupied seats nearby
                if seat == 'L' and occupied == 0:       # If the seat is empty and all it's neighbors are too:
                    new_seats[-1] += ['#']                  # Change it to occupied
                    if not change:
                        change = True                       # Flag that there has been a change
                elif seat == '#' and occupied > 3:      # If the seat is occupied and more 3 of it's neighbors are too:
                    new_seats[-1] += ['L']                  # Change it to empty
                    if not change:
                        change = True                       # Flag that there has been a change
                else:
                    new_seats[-1] += [seat]             # Otherwise, keep the seat the same
            else:                                       # If the 'seat' is floor, it doesn't change
                new_seats[-1] += ['.']
    seats_grid = new_seats[:]

# Count the total number of occupied seats
occupied = 0
for row in seats_grid:
    occupied += row.count('#')

print(occupied)
