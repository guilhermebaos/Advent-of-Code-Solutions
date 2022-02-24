from frozendict import frozendict

# Puzzle Input ----------
with open('Day23-Input.txt') as file:
    puzzle = file.read().split('\n')

with open('Day23-Test01.txt') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# See what amphipods are in each room
def process_burrow(burrow: list):
    rooms = [[] for _ in range(4)]
    for room_num, room_pos in enumerate(range(3, 10, 2)):
        for amphipod in range(2):
            rooms[room_num] += [burrow[amphipod + 2][room_pos]]

    # Coordinate system for the burrow
    coords = {f'H{str(hex(x))[-1]}': '.' for x in range(11)}
    hallway_coords = list(coords.keys())
    room_coords = []
    for room_letter, room in [('A', rooms[0]), ('B', rooms[1]), ('C', rooms[2]), ('D', rooms[3])]:
        for room_space, amphipod in enumerate(room):
            coords[f'{room_letter}{room_space}'] = amphipod
            room_coords += [f'{room_letter}{room_space}']
    return coords, hallway_coords, room_coords


# Get the energy per step associated with each amphipod
def energy_per_step(amphipod: str):
    energy_dict = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    return energy_dict[amphipod]


# See if the amphipod can and should leave the room
def can_leave_room(coords, start):
    # Ignore empty spaces
    if coords[start] == '.':
        return False

    room, y = start
    amphipod = coords[start]

    max_y = 1
    y = int(y)
    if amphipod != room:
        # It's on the room piece connecting to the hallway
        if y == 0:
            return True

        # See if the other room slots are blocked
        for room_y in range(y - 1, -1, -1):
            if coords[f'{room}{room_y}'] != '.':
                return False
        return True

    # If the amphipod is in the right room, see if there are only other amphipods of the same type in there
    else:
        for room_y in range(y, max_y + 1):
            if coords[f'{room}{room_y}'] != amphipod:
                return True
        return False


# See if a room only has the right type of amphipods
def room_right_amphipods(coords, amphipod):
    max_y = 1

    for room_y in range(max_y + 1):
        if not coords[amphipod + str(room_y)] in [amphipod, '.']:
            return False
    return True


# Get the possible moves the amphipods can make
def possible_moves(coords, hallway_coords: list, room_coords: list):
    moves = []

    # Coordinates of the rooms
    room_by_amphipod = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    for start in room_coords:
        if not can_leave_room(coords, start):
            continue

        amphipod = coords[start]

        # Check if the amphipod can go from one room to the right room
        if room_right_amphipods(coords, amphipod):

            # Check the hallway path to there is clear
            start_hall = room_by_amphipod[start[0]]
            end_hall = room_by_amphipod[amphipod]
            if end_hall > start_hall:
                path = [f'H{str(hex(x))[-1]}' for x in range(start_hall + 1, end_hall)]
            else:
                path = [f'H{str(hex(x))[-1]}' for x in range(end_hall + 1, start_hall)]
            path_blocked = False
            for item in path:
                if coords[item] != '.':
                    path_blocked = True
                    break
            if path_blocked:
                continue

            # Calculate energy and save this as a possible move
            end = amphipod + '1' if coords[amphipod + '1'] == '.' else amphipod + '0'
            steps = int(start[1]) + 1 + abs(start_hall - end_hall) + int(end[1]) + 1

            moves += [(start, end, steps * energy_per_step(amphipod))]

        for end in hallway_coords:
            if coords[end] != '.':
                continue

            # Check the hallway path there is clear
            start_hall = room_by_amphipod[start[0]]
            end_hall = int(end[1], 16)
            if end_hall > start_hall:
                path = [f'H{str(hex(x))[-1]}' for x in range(start_hall, end_hall + 1)]
            else:
                path = [f'H{str(hex(x))[-1]}' for x in range(end_hall, start_hall + 1)]
            path_blocked = False
            for item in path:
                if coords[item] != '.':
                    path_blocked = True
                    break
            if path_blocked:
                continue

            # Calculate energy and save this as a possible move
            steps = abs(start_hall - end_hall) + int(start[1]) + 1

            moves += [(start, end, steps * energy_per_step(amphipod))]

    # The amphipod starts in an hallway
    for start in hallway_coords:

        # Ignore empty spaces
        if coords[start] == '.':
            continue

        amphipod = coords[start]

        # Check if the room only has amphipods of the right type
        if room_right_amphipods(coords, amphipod):

            # Check that the hallway path to there is clear
            start_hall = int(start[1], 16)
            end_hall = room_by_amphipod[amphipod]
            if end_hall > start_hall:
                path = [f'H{str(hex(x))[-1]}' for x in range(start_hall + 1, end_hall)]
            else:
                path = [f'H{str(hex(x))[-1]}' for x in range(end_hall + 1, start_hall)]
            path_blocked = False
            for item in path:
                if coords[item] != '.':
                    path_blocked = True
                    break
            if path_blocked:
                continue

            # Calculate energy and save this as a possible move
            end = amphipod + '1' if coords[amphipod + '1'] == '.' else amphipod + '0'
            steps = abs(start_hall - end_hall) + int(end[1]) + 1

            moves += [(start, end, steps * energy_per_step(amphipod))]
    return moves


