# Puzzle Input
with open('Day13_Input.txt') as puzzle_input:
    bus_info = puzzle_input.read().split('\n')

# Get the departure time and the IDs
departure = int(bus_info[0])
bus_id = bus_info[1].split(',')

# Remove the x's
while 'x' in bus_id:
    bus_id.remove('x')

# Convert the IDs to integers
bus_id = list(map(int, bus_id))

# Calculate the waiting times
waiting_times = []
for ID in bus_id:                                   # The negative part is the time the bus departs before we can leave
    waiting_times += [-(departure % ID) + ID]       # the positive part changes it to after we left

# See which bus gave us the minimum waiting time
min_index = waiting_times.index(min(waiting_times))

# Show the result
print(waiting_times[min_index] * bus_id[min_index])
