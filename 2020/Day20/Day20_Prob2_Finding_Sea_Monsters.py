from random import randint

# Puzzle Input
with open('Day20_Input.txt') as puzzle_input:
    tiles = puzzle_input.read().split('\n\n')

# Parse the tiles: Separate the ID and get the 4 sides:
parsed_tiles = []
tiles_IDs = []
for index, original_tile in enumerate(tiles):   # For every tile:
    original_tile = original_tile.split('\n')       # Split the original tile into rows
    tiles[index] = original_tile[1:]
    tiles_IDs += [int(original_tile[0][5:-1])]      # Get the ID of the tile -> Tile: XXXX, XXXX starts at index 5

    parsed_tiles += [[]]                            # Next parsed tile
    left_side = ''
    right_side = ''
    for row in original_tile[1:]:                   # The left and right sides are the:
        left_side += row[0]                             # Beginning of rows
        right_side += row[-1]                           # End of rows
    parsed_tiles[-1] += original_tile[1][:], right_side[:], original_tile[-1][:], left_side[:]

# Number of tiles on the side of the final image
square_side = int(len(tiles_IDs) ** 0.5)

# Make connections between the tiles
connections = [[] for _ in range(len(tiles_IDs))]               # Create an empty list of connections
for tile_index, tile in enumerate(parsed_tiles):                    # For every tile:
    for other_tile_index, other_tile in enumerate(parsed_tiles):        # Try to match it to every other tile
        if other_tile_index == tile_index:                              # If they're the same tile, go to the next
            continue
        if other_tile_index in connections[tile_index]:                 # The other tile has the connection, skip this
            continue
        for other_side in other_tile:                                   # For every side in the other tile
            if other_side in tile or other_side[::-1] in tile:              # See if either the side currently matches
                connections[tile_index] += [other_tile_index]               # or if a rotated tile would match this tile
                connections[other_tile_index] += [tile_index]               # then, add the connections


# Rotate the list of the sides
def rotate_sides(list_of_sides, clockwise_rotations=1):
    if clockwise_rotations == 0:
        return list_of_sides
    elif clockwise_rotations != 1:
        return rotate_sides(rotate_sides(list_of_sides, 1), clockwise_rotations - 1)
    else:
        return [list_of_sides[3][::-1], list_of_sides[0], list_of_sides[1][::-1], list_of_sides[2]]


# Rotate the entire tile (after the border has been removed)
def rotate_tile(list_tile, clockwise_rotations=1):
    if clockwise_rotations == 0:
        return list_tile
    elif clockwise_rotations != 1:
        return rotate_tile(rotate_tile(list_tile, 1), clockwise_rotations - 1)
    else:
        new_tile = [[] for _ in range(8)]                           # 8 instead of len(tile_row[0]) for efficiency
        for row_in_tile in list_tile[::-1]:
            for new_row_index in range(8):
                new_tile[new_row_index] += row_in_tile[new_row_index]
        return new_tile


# Rotate the entire image
def rotate_image(tile_image, clockwise_rotations=1):
    if clockwise_rotations == 0:
        return tile_image
    elif clockwise_rotations != 1:
        return rotate_image(rotate_image(tile_image, 1), clockwise_rotations - 1)
    else:
        new_tile = [[] for _ in range(len(tile_image[0]))]
        for image_row in tile_image[::-1]:
            for new_row_index in range(len(tile_image[0])):
                new_tile[new_row_index] += image_row[new_row_index]
        return new_tile


# Flip the list of sides horizontally
def flip_sides(list_of_sides, number_of_flips=1):
    if number_of_flips % 2 == 1:
        return [list_of_sides[2], list_of_sides[1][::-1], list_of_sides[0], list_of_sides[3][::-1]]
    else:
        return list_of_sides


# Flip the entire tile horizontally
def flip_tile(list_tile, number_of_flips=1):
    if number_of_flips % 2 == 1:
        return list_tile[::-1]
    else:
        return list_tile


