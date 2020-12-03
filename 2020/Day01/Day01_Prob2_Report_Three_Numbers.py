# Puzzle_input
with open('Day01_Input.txt', 'r') as puzzle_input:
    expense_report = puzzle_input.read().split('\n')

expense_report = list(map(int, expense_report))

for pos1, exp1 in enumerate(expense_report):
    for pos2, exp2 in enumerate(expense_report[pos1 + 1:]):
        for exp3 in expense_report[pos2 + 1:]:
            if exp1 + exp2 + exp3 == 2020:
                print(exp1 * exp2 * exp3)
