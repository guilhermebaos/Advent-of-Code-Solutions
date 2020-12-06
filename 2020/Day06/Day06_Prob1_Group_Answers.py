import re

# Puzzle Input
with open('Day06_Input.txt') as puzzle_input:
    answers = puzzle_input.read().split('\n\n')

# Separate each person's answers with a Regular Expression
for index, group in enumerate(answers):
    answers[index] = re.split(r'\s', group)

    total_answers = set([])
    for person in answers[index]:
        for letter in person:
            total_answers.add(letter)

    answers[index] = total_answers

answers_len = map(len, answers)

print(sum(list(answers_len)))
