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

# Get the number os black tiles
num_black_tiles = len(black_tiles)

# Show the result
print(num_black_tiles)
