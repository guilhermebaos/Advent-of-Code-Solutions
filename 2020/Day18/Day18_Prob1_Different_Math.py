# Puzzle Input
with open('Day18_Input.txt') as puzzle_input:
    expressions = puzzle_input.read().split('\n')


# Function to parse expressions
def map_expressions(el):                        # Get the element
    el = el.split(' ')                          # Split the element into a list, using spaces as a separator
    for item_index, item in enumerate(el):      # If an item of the element has a parenthesis, separate it (there are
        if '(' in item or ')' in item:          # no spaces on one side of the parenthesis)
            item = list(item)
            el[item_index: item_index + 1] = item       # Update the element
    return el


# Parse the expressions
expressions = list(map(map_expressions, expressions))


# Recursively evaluate expressions without parenthesis
def evaluate(expr):
    if len(expr) == 1:                  # If it's an integer represented by a string or list, return it as an int
        return int(expr[0])
    elif expr[1] == '+':                # If it's a sum, return the sum of the numbers before and after
        return evaluate([int(expr[0]) + int(expr[2])] + expr[3:])
    elif expr[1] == '*':                # It it's a product, return the product of the numbers before and after
        return evaluate([int(expr[0]) * int(expr[2])] + expr[3:])


# Get the parenthesis indexes
parenthesis = []
for exp in expressions:                 # For every expression:
    open_index = []                         # Open parenthesis indexes
    parenthesis += [[]]                     # Pairs of open, close indexes
    for index, elem in enumerate(exp):      # For every element in the expression:
        if '(' in elem:                         # If it's an open parenthesis, add its index to the stack
            open_index += [index]
        elif ')' in elem:                       # If it's a close parenthesis, pair it with the one on top of the stack
            parenthesis[-1] += [[open_index[-1], index]]
            open_index.pop(-1)                  # Update the stack

# Fully evaluate the expressions
total = 0
for exp, exp_parenthesis in zip(expressions, parenthesis):  # For every expression and correspondent parenthesis indexes
    for paren_index, paren in enumerate(exp_parenthesis):   # Evaluate the parenthesis
        exp[paren[0]:paren[1] + 1] = [evaluate(exp[paren[0] + 1:paren[1]])]
        delta_index = paren[0] - paren[1]                   # Update the other parenthesis' indexes
        for other_index, other_paren in enumerate(exp_parenthesis[paren_index + 1:]):
            for other_paren_index, other_paren_pos in enumerate(other_paren):
                if other_paren_pos > paren[1]:              # Only update if necessary
                    exp_parenthesis[paren_index + 1 + other_index][other_paren_index] += delta_index
    total += evaluate(exp)

# Show the total sum
print(total)
