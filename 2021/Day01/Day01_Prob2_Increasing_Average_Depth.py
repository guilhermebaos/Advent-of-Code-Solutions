# Puzzle Input ----------
with open('Day01_Input.txt', 'r') as file:
    puzzle = list(map(int, file.read().split('\n')))

with open('Day01_Test01.txt', 'r') as file:
    test01 = list(map(int, file.read().split('\n')))


# Main Code ----------

# Sums three measurements and compare one sum with the next
def average_depth_increase(depth_list):
    total = 0
    measurement1 = sum(depth_list[0:3])
    for index, _ in enumerate(depth_list[:-2]):
        measurement2 = sum(depth_list[index + 1: index + 4])

        # Add to the total if the sum increases
        total += 1 if measurement2 > measurement1 else 0

        # The next first measurement is the current second measurement
        # Think about comparing A to B and then B to C
        measurement1 = measurement2
    return total


# Tests and Solution ----------
print(average_depth_increase(test01))
print(average_depth_increase(puzzle))
