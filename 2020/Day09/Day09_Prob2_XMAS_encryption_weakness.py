# Puzzle Input
with open('Day09_Input.txt') as puzzle_input:
    number_sequence = puzzle_input.read().split('\n')

# Convert to int
number_sequence = list(map(int, number_sequence))

# Test the numbers to see if they match the criteria
preamble = 25
exception_rule = None
for current_pos, number in enumerate(number_sequence[preamble:]):           # Number to analise
    lastX = number_sequence[current_pos:current_pos + preamble]             # Last X numbers that can be part of the sum
    valid_num = False
    for first_pos, first_num in enumerate(lastX):                           # First number to be part of the sum
        second_num = number - first_num                                     # Second number to be part of the sum
        if second_num in lastX[first_pos + 1:]:         # The second num must be in the rest of the last 25 numbers
            valid_num = True                            # IF one sum is found, the number is valid
            break
    if not valid_num:                                   # If a number was found to not be valid, it is the exception
        exception_rule = number
        break

# Allows for substitution in case the above code is to slow
objective = exception_rule

# Use a 'worm' of numbers to find the contiguous sequence that adds to the objective
start = 0
stop = 1
while True:
    numbers_sum = sum(number_sequence[start:stop])      # Sum of the sequence we are trying
    if numbers_sum < objective:                         # If the sum is to small, extend it by 1
        stop += 1
    elif numbers_sum > objective:                       # If the sum is to large, cut of the first number
        start += 1
    elif numbers_sum == objective:                      # If the sum is just right, we got our answer!
        break

encryption_weakness = min(number_sequence[start:stop]) + max(number_sequence[start:stop])
print(encryption_weakness)
