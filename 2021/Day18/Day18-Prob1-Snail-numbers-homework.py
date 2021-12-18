# Puzzle Input ----------
with open('Day18-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day18-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

def explore(snail_number, depth=0):
    x, y = snail_number.x, snail_number.y

    snails_found = []
    numbers_found = []
    for i, str_i in zip([x, y], ['x', 'y']):
        if isinstance(i, SnailNumber):

            i.depth = depth
            snails_found += [i]

            new_numbers_found, new_snails_found = explore(i, depth+1)

            numbers_found += new_numbers_found
            snails_found += new_snails_found
        elif type(i) == int:
            numbers_found += [{i: (snail_number, str_i)}]
    return numbers_found, snails_found


def explode(snail_number):
    numbers_found, snails_found = explore(snail_number)
    for index, sn in enumerate(snails_found):
        if sn.depth == 4:
            exploded_x, exploded_y = sn.x, sn.y
            if index > 0:
                pass
        print(sn, sn.depth)

    for n in numbers_found:
        print(n)
    return False


class SnailNumber:
    def __init__(self, snail_number, parent=None):
        x = snail_number[0]
        y = snail_number[1]

        if type(x) == list:
            x = SnailNumber(x, parent=self)
        if type(y) == list:
            y = SnailNumber(y, parent=self)
        self.x = x
        self.y = y
        self.parent = parent

    def __add__(self, other):
        result = SnailNumber([self, other])
        did_explode, did_split = True, False
        while did_explode or did_split:
            did_explode = explode(result)
            if did_explode:
                continue
            did_split = False
        return result

    def __str__(self):
        return f'[{str(self.x)}, {str(self.y)}]'


def parse_number(num_str: list):
    x, y = None, None
    snail_number = []
    while len(num_str) > 0:
        next_char = num_str.pop(0)
        if next_char == '[':
            num_str, x = parse_number(num_str)
        elif next_char == ',':
            num_str, y = parse_number(num_str)
        elif next_char == ']':
            snail_number = [x, y]
            break
        else:
            return num_str, int(next_char)

    return num_str, snail_number


# Return the magnitude off the result of the homework
def solve_homework(num_str: list):
    snail_numbers = []
    for num in num_str:
        snail_numbers += [parse_number(list(num))[1]]
    snail_numbers = list(map(SnailNumber, snail_numbers))

    for x in snail_numbers:
        print(x)


# Tests and Solution ----------
# print(SnailNumber([1, 2]) + SnailNumber([[3, 4], 5]))
print(SnailNumber([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) + SnailNumber([1, 2]))
# print(solve_homework(test01))
