# Puzzle Input
with open('Day24_Input.txt') as puzzle_input:
    tile_directions = puzzle_input.read().split('\n')

# Parse tile directions
for index, directions in enumerate(tile_directions):
    directions = list(directions)                           # Convert from string to list, so it can be manipulated
    tile_directions[index] = []                             # Empty the list in tile_directions
    while True:
        try:
            if directions[0] == 'e':                        # If the next character is 'e', the direction is east
                tile_directions[index] += ['e']
                directions.pop(0)
            elif directions[0] == 's':                      # If the next character is 's', the direction is either
                if directions[1] == 'e':                        # southeast
                    tile_directions[index] += ['se']
                elif directions[1] == 'w':                      # or southwest
                    tile_directions[index] += ['sw']
                directions.pop(0)
                directions.pop(0)
            elif directions[0] == 'w':                      # If the next character is 'w', the direction is west
                tile_directions[index] += ['w']
                directions.pop(0)
            elif directions[0] == 'n':                      # If the next character is 'n', the direction is either
                if directions[1] == 'e':                        # northeast
                    tile_directions[index] += ['ne']
                elif directions[1] == 'w':                      # or northwest
                    tile_directions[index] += ['nw']
                directions.pop(0)
                directions.pop(0)
        except IndexError:
            break

# Get the coordinates of the end hexagons (3**0.5 in y axis is 1 on x axis)
black_tiles = []
for directions in tile_directions:
    hexagon_coor = [0, 0]                   # Reference tile
    for command in directions:              # Update coordinates for every command (Geometry was done beforehand)
        if command == 'e':
            hexagon_coor[0] -= 1
        elif command == 'se':
            hexagon_coor[0] -= 0.5
            hexagon_coor[1] -= 1.5
        elif command == 'ne':
            hexagon_coor[0] -= 0.5
            hexagon_coor[1] += 1.5
        elif command == 'w':
            hexagon_coor[0] += 1
        elif command == 'sw':
            hexagon_coor[0] += 0.5
            hexagon_coor[1] -= 1.5
        elif command == 'nw':
            hexagon_coor[0] += 0.5
            hexagon_coor[1] += 1.5
    if hexagon_coor in black_tiles:
        black_tiles.remove(hexagon_coor)
    else:
        black_tiles += [hexagon_coor[:]]

# Initial value for Conway's Game of Tiles
tile_states = []
tile_coordinates = []
for tile in black_tiles:
    tile_states += [1]
    tile_coordinates += [tile]

# Execute Conway's rules on the tilling
max_index = len(tile_coordinates)
tile_neighbors = [[] for _ in range(max_index)]
tile_neigh_index = [[] for _ in range(max_index)]
for day in range(100):
    # Update neighbors and get the full list of tiles we have to keep track of (tiles adjacent to black tiles)
    for index, color in enumerate(tile_states):
        if color == 1:                              # We only care about tiles next to black tiles, other won't change
            if len(tile_neighbors[index]) != 6:         # If that tile hasn't got a full list of neighbors:
                neighbors = tile_neighbors[index]           # Get it's current list
                x, y = tile_coordinates[index][:]           # Get the tiles coordinates

                # For every possible neighbor, make sure it exists and is in the neighbors' list
                for neigh_tile in [[x - 1, y], [x - 0.5, y - 1.5], [x - 0.5, y + 1.5], [x + 1, y], [x + 0.5, y - 1.5], [x + 0.5, y + 1.5]]:
                    if neigh_tile not in neighbors:                     # If it isn't in the list:
                        if neigh_tile in tile_coordinates:                  # If it exists:
                            neigh_index = tile_coordinates.index(neigh_tile)    # Get it's index
                        else:                                               # If it doesn't exist yet
                            neigh_index = max_index                             # The tile is new, assign it a new index
                            max_index += 1                                      # Update the maximum index

                            tile_coordinates += [neigh_tile]                    # Add the tile to all lists it needs to
                            tile_states += [0]                                  # be in and create placeholder lists
                            tile_neighbors += [[]]                              # fot the new tile's neighbors
                            tile_neigh_index += [[]]

                        # Add the other tile as this tile's neighbor
                        tile_neighbors[index] += [neigh_tile]
                        tile_neigh_index[index] += [neigh_index]

                        # Add this tile as the other tile's neighbor
                        tile_neighbors[neigh_index] += [[x, y]]
                        tile_neigh_index[neigh_index] += [index]

    # Count the neighbors and then apply the rules
    switch = []
    for index, color in enumerate(tile_states):         # For every tile
        neigh_sum = 0                                       # The number of black neighbors
        for neigh_index in tile_neigh_index[index]:         # For every neighbors' index
            neigh_sum += tile_states[neigh_index]               # If it's black, count it as such
            if neigh_sum > 2:                                   # It doesn't matter if it has more than 2 black neighbor
                break
        if color == 1 and neigh_sum not in [1, 2]:          # Rule to turn from black to white
            switch += [index]
        elif color == 0 and neigh_sum == 2:                 # Rule to turn from white to black
            switch += [index]

    # Switch the tagged tiles
    for index in switch:
        tile_states[index] = (tile_states[index] + 1) % 2


# Get the number os black tiles
num_black_tiles = sum(tile_states)

# Show the result
print(num_black_tiles)
