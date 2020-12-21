import re

# Puzzle Input
with open('Day21_Input.txt') as puzzle_input:
    foods = puzzle_input.read().split('\n')


# Separate every element in the foods list
def map_foods(el):
    el = re.split(r'[ (,)]', el)                # Split it by all element that don't carry information
    for _ in range(el.count('')):               # Remove empty elements
        el.remove('')
    separator = el.index('contains')            # Use the separator to distinguish between ingredients and allergenics
    el = [set(el[:separator]), set(el[separator + 1:])]
    return el


# Remove paired ingredient-allergy from foods list, or just one of them if they're not paired
def remove_from_foods(ingredient_to_remove, allergy_to_remove):
    global foods, pairs
    pairs += [[ingredient_to_remove, allergy_to_remove]]
    for food_index, food_list in enumerate(foods):      # For every food and allergenic:
        food_list[0].discard(ingredient_to_remove)          # Discard the food from every ingredient list
        food_list[1].discard(allergy_to_remove)             # Discard the allergenic from every allergenic list
        foods[food_index] = food_list                       # Update the main list


# Parse the foods list
foods = list(map(map_foods, foods))

# Pairs of ingredient-allergy
pairs = []

# See how many times each ingredient appears in a food which has a certain allergenic
food_allergen_count = dict()
for food in foods:
    # Get the ingredients and the allergenic
    ingredients = food[0]
    allergens = food[1]

    # If they're not in the dict, add the allergens to it
    for allergy in allergens:
        if allergy not in food_allergen_count.keys():
            food_allergen_count[allergy] = dict()

    # Either add the ingredient to the sub-dict corresponding to an allergenic or add 1 to its value
    for ingr in ingredients:
        for allergy in allergens:
            if ingr not in food_allergen_count[allergy].keys():
                food_allergen_count[allergy][ingr] = 1
            else:
                food_allergen_count[allergy][ingr] += 1

# Get the allergens
allergens = list(food_allergen_count.keys())

# Sort them for later
sorted_allergens = allergens[:]
sorted_allergens.sort()

# See which ingredients appear the most for each allergen
max_ingredients = []
for allergy in allergens:
    ingr_list = food_allergen_count[allergy]        # The allergenic list we're considering
    max_ingredients += [[]]                         # Add a sub-list to the max ingredients
    ingredients = ingr_list.values()                # Get the ingredient names
    max_count_value = max(ingredients)              # Get the value of the ingredients that appear the most
    for ingr in ingr_list.keys():                   # For every ingredient that is connected to a certain allergenic:
        if ingr_list[ingr] == max_count_value:          # If that ingredient is one of those that appears the most:
            max_ingredients[-1] += [ingr]                   # Add it to the list on the position that corresponds
                                                            # to the allergenic
# Get the ingredient-allergy pairs
while len(max_ingredients) > 0:                     # As long as there are ingredients in the list
    # Items to be removed later, we can't remove them in the middle of the loop because then we jump elements
    to_remove_ingr = []
    to_remove_list = []

    # Start by pairing the allergenics which only have one possible food that contains them
    for max_index, ingr_list in enumerate(max_ingredients):
        if len(ingr_list) == 1:
            remove_from_foods(ingr_list[0], allergens[max_index])   # Remove food and allergenic from the foods list
            to_remove_ingr += [ingr_list[0]]
            to_remove_list += [ingr_list]

    # Remove the allergenic and the possible matches for that allergenic, which is only 1, from the lists
    for remove_list in to_remove_list:
        remove_index = max_ingredients.index(remove_list)
        max_ingredients.pop(remove_index)
        allergens.pop(remove_index)

    # Remove the matched ingredient from the other allergenic lists, because each ingredient contains 1 or 0  allergenic
    for remove_ingr in to_remove_ingr:
        for max_index, ingr_list in enumerate(max_ingredients):
            if remove_ingr in ingr_list:
                ingr_list.remove(remove_ingr)
                max_ingredients[max_index] = ingr_list


# Order the ingredients alphabetically by the allergenic
ordered_ingredient = []
ordered_index = 0
while len(pairs) != len(ordered_ingredient):
    for ingredient, allergenic in pairs:
        if allergenic == sorted_allergens[ordered_index]:   # If the allergenic is the next in the list:
            ordered_ingredient += [ingredient]                  # Add the ingredient to the next position
            ordered_index += 1                                  # Add one to the index
            break

# Get the canonical dangerous ingredient list
ordered_ingredient = ','.join(ordered_ingredient)

# Show the result
print(ordered_ingredient)