# Remove borders
for tile_index, tile in enumerate(tiles):
    tiles[tile_index] = tile[1:-1]
    for row_index, row in enumerate(tiles[tile_index]):
        tiles[tile_index][row_index] = row[1:-1]


# Get the index of one of the corners, we can start with any corner, later we can rotate the whole image
for index, conn in enumerate(connections):
    if len(conn) == 2:
        start_index = index

# Find the orientation for that corner, based on one of it's connections
done = False
for conn_index in connections[start_index]:
    # Values for the corner tile
    start_borders = parsed_tiles[start_index]
    start_tile = tiles[start_index]

    # All possible orientations for the tile
    for start_flip in range(0, 2):
        start_tile = flip_tile(start_tile)
        start_borders = flip_sides(start_borders)
        for start_rotation in range(0, 4):
            start_tile = rotate_tile(start_tile, 1)
            start_borders = rotate_sides(start_borders, 1)
            border_right = start_borders[1]                         # Resulting border to be matched by the next tile

            # Value for the connection tile
            conn_tile = tiles[conn_index]
            conn_borders = parsed_tiles[conn_index]
            for conn_flip in range(0, 2):
                conn_tile = flip_tile(conn_tile)
                conn_borders = flip_sides(conn_borders)
                for conn_rotation in range(0, 4):
                    conn_tile = rotate_tile(conn_tile, 1)
                    conn_borders = rotate_sides(conn_borders, 1)
                    border_left = conn_borders[3]                   # Resulting border to match the corner's

                    # If they match, exit the loops
                    if border_left == border_right:
                        done = True
                        break
                if done:
                    break
            if done:
                break
        if done:
            break
    if done:
        break

# Store the initial value for top left tiles
parsed_tiles[start_index] = start_borders[:]
parsed_tiles[conn_index] = conn_borders[:]
tiles[start_index] = start_tile[:]
tiles[conn_index] = conn_tile[:]

# Create a list for the final image and a list with the indexes in the right positions
image = [[[] for _ in range(square_side)] for _ in range(square_side)]
image_index = [[[] for _ in range(square_side)] for _ in range(square_side)]

# Values we already know for the lists
image[0][0] = tiles[start_index]
image[0][1] = tiles[conn_index]
image_index[0][0] = start_index
image_index[0][1] = conn_index

# Tiles already on the image
on_image = [start_index, conn_index]


