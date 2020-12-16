import re

# Puzzle Input
with open('Day16_Input.txt') as puzzle_input:
    areas = puzzle_input.read().split('\n\n')


# Function to fields into usable integer ranges
def map_fields(el):
    matches = re.findall('\d*-\d*', el)                     # Use RegEx to find all ranges
    parsed_matches = []
    for value_range in matches:                             # Parse the matches so they're a list of integers
        parsed_matches += list(map(int, value_range.split('-')))
    return parsed_matches                                   # Return the parsed matches


# Function to separate nearby tickets into integers list
def map_nearby_tickets(el):
    return list(map(int, el.split(',')))


# Select, split and convert into lists of integers each part of the input
fields_range = list(map(map_fields, areas[0].split('\n')))                        # Part 0: The fields
my_ticket = list(map(int, areas[1].split('\n')[1].split(',')))              # Part 1: My ticket
nearby_tickets = list(map(map_nearby_tickets, areas[2].split('\n')[1:]))    # Part 2: Nearby tickets

# Ranges for the values
minimums = []
maximums = []
for field in fields_range:                                # For every range in the fields:
    for index, range_limit in enumerate(field):           # Add the minimums and maximums to their respective list
        if index % 2 == 0:
            minimums += [range_limit]
        else:
            maximums += [range_limit]

# See the values out of the ranges
valid_tickets = []
for ticket in nearby_tickets:                       # For every ticket
    is_valid = True
    for value in ticket:                                # For every value in every ticket:
        in_range = False                                    # Assume it's not in a range
        for mini, maxi in zip(minimums, maximums):          # For every range:
            if mini <= value <= maxi:                           # If it's inside the range:
                in_range = True                                     # Set in_range to True
                break                                               # We don't need to test any more cases
        if not in_range:                                    # If the value is not in any range, the ticket is not valid
            is_valid = False
            break
    if is_valid:
        valid_tickets += [ticket]

# Assign each field to a position on the tickets
fields_to_pos = []                              # Assign each field, based on its index, to a position on a ticket
positions = len(my_ticket)                      # Positions per ticket
for field in fields_range:                      # Recalculate the maximums and minimums
    fields_to_pos += [[]]                       # Each field can correspond to many positions

    # Reset minimums and maximums to limit them to this field
    minimums = []
    maximums = []
    for index, range_limit in enumerate(field):         # Add the minimums and maximums to their respective list
        if index % 2 == 0:
            minimums += [range_limit]
        else:
            maximums += [range_limit]

    # Test if each position can fit in a certain field
    for pos in range(positions):
        right_pos = True                        # Assume it fits
        for ticket in valid_tickets:            # Test every ticket
            value = ticket[pos]                 # The value we want is in that position
            if not ((minimums[0] <= value <= maximums[0]) or (minimums[1] <= value <= maximums[1])):
                right_pos = False               # If it doesn't fit, we stop testing for this field-position pair
                break
        if right_pos:
            fields_to_pos[-1] += [pos]          # If it fits, we add to its list-in-a-list

# Make sure all fields correspond to one and only one position on the ticket
while True:
    # Select the value that has to be remove from all other fields, because there is one field that can only correspond
    # to that position
    for field in fields_to_pos:
        if len(field) == 1:
            to_remove = field[0]
            break

    # Remove that position from the other fields
    for index, field in enumerate(fields_to_pos):
        if len(field) != 1:
            try:                                        # If a field doesn't have that position as a possibility,
                fields_to_pos[index].remove(to_remove)  # an exception is raised, which is handled
            except ValueError:
                pass
        else:                                           # To declare we already removed a position, add a -1 that
            fields_to_pos[index] += [-1]                # field's list
    if max(list(map(len, fields_to_pos))) == 2:         # If all fields have only to positions, their real position
        break                                           # on the ticket and a -1, break

# Calculate the product
total = 1
for index in range(6):                                  # The first 6 parameters have departure in their name
    total *= my_ticket[fields_to_pos[index][0]]

# Show the result
print(total)
