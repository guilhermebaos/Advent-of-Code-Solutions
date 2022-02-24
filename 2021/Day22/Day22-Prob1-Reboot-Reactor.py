# Puzzle Input ----------
with open('Day22-Input.txt', 'r') as file:
    puzzle = file.read().split('\n')

with open('Day22-Test01.txt', 'r') as file:
    test01 = file.read().split('\n')


# Main Code ----------

# Valid coords for one of the parallelepiped's dimensions
def is_valid_coords(coords):
    if type(coords) == tuple:
        coords = list(coords)
    if type(coords) == list:
        return coords[1] >= coords[0]
    return False


class Parallelepiped:
    def __init__(self, x_coords, y_coords, z_coords):
        self.x_coords = x_coords
        self.y_coords = y_coords
        self.z_coords = z_coords

    # Intersection of two parallelepipeds, using the @ symbol
    def __matmul__(self, other):
        coords = ([None, None], [None, None], [None, None])
        for self_coord, other_coord, result_coord in zip(self.list_of_coords(), other.list_of_coords(), coords):

            # See if the parallelepipeds intersect
            if self_coord[1] < other_coord[0] or self_coord[0] > other_coord[1]:
                return None

            # Calculate the coordinates of the intersection, which also is a parallelepiped
            result_coord[0] = max(other_coord[0], self_coord[0])
            result_coord[1] = min(other_coord[1], self_coord[1])

        # Return their intersection
        return Parallelepiped(coords[0], coords[1], coords[2])

    # Removes a another parallelepiped from this a parallelepiped
    def __sub__(self, other):
        intersection = self @ other
        if not intersection:
            return [self]

        results = []

        # Use y and z from the intersection, and x from the difference between self and intersection
        y_coords = intersection.y_coords
        z_coords = intersection.z_coords

        x_coords = [self.x_coords[0], intersection.x_coords[0] - 1]
        if is_valid_coords(x_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        x_coords = [intersection.x_coords[1] + 1, self.x_coords[1]]
        if is_valid_coords(x_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        # Use y from the intersection, x from the self and z from the difference between self and intersection
        y_coords = intersection.y_coords
        x_coords = self.x_coords

        z_coords = [self.z_coords[0], intersection.z_coords[0] - 1]
        if is_valid_coords(z_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        z_coords = [intersection.z_coords[1] + 1, self.z_coords[1]]
        if is_valid_coords(z_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        # Use z and x from the self and y from the difference between self and intersection
        x_coords = self.x_coords
        z_coords = self.z_coords

        y_coords = [self.y_coords[0], intersection.y_coords[0] - 1]
        if is_valid_coords(y_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        y_coords = [intersection.y_coords[1] + 1, self.y_coords[1]]
        if is_valid_coords(y_coords):
            results += [Parallelepiped(x_coords, y_coords, z_coords)]

        return results

    def __str__(self):
        return f'x: {self.x_coords}, y: {self.y_coords}, z: {self.z_coords}, V: {self.get_volume()}'

    def list_of_coords(self):
        return self.x_coords, self.y_coords, self.z_coords

    def get_volume(self):
        delta_x = self.x_coords[1] - self.x_coords[0] + 1
        delta_y = self.y_coords[1] - self.y_coords[0] + 1
        delta_z = self.z_coords[1] - self.z_coords[0] + 1
        return abs(delta_x * delta_y * delta_z)


# Parse the instruction
def parse_instructions(instruction: str):
    command, coordinates = instruction.split()
    x, y, z = coordinates.split(',')

    coords = []
    for item in [x, y, z]:
        coords += [list(map(int, item.split('=')[1].split('..')))]
    return command, coords


initialization_area = Parallelepiped([-50, 50], [-50, 50], [-50, 50])
def reboot_reactor(initialization_procedure: list):
    procedure = list(map(parse_instructions, initialization_procedure))

    on_zones = []
    for command in procedure:
        order, zone = command
        zone = [Parallelepiped(zone[0], zone[1], zone[2]) @ initialization_area]

        if not zone[0]:
            continue
        if order == 'on':
            for already_on in on_zones:
                for new_zone in zone[:]:
                    zone.remove(new_zone)
                    zone += new_zone - already_on
            if zone:
                on_zones += zone

        elif order == 'off':
            for already_on in on_zones[:]:
                on_zones.remove(already_on)
                on_zones += already_on - zone[0]

    total = 0
    for zone in on_zones:
        total += zone.get_volume()
    return total


# Tests and Solution ----------
print(reboot_reactor(test01))
print(reboot_reactor(puzzle))
