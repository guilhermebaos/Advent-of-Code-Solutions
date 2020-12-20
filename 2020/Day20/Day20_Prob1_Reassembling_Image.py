# Puzzle Input
with open('Day20_Input.txt') as puzzle_input:
    tiles = puzzle_input.read().split('\n\n')

# Parse the tiles: Separate the ID and get the 4 sides:
parsed_tiles = []
tiles_IDs = []
for original_tile in tiles:                     # For every tile:
    original_tile = original_tile.split('\n')       # Split the original tile into rows
    tiles_IDs += [int(original_tile[0][5:-1])]      # Get the ID of the tile -> Tile: XXXX, XXXX starts at index 5

    parsed_tiles += [[]]                            # Next parsed tile
    left_side = ''
    right_side = ''
    for row in original_tile[1:]:                   # The left and right sides are the:
        left_side += row[0]                             # Beginning of rows
        right_side += row[-1]                           # End of rows
    parsed_tiles[-1] += original_tile[1][:], right_side[:], original_tile[-1][:], left_side[:]

# Make connections between the tiles
connections = [[] for _ in range(len(tiles_IDs))]               # Create an empty list of connections
for tile_index, tile in enumerate(parsed_tiles):                # For every tile:
    tile_id = tiles_IDs[tile_index]                                 # Get it's ID
    for other_tile_index, other_tile in enumerate(parsed_tiles):    # Try to match it to every other tile
        if other_tile_index == tile_index:                              # If they're the same tile, go to the next
            continue
        other_tile_id = tiles_IDs[other_tile_index]                     # Get the other tile's ID
        if other_tile_id in connections[tile_index]:                    # The other tile has the connection, skip this
            continue
        for other_side in other_tile:                                   # For every side in the other tile
            if other_side in tile or other_side[::-1] in tile:              # See if either the side currently matches
                connections[tile_index] += [other_tile_id]                  # or if a rotated tile would match this tile
                connections[other_tile_index] += [tile_id]                  # then, add the connections

# Get the product of the corners (the tiles that only have 2 connections)
total = 1
for ID, conn in zip(tiles_IDs, connections):
    if len(conn) == 2:
        total *= ID

# Show the result
print(total)
