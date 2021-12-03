# Puzzle Input ----------
with open('Day03-Input.txt', 'r') as file:
    puzzle = list(map(list, file.read().split('\n')))

with open('Day03-Test01.txt', 'r') as file:
    test01 = list(map(list, file.read().split('\n')))


# Main Code ----------
def power_consumption(diagnostic):
    # Size of binary numbers
    len_num = len(diagnostic[0])
    len_dgc = len(diagnostic)

    # Get the number of ones that appear in each position
    frequency_of_ones = [0 for _ in range(len_num)]
    for num in diagnostic:
        for index, bit in enumerate(num):
            frequency_of_ones[index] += int(bit)

    # Create the gamma and epsilon rates
    gamma, epsilon = [], []
    for frequency in frequency_of_ones:
        most_common = 1 if frequency > len_dgc / 2 else 0

        gamma += [str(most_common)]
        epsilon += [str(1 - most_common)]

    gamma, epsilon = int(''.join(gamma), 2), int(''.join(epsilon), 2)
    return gamma * epsilon


# Tests and Solution ----------
print(power_consumption(test01))
print(power_consumption(puzzle))
