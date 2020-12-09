from IntCode import intcode

memory = [109, 424, 203, 1, 21102, 11, 1, 0, 1105, 1, 282, 21102, 18, 1, 0, 1105, 1, 259, 1201, 1, 0, 221, 203, 1,
          21101, 31, 0, 0, 1105, 1, 282, 21101, 38, 0, 0, 1106, 0, 259, 21002, 23, 1, 2, 22101, 0, 1, 3, 21102, 1, 1, 1,
          21101, 0, 57, 0, 1105, 1, 303, 1201, 1, 0, 222, 20102, 1, 221, 3, 21001, 221, 0, 2, 21101, 259, 0, 1, 21101,
          0, 80, 0, 1105, 1, 225, 21102, 1, 76, 2, 21101, 91, 0, 0, 1106, 0, 303, 1201, 1, 0, 223, 21001, 222, 0, 4,
          21102, 1, 259, 3, 21101, 0, 225, 2, 21102, 1, 225, 1, 21102, 1, 118, 0, 1106, 0, 225, 20101, 0, 222, 3, 21101,
          100, 0, 2, 21102, 1, 133, 0, 1105, 1, 303, 21202, 1, -1, 1, 22001, 223, 1, 1, 21101, 148, 0, 0, 1105, 1, 259,
          2102, 1, 1, 223, 20102, 1, 221, 4, 21001, 222, 0, 3, 21101, 0, 17, 2, 1001, 132, -2, 224, 1002, 224, 2, 224,
          1001, 224, 3, 224, 1002, 132, -1, 132, 1, 224, 132, 224, 21001, 224, 1, 1, 21101, 0, 195, 0, 106, 0, 109,
          20207, 1, 223, 2, 21002, 23, 1, 1, 21102, 1, -1, 3, 21101, 214, 0, 0, 1105, 1, 303, 22101, 1, 1, 1, 204, 1,
          99, 0, 0, 0, 0, 109, 5, 1201, -4, 0, 249, 22101, 0, -3, 1, 21201, -2, 0, 2, 22102, 1, -1, 3, 21101, 0, 250, 0,
          1106, 0, 225, 22101, 0, 1, -4, 109, -5, 2105, 1, 0, 109, 3, 22107, 0, -2, -1, 21202, -1, 2, -1, 21201, -1, -1,
          -1, 22202, -1, -2, -2, 109, -3, 2105, 1, 0, 109, 3, 21207, -2, 0, -1, 1206, -1, 294, 104, 0, 99, 22101, 0, -2,
          -2, 109, -3, 2105, 1, 0, 109, 5, 22207, -3, -4, -1, 1206, -1, 346, 22201, -4, -3, -4, 21202, -3, -1, -1,
          22201, -4, -1, 2, 21202, 2, -1, -1, 22201, -4, -1, 1, 22101, 0, -2, 3, 21102, 1, 343, 0, 1105, 1, 303, 1106,
          0, 415, 22207, -2, -3, -1, 1206, -1, 387, 22201, -3, -2, -3, 21202, -2, -1, -1, 22201, -3, -1, 3, 21202, 3,
          -1, -1, 22201, -3, -1, 2, 21201, -4, 0, 1, 21102, 1, 384, 0, 1106, 0, 303, 1105, 1, 415, 21202, -4, -1, -4,
          22201, -4, -3, -4, 22202, -3, -2, -2, 22202, -2, -4, -4, 22202, -3, -2, -3, 21202, -4, -1, -2, 22201, -3, -2,
          1, 21201, 1, 0, -4, 109, -5, 2106, 0, 0]

outputs = []
for x in range(0, 50):
    for y in range(0, 50):
        _, one_output = intcode(memory, inputs=[x, y], output_vars=False, prints=False)
        outputs += one_output

print(outputs)
print(outputs.count(1))