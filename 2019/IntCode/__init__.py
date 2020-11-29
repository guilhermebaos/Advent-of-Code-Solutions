def intcode(memory=(), inputs=(), com_pos=0, rel_bas=0, output_vars=False, prints=True):
    param1 = param2 = param3 = stored = 999999

    # com_pos Command Position
    # rel_bas Relative base for relative position parameters

    outputs = []

    inputs = list(inputs)
    memory = list(memory)
    if len(memory) < 10000:
        memory += [0] * 10000
    while True:
        # What is the command
        instruction = str(memory[com_pos])

        # Identify the Opcode and its increase value
        opcode = int(instruction[-2:])
        if opcode == 99:
            opcode_len = 1
        elif opcode == 3 or opcode == 4 or opcode == 9:
            opcode_len = 2
        elif opcode == 5 or opcode == 6:
            opcode_len = 3
        else:
            opcode_len = 4

        # Identify the parameters modes for the Opcodes' parameters
        parameters = str(instruction[:-2])
        if len(parameters) < opcode_len:
            parameters = parameters.rjust(opcode_len, '0')
        if len(parameters) < 3:
            parameters = parameters.rjust(3, '0')

        # Identify the parameters that are going to be used by the Opcodes
        try:
            if opcode != 99:
                if parameters[-1] == '0':                               # 0-> Position Mode (Stores the address of the parameter)
                    param1 = memory[memory[com_pos + 1]]
                    stored = memory[com_pos + 1]
                elif parameters[-1] == '1':                             # 1-> Absolute Mode (Stores the value of the parameter)
                    param1 = memory[com_pos + 1]
                    stored = com_pos + 1
                elif parameters[-1] == '2':                             # 2-> Relative Mode (Stores the address relative to the base)
                    param1 = memory[memory[com_pos + 1] + rel_bas]
                    stored = memory[com_pos + 1] + rel_bas
                if opcode != 3 and opcode != 4 and opcode != 9:
                    if parameters[-2] == '0':                           # 0-> Position Mode
                        param2 = memory[memory[com_pos + 2]]
                    elif parameters[-2] == '1':                         # 1-> Absolute Mode
                        param2 = memory[com_pos + 2]
                    elif parameters[-2] == '2':
                        param2 = memory[memory[com_pos + 2] + rel_bas]
                    if opcode != 5 and opcode != 6:
                        if parameters[-3] == '0':                       # 0-> Position Mode
                            param3 = memory[com_pos + 3]
                        elif parameters[-3] == '1':                     # 1-> Absolute Mode
                            param3 = com_pos + 3
                        elif parameters[-3] == '2':
                            param3 = memory[com_pos + 3] + rel_bas
        except IndexError as error:
            print(f'ERROR: {error}, Opcode: {opcode}')

        # Execute the Opcodes
        # print('IntCode info:', 'Opcode:', opcode, 'Com_pos:', com_pos, 'Rel_bas:', rel_bas)
        if opcode == 99:                                        # Opcode 99 -> Finish the program
            break
        elif opcode == 1:                                       # Opcode 01 -> Sum two numbers and store them
            result = param1 + param2
            memory[param3] = result
            com_pos += opcode_len
        elif opcode == 2:                                       # Opcode 02 -> Multiply two numbers and store them
            result = param1 * param2
            memory[param3] = result
            com_pos += opcode_len
        elif opcode == 3:                                       # Opcode 03 -> Get user input and store it
            if len(inputs) == 0:
                result = int(input('Input value: ').strip())
                print('\n')
                memory[stored] = result
                com_pos += opcode_len
            else:
                result = inputs[0]
                memory[stored] = result
                inputs.pop(0)
                com_pos += opcode_len
        elif opcode == 4:                                       # Opcode 04 -> Print a result
            if prints:
                print('\nOutput:', param1,
                      f'  (stored in adress {stored})', '\n')
            outputs += [param1]
            com_pos += opcode_len
        elif opcode == 5:                                       # Opcode 05 -> Jump to address param2 if param1 != 0
            if param1 != 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 6:                                       # Opcode 06 -> Jump to address param2 if param1 == 0
            if param1 == 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 7:                                       # Opcode 07 -> Stores 1 if param1 < param2 else stores 0
            if param1 < param2:
                memory[param3] = 1
            else:
                memory[param3] = 0
            com_pos += opcode_len
        elif opcode == 8:                                       # Opcode 08 -> Stores 1 if param1 = param2 else stores 0
            if param1 == param2:
                memory[param3] = 1
            else:
                memory[param3] = 0
            com_pos += opcode_len
        elif opcode == 9:                                       # Opcode 09 -> Increases the relative base
            rel_bas += param1
            com_pos += opcode_len
    if output_vars:
        return memory, outputs, com_pos, rel_bas
    else:
        return memory, outputs


