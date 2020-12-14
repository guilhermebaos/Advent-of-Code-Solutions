# Puzzle Input
with open('Day14_Input.txt') as puzzle_input:
    operations = puzzle_input.read().split('\n')


# Converts list-represented binary number to decimal
def bin_to_decimal(bin_num):
    bin_num = ''.join(bin_num)
    dec_num = 0
    bin_len = len(bin_num)
    for pos, bit in enumerate(bin_num):         # Goes through the bits, from most to least important (left to right):
        if bit == '1':                              # If the bit is on:
            dec_num += 2 ** (bin_len - pos - 1)         # It adds the corresponding value to the total
    return dec_num


# Applies the masking to the memory addresses
def bitwise_masking(num, bitmask):
    num = list(str(bin(num))[2:].rjust(36, '0'))    # Creates a 36-bit number from an integer
    bitmask = list(bitmask)                         # Makes it so the bitmask is a list
    index = 0
    for bit_num, bit_mask in zip(num, bitmask):     # If a bit in the mask is non-0, it overwrites the memory address
        if bit_mask != '0':
            num[index] = bit_mask
        index += 1

    floating_bits = num.count('X')                                              # Number of floating bits
    floating_position = [index for index, bit in enumerate(num) if bit == 'X']  # Position of the floating bits
    memory_list = []                                                            # Possible memories
    for bit_possible in range(2**floating_bits):                                # Possible values for all the Xs
        bit_possible = list(str(bin(bit_possible))[2:].rjust(floating_bits, '0'))   # Pads the possible values
        for index, bit_value in zip(floating_position, bit_possible):   # Applies possibles value to the memory binary
            num[index] = bit_value
        memory_list += [bin_to_decimal(num)]                            # Stores all the memories
    return memory_list


# Execute operations
memory = dict()                 # Create the memory, stored in a dictionary because we can overwrite addresses without
for op in operations:           # having to keep 2^36 addresses with a 0
    op = op.split(' = ')        # Separate the operation keywords
    command = op[0]             # Select the command keyword
    value = op[1]               # Select the value to be used
    if command == 'mask':       # Change the mask
        mask = value
    else:                                                           # Assign numbers to memory
        location = int(command[4:-1])                               # Base address
        for memory_location in bitwise_masking(location, mask):     # List of all addresses
            memory[memory_location] = int(value)                    # Store the number

# Calculate the sum of all value in memory
total = 0
for key in memory:
    total += memory[key]

print(total)
