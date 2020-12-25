# Puzzle Input
with open('Day25_Input.txt') as puzzle_input:
    public_keys = puzzle_input.read().split('\n')

# Convert to integers
public_keys = list(map(int, public_keys))

# Separate the keys
card_key = public_keys[0]
door_key = public_keys[1]

# Define the parameters
prime_divisor = 20201227

# Brute force the card loop size
value = 1
subject_number = 7
card_loop_size = 0
while True:                     # Do the loop until the numbers match
    card_loop_size += 1             # Add one to
    value *= subject_number
    value %= prime_divisor
    if value == card_key:
        break

# Get the encryption key
value = 1
subject_number = door_key
for _ in range(card_loop_size):
    value *= subject_number
    value %= prime_divisor

# Get the encryption key
encryption_key = value

# Show the result
print(encryption_key)
