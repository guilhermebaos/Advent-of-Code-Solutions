# Puzzle_input
with open('Day1_Input.txt', 'r') as puzzle_input:
    expense_report = puzzle_input.read().split('\n')

expense_report = list(map(int, expense_report))

for pos1, exp1 in enumerate(expense_report):
    for exp2 in expense_report[pos1 + 1:]:
        if exp1 + exp2 == 2020:
            print(exp1 * exp2)
