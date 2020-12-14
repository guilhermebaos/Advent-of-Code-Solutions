# Puzzle Input
with open('Day14_Test_Prob1.txt') as puzzle_input:
    operations = puzzle_input.read().split('\n')


# Converts string-represented binary number to decimal
def bin_to_decimal(bin_num):
    dec_num = 0
    bin_len = len(bin_num)
    for pos, bit in enumerate(bin_num):         # Goes through the bits, from most to least important (left to right):
        if bit == '1':                              # If the bit is on:
            dec_num += 2 ** (bin_len - pos - 1)         # It adds the corresponding value to the total
    return dec_num


def bitwise_masking(num, bitmask):
    num = list(str(bin(num))[2:].rjust(36, '0'))
    bitmask = list(bitmask)
    index = 0
    for bit_num, bit_mask in zip(num, bitmask):
        if bit_mask != 'X':
            num[index] = bit_mask
        index += 1
    return bin_to_decimal(list(map(int, num)))


# Execute operations
memory = dict()                 # Create the memory, stored in a dictionary because we can overwrite addresses without
for op in operations:           # having to keep 2^36 addresses with a 0
    op = op.split(' = ')        # Separate the operation keywords
    command = op[0]             # Select the command keyword
    value = op[1]               # Select the value to be used
    if command == 'mask':       # Change the mask
        mask = value
    else:                                                           # Assign numbers to memory
        location = command[4:-1]                                    # Memory Address
        memory[location] = bitwise_masking(int(value), mask)        # Store the masked value


# Calculate the sum of all value in memory
total = 0
for key in memory:
    total += memory[key]

print(total)
