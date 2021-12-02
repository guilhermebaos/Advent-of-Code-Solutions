# Puzzle Input ----------
with open('Day01-Input.txt', 'r') as file:
    puzzle = list(map(int, file.read().split('\n')))

with open('Day01-Test01.txt', 'r') as file:
    test01 = list(map(int, file.read().split('\n')))


# Main Code ----------

# Compare the depth with the next one
def depth_increase(depth_list):
    total = 0
    for index, depth in enumerate(depth_list[:-1]):

        # If the next depth is higher, add to the total
        total += 1 if depth_list[index + 1] > depth else 0
    return total


# Tests and Solution ----------
print(depth_increase(test01))
print(depth_increase(puzzle))
