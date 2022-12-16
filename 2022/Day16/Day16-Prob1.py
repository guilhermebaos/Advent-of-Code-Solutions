# Solution for Problem 1 Day 16 of AoC 2022!
import re

# Puzzle Input ----------
with open('Day16-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day16-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------
memory = dict()
total_time = 30


# Calculate the distance between two valves
def calculate_distance(here: str, to: str, tunnels: dict) -> int:
    if here == to:
        return 0

    # Get value from memory
    map_here = memory.get(here, dict())
    dist = map_here.get(to, -1)
    if dist != -1:
        return dist

    # Find the distance
    paths = [[here]]
    while True:
        explore = paths.pop(0)
        current = explore[-1]
        for item in tunnels[current]:

            # Save the distance to memory and return it
            if item == to:
                dist = len(explore)
                map_to = memory.get(to, dict())
                map_to[here] = dist
                memory[to] = map_to

                map_here[to] = dist
                memory[here] = map_here
                return map_here[to]
            paths += [explore + [item]]


# Explore all working vents
def explore_vents(current: str, current_pressure: int, time: int, working: dict, tunnels: dict) -> int:
    # No more time or no more vents
    if len(working) == 0 or time >= 30:
        return current_pressure

    else:
        maxi = current_pressure
        all_valves = list(working.keys())
        for i in range(len(working)):
            # Move to and open valve w
            valve = all_valves[i]
            flow = working.pop(valve)
            dist = calculate_distance(current, valve, tunnels)
            new_time = time + dist + 1
            if new_time >= 30:
                continue

            # Open any valve after this one
            maxi = max(maxi, explore_vents(valve, current_pressure + flow * (total_time - new_time), new_time, working.copy(), tunnels))

            # Add the valve back into the working valves
            working[valve] = flow
        return maxi


def solution_day16_prob1(puzzle_in: list):
    global memory
    memory = dict()

    # Parse the input
    puzzle_in = list(map(lambda x: re.split("\s|=|;\s|,\s", x), puzzle_in))

    # Get valves and tunnel connections, and working valves flow rate
    tunnels = dict()
    working = dict()
    for item in puzzle_in:
        here = item[1]
        rate = int(item[5])
        to = item[10:]

        tunnels[here] = to
        if rate != 0:
            working[here] = rate

    return explore_vents("AA", 0, 0, working, tunnels)


# Tests and Solution ---
print("Tests:")
print(solution_day16_prob1(test01))
print("\nSolution:")
print(solution_day16_prob1(puzzle))
