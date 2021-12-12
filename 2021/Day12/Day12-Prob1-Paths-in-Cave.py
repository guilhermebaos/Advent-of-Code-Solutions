# Puzzle Input ----------
with open('Day12-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day12-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')

with open('Day12-Test02.txt', 'r') as file:
    test02 = file.read().split('\n')

with open('Day12-Test03.txt', 'r') as file:
    test03 = file.read().split('\n')


# Main Code ----------

# Parse the connections into a dictionary
def parse_paths(data: list):
    connections = dict()

    # Add the connections to both dictionary entries
    for conn in data:
        start, end = conn.split('-')
        connections[start] = connections.get(start, []) + [end]
        connections[end] = connections.get(end, []) + [start]
    return connections


# Recursively find all paths
all_paths = []


def search_all_paths(connections: dict, path: list):
    global all_paths
    check_next = path[-1]

    # Check all connections leaving from our current cave
    for cave in connections[check_next]:
        # Don't go back to start
        if cave == 'start':
            continue

        # End at end
        elif cave == 'end':
            all_paths += [path + ['end']]

        # Only explore each small cave once
        elif cave.islower():
            if cave not in path:
                search_all_paths(connections, path + [cave])

        # Go into big caves as many times as we want
        else:
            search_all_paths(connections, path + [cave])


def find_all_paths(data: list):
    global all_paths
    all_paths = []

    # Parse the connections and feed them to search_all_paths, starting at start
    connections = parse_paths(data)
    search_all_paths(connections, ['start'])
    return len(all_paths)


# Tests and Solution ----------
print(find_all_paths(test01))
print(find_all_paths(test02))
print(find_all_paths(test03))
print(find_all_paths(puzzle))