def intcode_day2(memory=()):
    com_pos = 0  # Command Position
    inputs = list(memory)
    while True:
        op_code = inputs[com_pos]  # What is the command
        if op_code == 99:
            break
        elif op_code == 1:
            value = inputs[inputs[com_pos + 1]] + inputs[inputs[com_pos + 2]]
            inputs[inputs[com_pos + 3]] = value
        elif op_code == 2:
            value = inputs[inputs[com_pos + 1]] * inputs[inputs[com_pos + 2]]
            inputs[inputs[com_pos + 3]] = value
        com_pos += 4
    return inputs


def intcode_day5(memory=()):
    param1 = param2 = 999999
    com_pos = 0  # Command Position
    inputs = list(memory)
    while True:
        # What is the command
        instruction = str(inputs[com_pos])

        # Identify the Opcode and its increase value
        opcode = int(instruction[-2:])
        if opcode == 99:
            param3 = 0
            opcode_len = 1
        elif opcode == 3 or opcode == 4:
            param3 = inputs[com_pos + 1]
            opcode_len = 2
        elif opcode == 5 or opcode == 6:
            param3 = 999999
            opcode_len = 3
        else:
            param3 = inputs[com_pos + 3]
            opcode_len = 4

        # Identify the parameters modes for the function parameters
        parameters = str(instruction[:-2])
        if len(parameters) < opcode_len-1:
            parameters = parameters.rjust(opcode_len-1, '0')
        if len(parameters) < 2:
            parameters = parameters.rjust(2, '0')

        # Identify the parameters that are going to be used by the Opcodes
        if opcode != 3 and opcode != 4 and opcode != 99:
            if parameters[-1] == '0':
                param1 = inputs[inputs[com_pos + 1]]
            elif parameters[-1] == '1':
                param1 = inputs[com_pos + 1]
            if parameters[-2] == '0':
                param2 = inputs[inputs[com_pos + 2]]
            elif parameters[-2] == '1':
                param2 = inputs[com_pos + 2]
        # Execute the Opcodes
        if opcode == 99:                                        # Opcode 99 -> Finish the program
            break
        elif opcode == 1:                                       # Opcode 01 -> Sum two numbers and store them
            result = param1 + param2
            inputs[param3] = result
            com_pos += opcode_len
        elif opcode == 2:                                       # Opcode 02 -> Multiply two numbers and store them
            result = param1 * param2
            inputs[param3] = result
            com_pos += opcode_len
        elif opcode == 3:                                       # Opcode 03 -> Get user input and store it
            result = int(input('Input value: ').strip())
            print('\n')
            inputs[param3] = result
            com_pos += opcode_len
        elif opcode == 4:                                       # Opcode 04 -> Print a result
            print('\nDeviation form expected value:', inputs[inputs[com_pos + 1]],
                  f'  (stored in adress {inputs[com_pos + 1]})', '\n')
            com_pos += opcode_len
        elif opcode == 5:                                       # Opcode 05 -> Jump to adress param2 if param1 != 0
            if param1 != 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 6:                                       # Opcode 06 -> Jump to adress param2 if param1 == 0
            if param1 == 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 7:                                       # Opcode 07 -> Stores 1 if param1 < param2 else stores 0
            if param1 < param2:
                inputs[param3] = 1
            else:
                inputs[param3] = 0
            com_pos += opcode_len
        elif opcode == 8:                                       # Opcode 08 -> Stores 1 if param1 = param2 else stores 0
            if param1 == param2:
                inputs[param3] = 1
            else:
                inputs[param3] = 0
            com_pos += opcode_len
    return inputs


