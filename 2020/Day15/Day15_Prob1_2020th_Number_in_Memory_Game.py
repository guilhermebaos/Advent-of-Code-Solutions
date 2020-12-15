# Puzzle Input
with open('Day15_Input.txt') as puzzle_input:
    starting = puzzle_input.read().split('\n')

# Separate the integers (convert from CSV to python list)
for index, number_list in enumerate(starting):
    starting[index] = number_list.split(',')

# Parameters
starting = list(map(int, starting[0]))  # Allows for easy change between the test cases
len_starting = len(starting)            # Length of the starting list

# Calculate the first turns
memory = dict()                                     # Memory of the previous turns
for last_turn in range(1, len_starting):            # For every last turn:
    memory[starting[last_turn - 1]] = last_turn         # Add to the memory when each value was spoken last

# Calculate the other turns
last_number = starting[-1]                          # Select the last number spoken
for last_turn in range(len_starting, 2020):         # For every last turn:
    try:                                                # See if the number was spoken before
        age = last_turn - memory[last_number]               # If it was, register the age of the number
    except KeyError:                                    # If it wasn't:
        age = 0                                             # The age is 0
    memory[last_number] = last_turn                 # Save to memory the turn when the last number was spoken
    last_number = age                               # Update the last number

# Show the result
print(last_number)
