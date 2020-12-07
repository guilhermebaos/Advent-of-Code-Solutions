# Puzzle Input
with open('Day07_Input.txt') as puzzle_input:
    bag_rules = puzzle_input.read().split('.\n')

# Analise each rule
bag_parents = []
bag_children = []
for index, rule in enumerate(bag_rules):
    parsed = rule.split(' ')

    # Parent Bag
    bag_parents += [parsed[0] + parsed[1]]
    bag_children += [[]]

    # Get the Child Bags inside the Parent Bag
    if len(parsed) != 7:
        for start in range(4, len(parsed), 4):
            bag_children[-1] += [[int(parsed[start]), parsed[start + 1] + parsed[start + 2]]]


# Explore the Bag Tree
bags_to_explore = ['shinygold']         # Bags to find inside other Bags
nums_to_explore = [1]                   # List of the amount of each bag we have
required_bags = 0                       # Number of bags required inside my Bag
while len(bags_to_explore) != 0:        # While we have bags to explore
    # Lists of bags to explore later
    bags_to_add = []
    nums_to_add = []

    # Search every child of the parents in bags_to_explore
    for parent_pos, parent_bag in enumerate(bags_to_explore):
        index = bag_parents.index(parent_bag)                           # Find the index of the parent
        for child in bag_children[index]:                               # Add every child of that parent
            # Add to the required_bags the number of child bags this parent bag contains times the number of parent bags
            required_bags += child[0] * nums_to_explore[parent_pos]

            bags_to_add += [child[1]]                                   # Add the child bag to the explore list
            nums_to_add += [nums_to_explore[parent_pos] * child[0]]     # The the number of times we have them

    # Add bags we found to the options available and search those bags
    bags_to_explore = bags_to_add[:]
    nums_to_explore = nums_to_add[:]

print(required_bags)