# Assemble the image with some recursion and randomness
def assemble_image(process_row=0):
    global image, on_image

    done = False

    # Do the first row, because it's different from the others
    if process_row == 0:
        # Get the border we have to match, the orientation for the previous tiles are already correct
        for index in range(square_side - 2):
            last_index = image_index[0][index + 1]
            border_right = parsed_tiles[last_index][1]

            # Randomize the order in which we pick wick tiles to test first, because some pieces fit in multiple spots
            # but the right place is only one of those spots
            if randint(0, 10) == 5:
                connections[last_index] = connections[last_index][::-1]

            # Try to match one of the tiles that connects to this one, by trying all orientations
            for conn_index in connections[last_index]:
                # Get the tile
                if conn_index not in on_image:
                    conn_tile = tiles[conn_index]
                    conn_borders = parsed_tiles[conn_index]

                    # Flip and rotate it
                    for conn_flip in range(0, 2):
                        conn_tile = flip_tile(conn_tile)
                        conn_borders = flip_sides(conn_borders)
                        for conn_rotation in range(0, 4):
                            conn_tile = rotate_tile(conn_tile, 1)
                            conn_borders = rotate_sides(conn_borders, 1)
                            border_left = conn_borders[3]

                            # If they match, exit the loops
                            if border_left == border_right:
                                done = True
                                break
                        if done:
                            break
                    if done:
                        # Commit the values
                        parsed_tiles[conn_index] = conn_borders[:]
                        tiles[conn_index] = conn_tile[:]
                        image[0][index + 2] = tiles[conn_index]
                        image_index[0][index + 2] = conn_index
                        on_image += [conn_index]

                        # Go to the next step
                        assemble_image(1)
                        return True

    elif process_row == square_side + 1:
        return True

    else:
        row = process_row
        last_row = image_index[row - 1]

        # If there is an empty spot in the previous row, recalculate it, by randomly searching, until it finds a full
        # output
        if [] in last_row:
            assemble_image(row - 1)
            return False

        # The same as above, but instead matching top-to-bottom instead of left-to-right
        for position in range(square_side):
            last_index = last_row[position]
            border_bottom = parsed_tiles[last_index][2]

            for conn_index in connections[last_index]:
                if conn_index not in on_image:
                    conn_tile = tiles[conn_index]
                    conn_borders = parsed_tiles[conn_index]
                    for conn_flip in range(0, 2):
                        conn_tile = flip_tile(conn_tile)
                        conn_borders = flip_sides(conn_borders)
                        for conn_rotation in range(0, 4):
                            conn_tile = rotate_tile(conn_tile, 1)
                            conn_borders = rotate_sides(conn_borders, 1)
                            border_top = conn_borders[0]

                            if border_bottom == border_top:
                                done = True
                                break
                        if done:
                            break
                    if done:
                        parsed_tiles[conn_index] = conn_borders[:]
                        tiles[conn_index] = conn_tile[:]
                        image[row][position] = tiles[conn_index]
                        image_index[row][position] = conn_index
                        on_image += [conn_index]

                        # Go to the next step
                        assemble_image(row + 1)
                        return True


# This function is super inefficient, because if a row ends up with a spot that can't be filled, it goes back to the
# previous row and uses randomness to change the order in which tiles are analysed
assemble_image()

# Join the image from the tiles
joined_image = []
for tile_row in image:
    for row_index in range(8):
        joined_image += [[]]                                            # Add a row
        for tile_index in range(square_side):
            joined_image[-1] += tile_row[tile_index][row_index]         # Add elements to that row


# Join the list-elements of a list in a map() function
def join_list(el):
    return ''.join(el)


# Find the dragons!
dragons_list = []
joined_image = list(map(join_list, joined_image))       # List of string that make up the final image

# Every possible orientation of the image
for image_flip in range(0, 4):
    image_tile = flip_tile(joined_image)
    for image_rotation in range(0, 8):
        image_tile = rotate_image(image_tile)
        image_tile = list(map(join_list, image_tile))

        # Dragons in this orientation
        dragons = 0
        for index_row, row in enumerate(image_tile):
            try:
                # Get 3 rows to match against the image on the puzzle
                top_row = image_tile[index_row - 1]
                middle_row = image_tile[index_row]
                bot_row = image_tile[index_row + 1]

                # Test if the dragon is in this three rows
                for start_index in range(len(row) - 19):
                    is_dragon = True                            # Assume it is, until ONE of the tests fails
                    for delta_index in [18]:
                        if not bot_row[start_index + delta_index] == '#':   # I search bottom first because it only
                            is_dragon = False                               # finds dragons in this orientation
                    for delta_index in [0, 5, 6, 11, 12, 17, 18, 19]:
                        if not middle_row[start_index + delta_index] == '#':
                            is_dragon = False
                    for delta_index in [1, 4, 7, 10, 13, 16]:
                        if not top_row[start_index + delta_index] == '#':
                            is_dragon = False

                    # Add to the total number of dragons
                    if is_dragon:
                        dragons += 1
            except IndexError:
                pass
        dragons_list += [dragons]

# Get the total number of # not in dragons (which are 15 # each)
joined_image = '\n'.join(image_tile)
roughness = joined_image.count('#') - max(dragons_list) * 15

# Show the result
print(roughness)
