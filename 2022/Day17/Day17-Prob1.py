# Solution for Problem 1 Day 17 of AoC 2022!

# Puzzle Input ----------
with open('Day17-Input.txt', 'r') as file:
    puzzle = list(file.read())

with open('Day17-Test01.txt', 'r') as file:
    test01 = list(file.read())


# Code ------------------
rocks = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]


class Rock:

    def __init__(self, start: list[int, int], coordinates: list[tuple[int, int]]):
        self.x_start = start[0]
        self.y_start = start[1]
        self.coordinates = [[start[0] + x_delta, start[1] + y_delta] for x_delta, y_delta in coordinates]

    # Move all coordinates of this rock
    def move(self, x_move: int, y_move: int, x_min: int, x_max: int, y_max: list[int], y_occupied: list[set]) -> bool:
        new_coordinates = []
        for pos in self.coordinates:
            x, y = pos
            new_x, new_y = x + x_move, y + y_move
            if x_max >= new_x >= x_min and new_y + 1 not in y_occupied[new_x]:
                new_coordinates += [[new_x, new_y]]
            else:
                break

        # The rock does not collide
        else:
            self.coordinates = new_coordinates
            return True

        # The rock collides
        return False


def solution_day17_prob1(puzzle_in: list):
    x_min, x_max = 0, 6
    y_max = [0 for _ in range(x_min, x_max + 1)]
    y_occupied = [{0} for _ in range(x_min, x_max + 1)]
    len_jet = len(puzzle_in)

    start = [2, 3]
    jet = 0
    for index in range(2022):
        # Create the rock
        rock = Rock(start, rocks[index % 5])

        while True:
            # Move the rock left or right
            x_move = -1 if puzzle_in[jet] == '<' else 1
            rock.move(x_move, 0, x_min, x_max, y_max, y_occupied)
            jet = (jet + 1) % len_jet

            # Move the rock down
            moved = rock.move(0, -1, x_min, x_max, y_max, y_occupied)
            if not moved:
                for coord in rock.coordinates:
                    start[1] = max(start[1], coord[1] + 1 + 3)
                    y_max[coord[0]] = max(y_max[coord[0]], coord[1] + 1)
                    y_occupied[coord[0]].add(coord[1] + 1)
                break

    return max(y_max)


# Tests and Solution ---
print("Tests:")
print(solution_day17_prob1(test01))
print("\nSolution:")
print(solution_day17_prob1(puzzle))