def intcode_day7(memory=(), com_pos=0, *user_inputs):
    print(user_inputs)
    param1 = param2 = 999999
    input_num = output = 0  # Command Position
    condition = True
    inputs = list(memory)
    while True:
        # What is the command
        instruction = str(inputs[com_pos])

        # Identify the Opcode and its increase value
        opcode = int(instruction[-2:])
        if opcode == 99:
            param3 = 0
            opcode_len = 1
        elif opcode == 3 or opcode == 4:
            param3 = inputs[com_pos + 1]
            opcode_len = 2
        elif opcode == 5 or opcode == 6:
            param3 = 999999
            opcode_len = 3
        else:
            param3 = inputs[com_pos + 3]
            opcode_len = 4

        # Identify the parameters modes for the function parameters
        parameters = str(instruction[:-2])
        if len(parameters) < opcode_len-1:
            parameters = parameters.rjust(opcode_len-1, '0')
        if len(parameters) < 2:
            parameters = parameters.rjust(2, '0')

        # Identify the parameters that are going to be used by the Opcodes
        if opcode != 3 and opcode != 4 and opcode != 99:
            if parameters[-1] == '0':
                param1 = inputs[inputs[com_pos + 1]]
            elif parameters[-1] == '1':
                param1 = inputs[com_pos + 1]
            if parameters[-2] == '0':
                param2 = inputs[inputs[com_pos + 2]]
            elif parameters[-2] == '1':
                param2 = inputs[com_pos + 2]
        # Execute the Opcodes
        if opcode == 99:                                        # Opcode 99 -> Finish the program
            condition = False
            break
        elif opcode == 1:                                       # Opcode 01 -> Sum two numbers and store them
            result = param1 + param2
            inputs[param3] = result
            com_pos += opcode_len
        elif opcode == 2:                                       # Opcode 02 -> Multiply two numbers and store them
            result = param1 * param2
            inputs[param3] = result
            com_pos += opcode_len
        elif opcode == 3:                                       # Opcode 03 -> Get user input and store it
            if len(user_inputs) == 0:
                result = int(input('Input value: ').strip())
                print('\n')
                inputs[param3] = result
                com_pos += opcode_len
            else:
                print(input_num)
                try:
                    result = user_inputs[input_num]
                    inputs[param3] = result
                    com_pos += opcode_len
                    input_num += 1
                except IndexError:
                    break
        elif opcode == 4:                                       # Opcode 04 -> Print a result
            print('\nOutput to next amplifier:', inputs[inputs[com_pos + 1]],
                  f'  (stored in adress {inputs[com_pos + 1]})', '\n')
            output = inputs[inputs[com_pos + 1]]
            condition = True
            com_pos += opcode_len
        elif opcode == 5:                                       # Opcode 05 -> Jump to adress param2 if param1 != 0
            if param1 != 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 6:                                       # Opcode 06 -> Jump to adress param2 if param1 == 0
            if param1 == 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 7:                                       # Opcode 07 -> Stores 1 if param1 < param2 else stores 0
            if param1 < param2:
                inputs[param3] = 1
            else:
                inputs[param3] = 0
            com_pos += opcode_len
        elif opcode == 8:                                       # Opcode 08 -> Stores 1 if param1 = param2 else stores 0
            if param1 == param2:
                inputs[param3] = 1
            else:
                inputs[param3] = 0
            com_pos += opcode_len
    return inputs, output, condition, com_pos


