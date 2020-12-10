# Puzzle Input
with open('Day10_Input.txt') as puzzle_input:
    joltage_adaptors = puzzle_input.read().split('\n')

# Convert to int
joltage_adaptors = list(map(int, joltage_adaptors))

# The the power outlet (0 Jolts) and device adaptor (max + 3 Jolts)
joltage_adaptors += [0, max(joltage_adaptors) + 3]

# Sort the list
joltage_adaptors.sort()

# List number of adapters that can connect to another adapter
connections = []
for index, adapter in enumerate(joltage_adaptors):              # Go through every adapter
    can_connect = []
    for connect_adapter in joltage_adaptors[index + 1:]:        # Go through every other adapter with a larger value
        if connect_adapter > 3 + adapter:                       # If it can connect, then break
            break
        can_connect += [connect_adapter]                        # If it connects, add it to a temporary list
    connections += [can_connect]                                # Add the temp list to the main list of connections

# Calculate the number of arrangements

# We know the second to last element of our list, the last adapter, only has one connection, our device, therefore, we
    # can assign it the value 1 and go through the list in reverse, calculating the number of possible connections of an
    # adapter by adding the number of connections that the adapters that can connect to it make
arrangements = {str(joltage_adaptors[-2]): 1}               # Dictionary for the number of arrangements for each adaptor
for index in range(len(joltage_adaptors) - 3, -1, -1):      # Go through the numbers in reverse order
    total = None                                            # Total number of connections for this adapter
    for adapter in connections[index]:                      # For every adapter that can connect to this one,
        number_of_connections = arrangements[str(adapter)]      # add the number of connections they can make.
        if total is None:                                       # That's the number of connections this adapter can make
            total = number_of_connections
        else:
            total += number_of_connections
    arrangements[str(joltage_adaptors[index])] = total      # Add the number os connections to the total

# The result is the number os connections the power outlet, the '0' on our list, can make
print(arrangements['0'])
