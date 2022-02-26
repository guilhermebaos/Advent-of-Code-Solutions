from copy import deepcopy

# Puzzle Input ----------
with open('Day24-Input.txt') as file:
    puzzle = file.read().split('\n')


# Main Code ----------

# Parse the monad parameters for each set of instructions
def monad_parameters(monad_code):
    all_parameters = []
    for start in range(14):
        a = int(monad_code[start * 18 + 4].split()[2])
        b = int(monad_code[start * 18 + 5].split()[2])
        c = int(monad_code[start * 18 + 15].split()[2])
        all_parameters += [(a, b, c)]
    return all_parameters


# Execute one digit of monad
def monad_digit(digit: int, index: int, z: int, parameters: list):
    a, b, c = parameters[index]
    x = (z % 26 + b) != digit
    z = int(z / a)

    if x:
        z *= 26
        z += digit + c
    return z, x


# Find the smallest model number possible
def smallest_model_num(monad_code):
    parameters = monad_parameters(monad_code)
    # By analysing the parameters, we see that whenever b >= 10 we  have a = 1 AND whenever b < 10 we have a = 26
    # This means that whenever b >= 10, x is 1, because it's impossible for z % 26 + b to be only one digit
    # As such, whenever b >= 10, z is going to increase by a factor of 26
    # And, whenever b < 10, there's a chance that z is going to decrease by a factor of 26
    # Because there are equal number of increases and decreases, in order for the number to be 0, it has to decrease
    # every chance it gets to
    decrease = [index for index, param in enumerate(parameters) if param[1] < 10]

    # Model numbers to check, with (number, depth, current_z)
    to_check = [(str(x), 0, 0) for x in range(1, 10)]

    while True:
        num, depth, old_z = to_check.pop(0)
        z, x = monad_digit(int(num[-1]), depth, old_z, parameters)

        # If the z value didn't decrease when it should have, this number won't lead to a valid model number
        if depth in decrease and x:
            continue

        # See if the number is a valid model number
        if depth == 13:
            if z == 0:
                return num
        else:
            to_check = [(num + str(x), depth + 1, z) for x in range(1, 10)] + to_check


# Tests and Solution ----------
print(smallest_model_num(puzzle))
