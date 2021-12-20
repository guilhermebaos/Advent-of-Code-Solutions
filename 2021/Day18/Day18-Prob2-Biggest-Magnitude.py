from copy import deepcopy

# Puzzle Input ----------
with open('Day18-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day18-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

with open('Day18-Test02.txt', 'r') as file:
    test02 = file.read().split('\n')


# Main Code ----------

# SnailNumber class
class SnailNumber:
    def __init__(self, snail_number, parent=None):
        # Separate the x and y values of the snail number
        x = snail_number[0]
        y = snail_number[1]
        if type(x) == list:
            x = SnailNumber(x, parent=self)
        if type(y) == list:
            y = SnailNumber(y, parent=self)

        # Save the snail number's x and y values
        self.x = x
        self.y = y
        self.parent = parent

        self.numbers_found, self.snails_found = explore(self)

    # Addition
    def __add__(self, other):
        # The result is the composition of the numbers
        result = SnailNumber([self, other])

        # Keep trying to explode and split the number until it is impossible to do so (it's reduced)
        did_explode, did_split = True, False
        while did_explode or did_split:
            did_explode = explode(result)
            if did_explode:
                continue
            did_split = split(result)
        return result

    def __str__(self):
        return f'[{str(self.x)}, {str(self.y)}]'


def explore(snail_number, depth=0):
    x, y = snail_number.x, snail_number.y

    snails_found = []
    numbers_found = []
    for item, position in zip([x, y], ['x', 'y']):
        # If we find another SnailNumber, mark it's parent
        if isinstance(item, SnailNumber):

            # Snail Numbers and their parents
            snails_found += [item]
            item.parent = snail_number

            # Explore their children
            new_numbers_found, new_snails_found = explore(item, depth + 1)

            # Save the new numbers and snail numbers found
            numbers_found += new_numbers_found
            snails_found += new_snails_found

        elif type(item) == int:
            # Literal number found, store it in a tuple with:
            # The value of the number
            # The parent
            # The position -> either 'x' or 'y'
            # The depth
            numbers_found += [[item, snail_number, position, depth]]
    return numbers_found, snails_found


def explode(snail_number):
    index = 0
    while index < len(snail_number.numbers_found):
        number, num_parent, position, depth = snail_number.numbers_found[index]

        # If we have to explode a number
        # We consider only the literal numbers in position 'x' because we can also do 'y' numbers at the same times
        if depth == 4 and position == 'x':
            explode_x = number
            explode_y = snail_number.numbers_found[index + 1][0]

            # Add exploded_x to the number before, if it exists
            if index > 0:
                number, num_parent, position, depth = snail_number.numbers_found[index - 1]

                snail_number.numbers_found[index - 1][0] += explode_x
                if position == 'x':
                    num_parent.x += explode_x
                else:
                    num_parent.y += explode_x

            # Add exploded_y to the next number, if it exists
            if index < len(snail_number.numbers_found) - 2:
                number, num_parent, position, depth = snail_number.numbers_found[index + 2]

                snail_number.numbers_found[index + 2][0] += explode_y
                if position == 'x':
                    num_parent.x += explode_y
                else:
                    num_parent.y += explode_y

            # Put a 0 in the exploded pair's place (by accessing the parent)
            number, num_parent, position, depth = snail_number.numbers_found[index]
            if type(num_parent.parent.x) != int:
                zero_position = 'x'
                num_parent.parent.x = 0
            else:
                zero_position = 'y'
                num_parent.parent.y = 0

            # Erase the two deleted numbers and add a 0 in their place
            # Essentially, add the new literal number to the list of numbers found in this snail number
            snail_number.numbers_found.pop(index)
            snail_number.numbers_found[index] = [0, num_parent.parent, zero_position, depth - 1]
            return True
        index += 1
    return False


def split(snail_number):
    index = 0
    while index < len(snail_number.numbers_found):
        # Extract the next literal number
        number, num_parent, position, depth = snail_number.numbers_found[index]

        # If the number has to be split
        if number >= 10:

            # Calculate x and y values of the new Snail Number
            left_element = int(number / 2)
            right_element = number - int(number / 2)

            # Create new Snail Number with the right parents
            if position == 'x':
                num_parent.x = SnailNumber([left_element, right_element], num_parent)
                this_parent = num_parent.x
            else:
                num_parent.y = SnailNumber([left_element, right_element], num_parent)
                this_parent = num_parent.y

            # Add the new literal numbers to the list of numbers found in this snail number
            snail_number.numbers_found[index] = [left_element, this_parent, 'x', depth + 1]
            snail_number.numbers_found.insert(index + 1, [right_element, this_parent, 'y', depth + 1])
            index -= 1
            if depth == 3:
                return True
        index += 1
    return False


# Find the magnitude of a snail number
def magnitude(snail_number):
    x, y = snail_number.x, snail_number.y

    # Recursively find out the magnitude of each component of this snail number
    mag_x = x if type(x) == int else magnitude(x)
    mag_y = y if type(y) == int else magnitude(y)

    return 3 * mag_x + 2 * mag_y


def parse_number(num_str: list):
    # Variables for the x and y values of this number
    x, y = None, None
    snail_number = []

    # Analyse one character at a time
    while len(num_str) > 0:
        next_char = num_str.pop(0)

        # Parse the x element of the Snail Number
        if next_char == '[':
            num_str, x = parse_number(num_str)

        # Parse the y element of the Snail Number
        elif next_char == ',':
            num_str, y = parse_number(num_str)

        # Join the x and y elements into a list
        elif next_char == ']':
            snail_number = [x, y]
            break
        else:
            return num_str, int(next_char)

    # Return the list and the remaining string
    return num_str, snail_number


# Return the magnitude of the sum of all numbers
def solve_homework(num_str: list):
    # Parse the snail numbers into a list
    snail_numbers = []
    for num in num_str:
        snail_numbers += [parse_number(list(num))[1]]
    snail_numbers = list(map(SnailNumber, snail_numbers))

    # Add the possible magnitudes to the total
    all_magnitudes = []
    for num1 in snail_numbers:
        for num2 in snail_numbers:
            # Using deepcopy because my SnailNumber Class changes its own properties after a sum
            temp1, temp2 = deepcopy(num1), deepcopy(num2)
            if num1 != num2:
                all_magnitudes += [magnitude(temp1 + temp2)]

    # Return the magnitude of the total
    return max(all_magnitudes)


# Tests and Solution ----------
print(solve_homework(test01))
print(solve_homework(test02))
print(solve_homework(puzzle))
