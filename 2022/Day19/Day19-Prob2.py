# Solution for Problem 2 Day 19 of AoC 2022!

# Puzzle Input ----------
with open('Day19-Input.txt', 'r') as file:
    puzzle = file.read().split("\n")

with open('Day19-Test01.txt', 'r') as file:
    test01 = file.read().split("\n")

# Code ------------------
resources = ["GEODE", "OBSIDIAN", "CLAY", "ORE"]


# A class that specifies a robot's costs and mining type
class Robot:

    def __init__(self, resource: str, ore_cost=0, clay_cost=0, obsidian_cost=0):
        self.cost = {
            "ORE": ore_cost,
            "CLAY": clay_cost,
            "OBSIDIAN": obsidian_cost,
            "GEODE": 0
        }
        self.resourse = resource

    # Check if this robot can be built!
    def can_build(self, inventory: dict[str, int]) -> bool:
        for material in inventory:
            if inventory[material] < self.cost[material]:
                return False
        return True

    # Build a new robot (allows for negative ballances, use can_build first!)
    def build(self, inventory: dict[str, int], workers: dict) -> (dict[str, int], dict):
        for material in inventory:
            inventory[material] -= self.cost[material]
        workers[self.resourse] += 1
        return inventory, workers

    # The robot mines its resource
    def mine(self, inventory: dict[str, int], workers: dict) -> dict[str, int]:
        inventory[self.resourse] += workers[self.resourse]
        return inventory


# Create the Robot instances
def parse_robots(blueprint: list[str]) -> dict[str, Robot]:
    return {
        "ORE": Robot("ORE", ore_cost=int(blueprint[6])),
        "CLAY": Robot("CLAY", ore_cost=int(blueprint[12])),
        "OBSIDIAN": Robot("OBSIDIAN", ore_cost=int(blueprint[18]), clay_cost=int(blueprint[21])),
        "GEODE": Robot("GEODE", ore_cost=int(blueprint[27]), obsidian_cost=int(blueprint[30]))
    }


# Calculate if we still need a material or not, based on if we have enough of that material to build robots every turn
def items_needed(robots: dict[str, Robot], inventory: dict[str, int], workers: dict[str, int], max_time: int,
                 time: int):
    items = ["GEODE"]
    if inventory["OBSIDIAN"] + (max_time - time) * workers["OBSIDIAN"] < (max_time - time) * robots["GEODE"].cost[
        "OBSIDIAN"]:
        items += ["OBSIDIAN"]
    if inventory["CLAY"] + (max_time - time) * workers["CLAY"] < (max_time - time) * robots["OBSIDIAN"].cost["CLAY"]:
        items += ["CLAY"]
    items += ["ORE"]
    return items


memory = []


# Optimize this blueprint
def optimize(robots: dict[str, Robot], inventory: dict[str, int], workers: dict[str, int], max_time: int,
             time: int) -> int:
    global memory

    # No more time!
    time += 1
    if time > max_time:
        return inventory["GEODE"]

    # If we have achieved this number of workers with more items in our inventory, stop exploring this route
    for prev_time in range(time, 0, -1):
        best_inventory = memory[prev_time].get(str(workers), -1)
        if best_inventory != -1:
            for material in best_inventory:
                if best_inventory[material] < inventory[material]:
                    break
            else:
                return 0

    # Save state to memory
    memory[time][str(workers)] = inventory
    memory[time]["GEODE"] = max(memory[time].get("GEODE", -1), inventory["GEODE"])

    # Create the inventory at the end of this time step
    new_inventory = inventory.copy()
    for material in robots:
        new_inventory = robots[material].mine(new_inventory.copy(), workers.copy())

    # Create robots to be ready at the end of this time step
    average_ore_cost = robots["GEODE"].cost["ORE"] + robots["OBSIDIAN"].cost["ORE"]
    can_build = []
    for material in resources:

        # See if we can build this type of robot
        if robots[material].can_build(inventory):
            can_build += [material]

            # Build GEODE robot if we can
            if material == "GEODE" and inventory["ORE"] > average_ore_cost + 1:
                next_inventory, next_workers = robots[material].build(new_inventory.copy(), workers.copy())
                return optimize(robots, next_inventory.copy(), next_workers.copy(), max_time, time)

            # Build OBSIDIAN robot if we can
            elif material == "OBSIDIAN" and inventory["ORE"] > average_ore_cost + 1:
                next_inventory, next_workers = robots[material].build(new_inventory.copy(), workers.copy())
                return optimize(robots, next_inventory.copy(), next_workers.copy(), max_time, time)
    else:
        max_geodes = 0

        # Needed items
        needed = items_needed(robots, inventory, workers, max_time, time)
        for material in needed:

            # Build robots we can and need
            if material in can_build:
                next_inventory, next_workers = robots[material].build(new_inventory.copy(), workers.copy())
                max_geodes = max(max_geodes,
                                 optimize(robots, next_inventory.copy(), next_workers.copy(), max_time, time))

        # Don't save up resources
        if can_build == needed:
            return max_geodes

        len_can_build = len(can_build)
        if len_can_build == 4 or (len_can_build == 3 and workers["OBSIDIAN"] == 0) or (
                len_can_build == 2 and workers["OBSIDIAN"] + workers["CLAY"] == 0):
            return max_geodes

        # Save up resources
        else:
            return max(max_geodes, optimize(robots, new_inventory.copy(), workers.copy(), max_time, time))


def solution_day19_prob2(puzzle_in: list):
    global memory
    puzzle_in = list(map(lambda y: y.split(" "), list(filter(lambda x: len(x) > 1, puzzle_in))))[:3]
    max_time = 32

    total = 1
    for index, blueprint in enumerate(puzzle_in):
        inventory = {
            "ORE": 0,
            "CLAY": 0,
            "OBSIDIAN": 0,
            "GEODE": 0
        }
        workers = {
            "ORE": 1,
            "CLAY": 0,
            "OBSIDIAN": 0,
            "GEODE": 0
        }
        memory = [dict() for _ in range(max_time + 1)]
        robots = parse_robots(blueprint)
        max_geodes = optimize(robots, inventory, workers, max_time, 0)
        print(index + 1, max_geodes)
        total *= max_geodes
    return total


# Tests and Solution ---
print("Tests:")
print(solution_day19_prob2(test01))
print("\nSolution:")
print(solution_day19_prob2(puzzle))


# Note to self:
# To optimize this I think I can do it in a completely different manner!
# Instead of simulating every time step, jump ahead until I can build a new robot
# So, at the beggining of optimize I get the robots I've unlocked
# (ORE and CLAY in the beggining, if I have clay add OBSIDIAN and if I have OBSIDIAN add GEODE)
# Then decide what robot to build and jump ahead to the time I have the materials to build it!
# To do this, calculate how many mining rounds I have to do and do them all at once (kinda like Day 16!)
