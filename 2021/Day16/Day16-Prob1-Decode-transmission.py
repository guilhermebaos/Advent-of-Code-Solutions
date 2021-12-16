# Puzzle Input ----------
with open('Day16-Input.txt', 'r') as file:
    puzzle = file.read()

with open('Day16-Test01.txt', 'r') as file:
    test01 = file.read()

with open('Day16-Test02.txt', 'r') as file:
    test02 = file.read()

with open('Day16-Test03.txt', 'r') as file:
    test03 = file.read()

with open('Day16-Test04.txt', 'r') as file:
    test04 = file.read()


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


# Evaluate the packets
def evaluate(packets: list):
    total_sum = 0

    # Use BFS to sum all the versions in the packets
    check_next = packets.copy()
    while len(check_next) > 0:
        check_now = check_next.copy()
        check_next = []

        for p in check_now:
            total_sum += p['version']

            # Add the sub packets to check next
            sub_packets = p.get('sub_packets', [])
            for sub_p in sub_packets:
                check_next += [sub_p]

    return total_sum


def get_sum_versions(data: str):
    global bits

    # Get the bits
    bits = ''.join([hex_to_bin[char] for char in data])

    # Get the packets
    packets = parse_packets()

    # Return after evaluating
    return evaluate(packets)


# Tests and Solution ----------
print(get_sum_versions(test01))
print(get_sum_versions(test02))
print(get_sum_versions(test03))
print(get_sum_versions(test04))
print(get_sum_versions(puzzle))
