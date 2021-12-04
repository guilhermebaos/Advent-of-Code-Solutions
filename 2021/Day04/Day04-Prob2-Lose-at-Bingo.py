# Puzzle Input ----------
with open('Day04-Input.txt', 'r') as file:
    puzzle = file.read().split('\n\n')

with open('Day04-Test01.txt', 'r') as file:
    test01 = file.read().split('\n\n')


# Main Code ----------

# Convert the board string into a list
def process_board(raw_board):
    new_board = []
    for row in raw_board.split('\n'):
        new_board += [row.split()]
    return new_board


# Find the set of all the numbers on a board
def find_numbers(board):
    nums = []
    for row in board:
        nums += [item for item in row]
    return set(nums)


# Find all lines (rows and columns) on a board, save them as a set
def find_lines(board):
    lines = []

    # Save the rows and organize the columns
    columns = list([] for _ in range(len(board)))
    for row in board:
        lines += [set(row)]
        for index, item in enumerate(row):
            columns[index] += [item]

    # Save the columns
    for col in columns:
        lines += [set(col)]
    return lines


# Simple Bingo Board class
class BingoBoard:
    def __init__(self, raw_board):
        self.board = process_board(raw_board)
        self.numbers = find_numbers(self.board)
        self.lines = find_lines(self.board)

        # When does this board win
        self.position = -1


# Determine the last winner and return its score
def find_last_winner(boards):
    # Numbers that were picked
    num_order = boards[0].split(',')

    # Bingo Boards
    bingo_boards = [BingoBoard(b) for b in boards[1:]]
    bingo_boards_len = len(bingo_boards)

    # Find the last winner and the score
    position = 0
    loser, nums, max_index = None, None, None
    for max_index, _ in enumerate(num_order):

        # All numbers until now
        last_index = max_index + 5
        nums = set(num_order[:last_index])

        # Test for every row if that row if in the set of all numbers chosen until now
        for board in bingo_boards:
            if board.position != -1:
                continue
            for line in board.lines:

                # If a board wins, break after checking if it was the last winner
                if len(nums.intersection(line)) == 5:
                    board.position = position
                    position += 1

                    if position == bingo_boards_len:
                        loser = board
                        break
                    break
            if loser:
                break

        if loser:
            break

    # Calculate the score
    unmarked = loser.numbers.difference(nums)

    score = sum(list(map(int, list(unmarked)))) * int(num_order[last_index - 1])
    return score


# Tests and Solution ----------
print(find_last_winner(test01))
print(find_last_winner(puzzle))
