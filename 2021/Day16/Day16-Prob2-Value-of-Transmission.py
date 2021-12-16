# Puzzle Input ----------
with open('Day16-Input.txt', 'r') as file:
    puzzle = file.read()

# Main Code ----------

# Store the bits left to examine
bits = ''


# Create the hex_to_bin dictionary
def create_hex_to_bin(max_num=15):
    local_hex_to_bin = dict()
    for i in range(max_num + 1):
        # The keys are hex values of integers
        hexi = hex(i)[2:].upper()

        # The values are the corresponding binary padded to length 4
        bini = bin(i)[2:].rjust(4, '0')
        local_hex_to_bin[hexi] = bini
    return local_hex_to_bin


hex_to_bin = create_hex_to_bin()


# Access the next n bits
def next_bits(n):
    global bits

    # Return the bits and delete them from the string
    next_up = bits[:n]
    bits = bits[n:]
    return next_up


# Get the literal value in a packet
def get_literal_value():
    global bits

    # While there is a new packet, keep reading
    prefix = '1'
    literal_value = list()
    while prefix == '1':
        # Binary number without the prefix
        binary_number = next_bits(5)
        prefix = binary_number[0]

        # The literal value is the concatenation of the strings, converted to decimal
        literal_value += list(binary_number[1:])
    return int(''.join(literal_value), 2)


# Packet with typeID = 4
def literal_value_packet(version, type_id):
    global bits

    # Return the packet
    literal_value = get_literal_value()
    p = {
        'version': version,
        'type_id': type_id,
        'literal_value': literal_value
    }
    return p


# Create a operator packet
def operator_packet(version, type_id, length_type_id):
    global bits

    # The operator packet has sub packets in the next X bits
    if length_type_id == '0':
        length_sub_packets = int(next_bits(15), 2)
        p = {
            'version': version,
            'type_id': type_id,

            # Return the sub packets of this packet, which are part of the next n bits
            'sub_packets': parse_packets(max_bits=length_sub_packets)
        }

    # The operator packet has X sub packets
    else:
        num_sub_packets = int(next_bits(11), 2)
        p = {
            'version': version,
            'type_id': type_id,

            # Return the next X sub_packets we find
            'sub_packets': parse_packets(num_packets=num_sub_packets)
        }

    return p


# Recursively parse the packets
def parse_packets(max_bits=float('inf'), num_packets=float('inf')):
    global bits

    # Packets found and number of bits used
    packets_found = []
    bits_used = 0
    while bits_used < max_bits and len(packets_found) < num_packets:
        # Get the initial length of the bits, to find out the total length of the packet
        initial_bit_len = len(bits)

        # Extract the version and the typeID from the bits
        version = int(next_bits(3), 2)
        type_id = int(next_bits(3), 2)

        # It's a literal value packet
        if type_id == 4:
            p = literal_value_packet(version, type_id)

        # It's a operator packet
        else:
            length_type_id = next_bits(1)
            p = operator_packet(version, type_id, length_type_id)

        packets_found += [p]

        # Find the packet length
        packet_len = initial_bit_len - len(bits)
        bits_used += packet_len

        # If there are only 0s left, return
        if bits == '0' * len(bits):
            break
    return packets_found


# Product of a list
def prod(values: list):
    total = 1
    for v in values:
        total *= v
    return total


# Define the greater then function
def greater_than(values: list):
    return 1 if values[0] > values[1] else 0


# Define the less then function
def less_than(values: list):
    return 1 if values[0] < values[1] else 0


# Define the equal to function
def equal_to(values: list):
    return 1 if values[0] == values[1] else 0


# Evaluate the packets
def evaluate(packet: dict):
    type_id = packet['type_id']

    # Apply the operation associated with the type_id to the value of all sub_packets
    operation = None
    if type_id == 0:
        operation = sum
    elif type_id == 1:
        operation = prod
    elif type_id == 2:
        operation = min
    elif type_id == 3:
        operation = max
    elif type_id == 4:
        return packet['literal_value']
    elif type_id == 5:
        operation = greater_than
    elif type_id == 6:
        operation = less_than
    elif type_id == 7:
        operation = equal_to
    return operation([evaluate(sub_p) for sub_p in packet['sub_packets']])


def value_of_transmission(data: str):
    global bits

    bits = ''.join([hex_to_bin[char] for char in data])

    transmission = parse_packets()[0]

    return evaluate(transmission)


# Tests and Solution ----------
print(value_of_transmission('C200B40A82'))
print(value_of_transmission('04005AC33890'))
print(value_of_transmission('880086C3E88112'))
print(value_of_transmission('CE00C43D881120'))
print(value_of_transmission('D8005AC2A8F0'))
print(value_of_transmission('F600BC2D8F'))
print(value_of_transmission('9C005AC2F8F0'))
print(value_of_transmission('9C0141080250320F1802104A08'))
print(value_of_transmission(puzzle))
