# Puzzle Input
with open('Day08_Input.txt') as puzzle_input:
    boot_code = puzzle_input.read().split('\n')

for pos, line in enumerate(boot_code):
    boot_code[pos] = line.split(' ')


# Run the code
def run_boot_code(code):
    index = 0
    accumulator = 0
    finish_index = len(code)
    executed = []
    while index not in executed:        # Detects that another command will be executed a second time
        executed += [index]
        cmd = code[index][0]            # Command
        arg = int(code[index][1])       # Argument
        if cmd == 'acc':                # acc function
            index += 1
            accumulator += arg
        elif cmd == 'jmp':              # jmp function
            index += arg
        elif cmd == 'nop':              # nop function
            index += 1
        if index == finish_index:       # Finish the boot sequence
            print('Finished!')
            print(accumulator)
            return True
    return False


# Try changing all the jmp to nop and vice-versa
for pos, line in enumerate(boot_code):
    if line[0] == 'nop':
        boot_code[pos][0] = 'jmp'
        if not run_boot_code(boot_code):    # Cancel the change
            boot_code[pos][0] = 'nop'
        else:
            break
    elif line[0] == 'jmp':
        boot_code[pos][0] = 'nop'
        if not run_boot_code(boot_code):    # Cancel the change
            boot_code[pos][0] = 'jmp'
        else:
            break
