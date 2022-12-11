# Solution for Problem 2 Day 11 of AoC 2022!

# Puzzle Input ----------
with open('Day11-Input.txt', 'r') as file:
    puzzle = file.read().split("\n\n")

with open('Day11-Test01.txt', 'r') as file:
    test01 = file.read().split("\n\n")


# Code ------------------
class Monkey:

    def __init__(self, uid: int, inv: list[int], oper=lambda x: x, test=lambda x: x, true=None, false=None):
        self.uid = uid
        self.inv = inv
        self.oper = oper
        self.test = test
        self.true = true
        self.false = false
        self.inspetions = 0
        self.worry_control = 1

    def __str__(self):
        return f"Monkey {self.uid}: {self.inv}"

    # Define the operation the monkey will use while inspecting an item
    def build_oper(self, operation, o2):
        if operation == "*":
            self.oper = lambda x: x * (x if o2 == "old" else int(o2))
        else:
            self.oper = lambda x: x + (x if o2 == "old" else int(o2))

    # Test an item's worry level
    def build_test(self, num):
        self.test = lambda x: (x % num) == 0

    # Execute a monkey's turn
    def turn(self):
        for _ in range(len(self.inv)):
            self.inspetions += 1

            item = self.inv[0]
            item = self.oper(item) % self.worry_control
            if self.test(item):
                self.true.inv += [item]
            else:
                self.false.inv += [item]

            self.inv.pop(0)


def solution_day11_prob2(puzzle_in: list):
    # Separate input by lines and then by spaces
    monkey_data = list(map(lambda z: list(map(lambda y: y.replace(",", "").split(" "), z.split("\n"))), puzzle_in))
    monkeys = [Monkey(uid, list(map(int, m[1][4:]))) for uid, m in enumerate(monkey_data)]

    # Build monkey operations and tests
    mcm = 1
    for index, m_data in enumerate(monkey_data):
        m = monkeys[index]

        o1, operation, o2 = m_data[2][5:]
        m.build_oper(operation, o2)

        test_num = int(m_data[3][-1])
        mcm *= test_num
        m.build_test(test_num)
        m.true = monkeys[int(m_data[4][-1])]
        m.false = monkeys[int(m_data[5][-1])]

    # Keep worry levels under control
    # This will preserve divisibility by all test numbers
    for m in monkeys:
        m.worry_control = mcm

    # Simulate 10k rounds
    for x in range(10000):
        for m in monkeys:
            m.turn()

    # Get the most active monkeys
    activity = [m.inspetions for m in monkeys]
    activity.sort(reverse=True)

    return activity[0] * activity[1]


# Tests and Solution ---
print("Tests:")
print(solution_day11_prob2(test01))
print("\nSolution:")
print(solution_day11_prob2(puzzle))
