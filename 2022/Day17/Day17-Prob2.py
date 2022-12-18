# Solution for Problem 2 Day 17 of AoC 2022!

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


def solution_day17_prob2(puzzle_in: list):
    x_min, x_max = 0, 6
    y_max = [0 for _ in range(x_min, x_max + 1)]
    y_occupied = [{0} for _ in range(x_min, x_max + 1)]
    len_jet, len_rocks = len(puzzle_in), len(rocks)

    start = [2, 3]
    jet, loop_index = 0, 0
    states, y_maxes = [], []
    iterations = 1000000000000
    saved_rocks = 200 # Rock points to save in the state
    for index in range(iterations):

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

        # Create this state and see if it is a repeat of some other state
        height = max(y_max)
        last_y_occupied = [{-1} for _ in range(x_min, x_max + 1)]
        for x, col in enumerate(y_occupied):
            to_add = [x - (height - saved_rocks) if x >= (height - saved_rocks) else -1 for x in col] if height >= saved_rocks else [x for x in col]
            last_y_occupied[x].update(set(to_add))
        this_state = (index % len_rocks, jet % len_jet, last_y_occupied)
        if len(states) > saved_rocks and this_state in states:
            loop_index = states.index(this_state)
            states += [this_state]
            y_maxes += [height]
            break
        states += [this_state]
        y_maxes += [height]
    else:
        return y_maxes[-1]

    len_loop = len(states) - loop_index - 1
    height_loop = y_maxes[-1] - y_maxes[loop_index]
    num_loop = (iterations - loop_index - 1) // len_loop
    num_remaining = (iterations - loop_index - 1) % len_loop

    y_maxes = [x - y_maxes[loop_index] if index > loop_index else x for index, x in enumerate(y_maxes)]
    return y_maxes[loop_index] + height_loop * num_loop + (y_maxes[num_remaining + loop_index] if num_remaining != 0 else 0)


# Tests and Solution ---
print("Tests:")
print(solution_day17_prob2(test01))
print("\nSolution:")
print(solution_day17_prob2(puzzle))
