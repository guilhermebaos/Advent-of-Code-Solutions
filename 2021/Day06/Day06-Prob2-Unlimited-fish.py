# Puzzle Input ----------
with open('Day06-Input.txt', 'r') as file:
    puzzle = list(map(int, file.read().split(',')))

with open('Day06-Test01.txt', 'r') as file:
    test01 = list(map(int, file.read().split(',')))


# Main Code ----------

# Count the first few fish and organize them by age in a dictionary
def count_first_fish(fish_list: list):
    fish_per_age = dict()
    for fish in fish_list:
        fish_per_age[fish] = fish_per_age.get(fish, 0) + 1
    return fish_per_age


# See how many fish there are after n days at sea
def fish_in_n_days(fish_list: list, n: int):
    fish_per_age = count_first_fish(fish_list)

    # Simulate each day
    for _ in range(n):
        new_fish_per_age = dict()

        for age in fish_per_age:
            # Make fish reproduce and create new fish
            if age == 0:
                new_fish_per_age[8] = fish_per_age[age]
                new_fish_per_age[6] = new_fish_per_age.get(6, 0) + fish_per_age[age]

            # Decrease the timer in fish by 1
            else:
                new_fish_per_age[age - 1] = new_fish_per_age.get(age - 1, 0) + fish_per_age[age]

        fish_per_age = new_fish_per_age.copy()

    # Return the total number of fish
    return sum(fish_per_age.values())


# Tests and Solution ----------
print(fish_in_n_days(test01, 256))
print(fish_in_n_days(puzzle, 256))
