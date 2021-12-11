# Puzzle Input ----------
with open('Day11-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day11-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Attribute an ID to each dumbo by putting them into a list
def id_to_dumbos(dumbos: list):
    dumbos_id = []
    for row in dumbos:
        dumbos_id += list(map(int, row))
    return dumbos_id


# See the IDs of nearby dumbos
def id_nearby_dumbos(dumbo_id: int):
    nearby_ids = list()

    # List of conditions
    have_left = dumbo_id % 10 != 0
    have_right = dumbo_id % 10 != 9
    have_up = dumbo_id >= 10
    have_down = dumbo_id <= 89

    # List of nearby dumbos
    if have_left:
        nearby_ids += [dumbo_id - 1]
    if have_right:
        nearby_ids += [dumbo_id + 1]
    if have_up:
        nearby_ids += [dumbo_id - 10]

        if have_right:
            nearby_ids += [dumbo_id - 9]
        if have_left:
            nearby_ids += [dumbo_id - 11]

    if have_down:
        nearby_ids += [dumbo_id + 10]

        if have_right:
            nearby_ids += [dumbo_id + 11]
        if have_left:
            nearby_ids += [dumbo_id + 9]

    return nearby_ids


# Simulate a step
def simulate_step(dumbos_with_ids: list, connections: dict):
    new_flashes = []

    # Find the first dumbos to flash
    for dumbo_id, dumbo_energy in enumerate(dumbos_with_ids):
        if dumbo_energy == 9:
            new_flashes += [dumbo_id]
        dumbos_with_ids[dumbo_id] += 1

    # Iterate through the flash to see how they affect nearby dumbos
    all_flashes = new_flashes[:]
    while len(new_flashes) > 0:
        current_flash = new_flashes.pop()
        current_connections = connections[current_flash]

        # Increase the energy of nearby dumbos
        for dumbo in current_connections:
            dumbos_with_ids[dumbo] += 1
            if dumbos_with_ids[dumbo] == 10:
                new_flashes += [dumbo]
                all_flashes += [dumbo]

    # Reset all dumbos that flashed energies to 0
    for dumbo in all_flashes:
        dumbos_with_ids[dumbo] = 0

    return len(all_flashes), dumbos_with_ids


# Total number of flashes
def num_flashes(dumbos: list, steps=100):
    dumbos_with_ids = id_to_dumbos(dumbos)

    # Find which dumbos are affected by each dumbo
    connections = dict()
    for dumbo_id, _ in enumerate(dumbos_with_ids):
        connections[dumbo_id] = id_nearby_dumbos(dumbo_id)

    # Find the step in which all dumbos flash (when there are 100 flashes)
    step = 0
    while True:
        step += 1
        new_flashes, dumbos_with_ids = simulate_step(dumbos_with_ids, connections)
        if new_flashes == 100:
            break
    return step


# Tests and Solution ----------
print(num_flashes(test01))
print(num_flashes(puzzle))
