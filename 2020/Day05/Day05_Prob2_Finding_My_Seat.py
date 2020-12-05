# Puzzle Input
with open('Day05_Input.txt') as puzzle_input:
    seats = puzzle_input.read().split('\n')


# Converts a list containing a binary number to a decimal number
def bin_to_decimal(bin_num):
    dec_num = 0
    bin_len = len(bin_num)
    for pos, bit in enumerate(bin_num):
        if bit == 1:
            dec_num += 2 ** (bin_len - pos - 1)
    return dec_num


# Calculates all the seats IDs
seat_id = []
for s in seats:
    seat_position = [[], []]
    # Convert from letters to binary
    for letter in s[:-3]:
        seat_position[0] += [0] if letter == 'F' else [1]
    for letter in s[-3:]:
        seat_position[1] += [0] if letter == 'L' else [1]

    # Convert from binary to seat ID
    seat_id += [bin_to_decimal(seat_position[0]) * 8 + bin_to_decimal(seat_position[1])]

# Loop through the seats to find one that is empty but has the ones next to him filled
for s_id in range(1, max(seat_id)):
    if not seat_id.__contains__(s_id):
        if seat_id.__contains__(s_id - 1) and seat_id.__contains__(s_id + 1):
            print(s_id)