def intcode_day11(memory=(), inputs=(), com_pos=0, rel_bas=0):
    param1 = param2 = param3 = stored = 999999

    # com_pos Command Position
    # rel_bas Relative base for relative position parameters

    outputs = []

    will_break = False
    inputs = list(inputs)
    memory = list(memory)
    if len(memory) < 10000:
        memory += [0] * 1000
    while True:
        # What is the command
        instruction = str(memory[com_pos])

        # Identify the Opcode and its increase value
        opcode = int(instruction[-2:])
        if opcode == 99:
            opcode_len = 1
        elif opcode == 3 or opcode == 4 or opcode == 9:
            opcode_len = 2
        elif opcode == 5 or opcode == 6:
            opcode_len = 3
        else:
            opcode_len = 4

        # Identify the parameters modes for the Opcodes' parameters
        parameters = str(instruction[:-2])
        if len(parameters) < opcode_len:
            parameters = parameters.rjust(opcode_len, '0')
        if len(parameters) < 3:
            parameters = parameters.rjust(3, '0')

        # Identify the parameters that are going to be used by the Opcodes
        try:
            if opcode != 99:
                if parameters[-1] == '0':                               # 0-> Position Mode (Stores the address of the parameter)
                    param1 = memory[memory[com_pos + 1]]
                    stored = memory[com_pos + 1]
                elif parameters[-1] == '1':                             # 1-> Absolute Mode (Stores the value of the parameter)
                    param1 = memory[com_pos + 1]
                    stored = com_pos + 1
                elif parameters[-1] == '2':                             # 2-> Relative Mode (Stores the address relative to the base)
                    param1 = memory[memory[com_pos + 1] + rel_bas]
                    stored = memory[com_pos + 1] + rel_bas
                if opcode != 3 and opcode != 4 and opcode != 9:
                    if parameters[-2] == '0':                           # 0-> Position Mode
                        param2 = memory[memory[com_pos + 2]]
                    elif parameters[-2] == '1':                         # 1-> Absolute Mode
                        param2 = memory[com_pos + 2]
                    elif parameters[-2] == '2':
                        param2 = memory[memory[com_pos + 2] + rel_bas]
                    if opcode != 5 and opcode != 6:
                        if parameters[-3] == '0':                       # 0-> Position Mode
                            param3 = memory[com_pos + 3]
                        elif parameters[-3] == '1':                     # 1-> Absolute Mode
                            param3 = com_pos + 3
                        elif parameters[-3] == '2':
                            param3 = memory[com_pos + 3] + rel_bas
        except IndexError as error:
            print(f'ERROR: {error}, Opcode: {opcode}')

        # Execute the Opcodes
        # print('IntCode info:', 'Opcode:', opcode, 'Com_pos:', com_pos, 'Rel_bas:', rel_bas)
        if opcode == 99:                                        # Opcode 99 -> Finish the program
            outputs += [-1]
            break
        elif opcode == 1:                                       # Opcode 01 -> Sum two numbers and store them
            result = param1 + param2
            memory[param3] = result
            com_pos += opcode_len
        elif opcode == 2:                                       # Opcode 02 -> Multiply two numbers and store them
            result = param1 * param2
            memory[param3] = result
            com_pos += opcode_len
        elif opcode == 3:                                       # Opcode 03 -> Get user input and store it
            if will_break:
                break
            if len(inputs) == 0:
                result = int(input('Input value: ').strip())
                print('\n')
                memory[stored] = result
                com_pos += opcode_len
            else:
                result = inputs[0]
                memory[stored] = result
                inputs.pop(0)
                com_pos += opcode_len
        elif opcode == 4:                                       # Opcode 04 -> Print a result
            print('\nOutput:', param1,
                  f'  (stored in adress {stored})', '\n')
            outputs += [param1]
            com_pos += opcode_len
            if len(outputs) == 2:
                will_break = True
        elif opcode == 5:                                       # Opcode 05 -> Jump to address param2 if param1 != 0
            if param1 != 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 6:                                       # Opcode 06 -> Jump to address param2 if param1 == 0
            if param1 == 0:
                com_pos = param2
            else:
                com_pos += opcode_len
        elif opcode == 7:                                       # Opcode 07 -> Stores 1 if param1 < param2 else stores 0
            if param1 < param2:
                memory[param3] = 1
            else:
                memory[param3] = 0
            com_pos += opcode_len
        elif opcode == 8:                                       # Opcode 08 -> Stores 1 if param1 = param2 else stores 0
            if param1 == param2:
                memory[param3] = 1
            else:
                memory[param3] = 0
            com_pos += opcode_len
        elif opcode == 9:                                       # Opcode 09 -> Increases the relative base
            rel_bas += param1
            com_pos += opcode_len
    return memory, outputs, com_pos, rel_bas
