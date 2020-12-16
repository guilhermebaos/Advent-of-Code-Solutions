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
    for index, range_limit in enumerate(field):         # Add the minimums and maximums to their respective list
        if index % 2 == 0:
            minimums += [range_limit]
        else:
            maximums += [range_limit]

# See the values out of the ranges
error_rate = 0
for ticket in nearby_tickets:                       # For every ticket
    for value in ticket:                                # For every value in every ticket:
        in_range = False                                    # Assume it's not in a range
        for mini, maxi in zip(minimums, maximums):          # For every range:
            if mini <= value <= maxi:                           # If it's inside the range:
                in_range = True                                     # Set in_range to True
                break                                               # We don't need to test any more cases
        if not in_range:                                    # If it's not in any range, add to the error rate
            error_rate += value

# Show the result
print(error_rate)
