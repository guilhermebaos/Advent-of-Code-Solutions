# Puzzle Input
with open('Day08_Input.txt') as puzzle_input:
    boot_code = puzzle_input.read().split('\n')

for pos, line in enumerate(boot_code):
    boot_code[pos] = line.split(' ')

# Run the code
index = 0
accumulator = 0
executed = []
while index not in executed:        # Detects that another command will be executed a second time
    executed += [index]
    cmd = boot_code[index][0]       # Command
    arg = int(boot_code[index][1])  # Argument
    if cmd == 'acc':                # acc function
        index += 1
        accumulator += arg
    elif cmd == 'jmp':              # jmp function
        index += arg
    elif cmd == 'nop':              # nop function
        index += 1

print(accumulator)
