# Puzzle Input ----------
with open('Day08-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day08-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Each number that has a non-unique length has a certain signature
# Where the signature is the number of connections it shares with 1, 4, 7 or 8
# So in the order 1, 4, 7, 8:
signature = {
    0: [2, 3, 3, 6],
    2: [1, 2, 2, 5],
    3: [2, 3, 3, 5],
    5: [1, 3, 2, 5],
    6: [1, 3, 2, 6],
    9: [2, 4, 3, 6]
}


# Parse each display info
def parse_display(display: str):
    info, readout = display.split(' | ')
    return [info.split(), readout.split()]


# Number of characters of a which are in b -> Shared connections
def chars_of_a_in_b(a: str, b: str):
    return len([x for x in a if x in b])


# Decode a single display
def decode_display(display: list):
    global signature

    info, readout = display

    # Save the connections for 1, 4, 7, 8 (unique length)
    decoded = {x: '' for x in range(10)}
    for item in info:
        if len(item) == 2:
            decoded[1] = item
        elif len(item) == 3:
            decoded[7] = item
        elif len(item) == 4:
            decoded[4] = item
        elif len(item) == 7:
            decoded[8] = item

    # Find the signature of non-unique length patterns and compare them with the signatures we know
    for item in info:
        if len(item) not in [5, 6]:
            continue
        this_signature = [
            chars_of_a_in_b(item, decoded[1]),
            chars_of_a_in_b(item, decoded[4]),
            chars_of_a_in_b(item, decoded[7]),
            chars_of_a_in_b(item, decoded[8])
        ]

        # If the signature is the same as a number, this string is meant to be that number!
        for num in signature:
            if signature[num] == this_signature:
                decoded[num] = item

    # Invert the decoded dictionary
    decoded = {string: num for num, string in decoded.items()}
    return decoded


# Get the output of a display given it's decoded dictionary
def output_display(display: list, decoded: dict):
    info, readout = display

    # Get the 4 digit output of each display
    output = ''
    for string in readout:
        for key in decoded:
            if set(string) == set(key):
                output += str(decoded[key])
    return int(output)


# Decode the entire wire pattern for all displays
def decode_all(displays):
    # Parse the displays
    displays = list(map(parse_display, displays))

    # Decode the displays
    decoded = list(map(decode_display, displays))

    # Output of each display
    outputs = list(map(output_display, displays, decoded))

    # Return the sum off all outputs
    return sum(outputs)


# Tests and Solution ----------
print(decode_all(test01))
print(decode_all(puzzle))
