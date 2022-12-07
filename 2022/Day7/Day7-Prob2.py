# Solution for Problem 2 Day 7 of AoC 2022!

# Puzzle Input ----------
with open('Day7-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day7-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------

# Global variables
memory = {"/": set()}
sizes = {}


# Reset global variables
def reset_globals():
    global memory, sizes
    memory = {"/": set()}
    sizes = {}


# Get this directories parent directory
def get_parent_dir(directory: str):
    global memory
    for key in memory:
        if directory in memory[key]:
            return key
    raise ValueError("Directory not found in memory")


# Add an item to the current directory
def add_to_current_dir(directory: str, item) -> None:
    global memory

    content = memory.get(directory, set())
    content.add(item)
    memory[directory] = content
    return


# Read a line
def read_line(directory: str, line: str) -> str:
    global memory

    command = line.split(" ")

    # Execute the command
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "/":
                directory = "/"

            # Go back a directory if not in "/"
            elif command[2] == "..":
                if directory != 1:
                    directory = get_parent_dir(directory)

            # Change directory, add dir to the memory if not already there
            else:
                new_dir = directory + command[2] + "/"
                add_to_current_dir(directory, new_dir)

                directory = new_dir
        elif command[1] == "ls":
            pass

    # Add an item to memory
    else:
        content = line.split(" ")
        if content[0] == "dir":
            add_to_current_dir(directory, directory + command[1] + "/")
        else:
            add_to_current_dir(directory, (int(content[0]), content[1]))
    return directory


# Recursivly get all of the directories' sizes
def get_size_dir(directory: str) -> int:
    global memory, sizes

    total = 0
    contents = list(memory.get(directory, set()))

    if len(contents) == 0:
        sizes[directory] = 0

    for item in contents:

        # Get dir size and add it to total
        if type(item) == str:
            item_size = sizes.get(item, get_size_dir(item))
            total += item_size

        # Add item size to total
        else:
            total += item[0]
    sizes[directory] = total
    return total


def solution_day7_prob2(puzzle_in: list):
    global memory
    reset_globals()

    # Explore command list
    directory = "/"
    for line in puzzle_in:
        directory = read_line(directory, line)

    # Fill size dictionary
    get_size_dir("/")

    # Find smallest directory above threshold
    available_space = 70000000
    required_space = 30000000
    free_space = available_space - sizes["/"]
    needed_space = required_space - free_space
    sorted_sizes = sorted(sizes, key=sizes.get)
    for item in sorted_sizes:
        value = sizes[item]
        if value >= needed_space:
            return value

    return -1


# Tests and Solution ---
print("Tests:")
print(solution_day7_prob2(test01))
print("\nSolution:")
print(solution_day7_prob2(puzzle))
