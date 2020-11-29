from IntCode import intcode_day7
from time import sleep

memory_puzzle = [3, 8, 1001, 8, 10, 8, 105, 1, 0, 0, 21, 34, 47, 72, 93, 110, 191, 272, 353, 434, 99999, 3, 9, 102, 3, 9, 9, 1001, 9, 3, 9, 4, 9, 99, 3, 9, 102, 4, 9, 9, 1001, 9, 4, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 1002, 9, 3, 9, 1001, 9, 2, 9, 1002, 9, 2, 9, 101, 4, 9, 9, 4, 9, 99, 3, 9, 1002, 9, 3, 9, 101, 5, 9, 9, 102, 4, 9, 9, 1001, 9, 4, 9, 4, 9, 99, 3, 9, 101, 3, 9, 9, 102, 4, 9, 9, 1001, 9, 3, 9, 4, 9, 99, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 99, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 99, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 101, 2, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 2, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 102, 2, 9, 9, 4, 9, 3, 9, 1001, 9, 1, 9, 4, 9, 3, 9, 101, 1, 9, 9, 4, 9, 3, 9, 1002, 9, 2, 9, 4, 9, 99]

# Expected 139629729
test1 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]

# Expected 18216
test2 = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54, -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4, 53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

memory = memory_puzzle[:]

# All combinations of Phases
outputs = []
condition = True
for c1 in range(0, 5):
    phases_1 = [5, 6, 7, 8, 9]
    p1 = phases_1[c1]
    phases_1.pop(c1)
    for c2 in range(0, 4):
        phases_2 = phases_1[:]
        p2 = phases_2[c2]
        phases_2.pop(c2)
        for c3 in range(0, 3):
            phases_3 = phases_2[:]
            p3 = phases_3[c3]
            phases_3.pop(c3)
            for c4 in range(0, 2):
                phases_4 = phases_3[:]
                p4 = phases_4[c4]
                phases_4.pop(c4)
                for c5 in range(0, 1):
                    phases_5 = phases_4[:]
                    p5 = phases_5[c5]
                    phases_5.pop(c5)

                    # Inicial value for the Amplifiers
                    outputE = 0
                    MemA, MemB, MemC, MemD, MemE = memory[:], memory[:], memory[:], memory[:], memory[:]
                    com_posA = com_posB = com_posC = com_posD = com_posE = 0
                    condition = True

                    # First run (giving the Amplifiers their phases)
                    MemA, outputA, _, com_posA = intcode_day7(MemA, com_posA, p1, outputE)
                    MemB, outputB, _, com_posB = intcode_day7(MemB, com_posB, p2, outputA)
                    MemC, outputC, _, com_posC = intcode_day7(MemC, com_posC, p3, outputB)
                    MemD, outputD, _, com_posD = intcode_day7(MemD, com_posD, p4, outputC)
                    MemE, outputE, _, com_posE = intcode_day7(MemE, com_posE, p5, outputD)

                    # Rerunning giving them only their inputs (previous Amp'2 output)
                    while condition:
                        MemA, outputA, _, com_posA = intcode_day7(MemA, com_posA, outputE)
                        MemB, outputB, _, com_posB = intcode_day7(MemB, com_posB, outputA)
                        MemC, outputC, _, com_posC = intcode_day7(MemC, com_posC, outputB)
                        MemD, outputD, _, com_posD = intcode_day7(MemD, com_posD, outputC)
                        MemE, outputE, condition, com_posE = intcode_day7(MemE, com_posE, outputD)
                    outputs += [outputE]

print(max(outputs))
