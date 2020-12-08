# Puzzle Input
with open('Day07_Input.txt') as puzzle_input:
    bag_rules = puzzle_input.read().split('.\n')

# Analise each rule
for index, rule in enumerate(bag_rules):
    parsed = rule.split(' ')

    # Parent Bag
    bag_rules[index] = [parsed[0] + parsed[1]]

    # Get the Child Bags inside the Parent Bag
    if len(parsed) != 7:
        for start in range(4, len(parsed), 4):
            bag_rules[index] += [[int(parsed[start]), parsed[start + 1] + parsed[start + 2]]]

# Explore the Bag Tree
bags_to_explore = {'shinygold'}         # Bags to find inside other Bags
options_available = set()               # Where can we put our Shiny Gold Bag
while len(bags_to_explore) != 0:        # While we have bags to explore
    bags_to_add = set()                 # Temporary set of other bags to explore later, and to add as options available
    for rule in bag_rules:              # Explore each rule (Bag connections)
        for child in rule[1:]:          # See the contents of each Bag
            if child[1] in bags_to_explore:      # Find if the contents are what we are looking for
                bags_to_add.update({rule[0]})

    # Add bags we found to the options available and search those bags
    options_available.update(bags_to_add)
    bags_to_explore = bags_to_add

print(len(options_available))