# See the theoretical minimum or maximum energy to get from the current state to the solution state
limit_energy_memory = dict()


def limit_energy(coords, minimum=True):
    if coords in limit_energy_memory:
        return limit_energy_memory[coords]
    max_y = 1

    # Coordinates of the rooms
    room_by_amphipod = {
        'A': 2,
        'B': 4,
        'C': 6,
        'D': 8
    }

    energy = 0
    for room in ['A', 'B', 'C', 'D']:
        for room_y in range(0, max_y + 1):
            amphipod = coords[room + str(room_y)]
            if amphipod == '.':
                continue

            start_hall = room_by_amphipod[room]
            end_hall = room_by_amphipod[amphipod]

            if minimum:
                steps = abs(end_hall - start_hall) + int(room_y) * 2 + 2
            else:
                steps = end_hall + start_hall + int(room_y) * 2 + 2
            energy += steps * energy_per_step(amphipod)

    for hallway_num in range(0, 11):
        hallway_str = str(hex(hallway_num))[-1]
        amphipod = coords['H' + hallway_str]
        if amphipod == '.':
            continue

        start_hall = hallway_num
        end_hall = room_by_amphipod[amphipod]

        if minimum:
            steps = abs(end_hall - start_hall) + 1
        else:
            steps = end_hall + start_hall + max_y + 1
        energy += steps * energy_per_step(amphipod)

    limit_energy_memory[coords] = energy
    return energy


# Do a move
def move_amphipod(coords, move: tuple):
    coords = dict(coords).copy()
    start, end, energy = move
    coords[start], coords[end] = '.', coords[start]
    return frozendict(coords)


def mini_energy_sort(burrow: list):
    coords, hallway_coords, room_coords = process_burrow(burrow)
    hallway_coords.remove('H2')
    hallway_coords.remove('H4')
    hallway_coords.remove('H6')
    hallway_coords.remove('H8')

    solution = {'H0': '.', 'H1': '.', 'H2': '.', 'H3': '.', 'H4': '.', 'H5': '.', 'H6': '.', 'H7': '.', 'H8': '.',
                'H9': '.', 'Ha': '.', 'A0': 'A', 'A1': 'A', 'B0': 'B', 'B1': 'B', 'C0': 'C', 'C1': 'C', 'D0': 'D',
                'D1': 'D'}

    coords = frozendict(coords)
    solution = frozendict(solution)

    connections = dict()
    connections[coords] = [0, None]

    mini_energy = limit_energy(coords, False)

    # Search all possible states
    while True:
        differences = False
        for start_coords in connections.copy():
            start_energy, end = connections[start_coords]

            # See if this node is the solution
            if start_coords == solution:
                mini_energy = min(mini_energy, start_energy)
                continue

            # See if this node has been searched
            if end:
                continue

            # See if this node is already above the solution energy
            if start_energy + limit_energy(start_coords) > mini_energy:
                continue

            end = list()

            # See every possible move we can make from here
            moves = possible_moves(start_coords, hallway_coords, room_coords)
            for m in moves:
                # Move consequences
                new_coords = move_amphipod(start_coords, m)
                new_energy = start_energy + m[2]

                # If we have seen this end state...
                if new_coords in connections:
                    seen_energy, seen_children = connections[new_coords]
                    delta_energy = new_energy - seen_energy

                    # ...and the new energy is lower than the one we had found, then recursively lower the energy of all children states
                    if delta_energy < 0:
                        differences = True
                        to_check = [(new_coords, delta_energy)]

                        while len(to_check) > 0:
                            parent_coords, delta_energy = to_check.pop()
                            parent_energy, children = connections[parent_coords]

                            connections[parent_coords] = [parent_energy + delta_energy, children]
                            if not children:
                                continue
                            for child in children:
                                child_coords, child_energy = child
                                child_energy += delta_energy

                                child_mini_energy, child_children = connections[child_coords]
                                child_delta_energy = child_energy - child_mini_energy
                                if child_delta_energy < 0:
                                    to_check += [(child_coords, child_delta_energy)]

                else:
                    differences = True
                    end += [(new_coords, new_energy)]
                    connections[new_coords] = [new_energy, None]
            connections[start_coords] = [start_energy, end]

        if not differences:
            break
        print(f'\nCurrent minimum energy: {mini_energy}')
        print(f'Current connections: {len(connections)}')

    return mini_energy


# Tests and Solution ----------
print(mini_energy_sort(test01))
print(mini_energy_sort(puzzle))

