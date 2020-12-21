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
    global foods
    for food_index, food_list in enumerate(foods):      # For every food and allergenic:
        food_list[0].discard(ingredient_to_remove)          # Discard the food from every ingredient list
        food_list[1].discard(allergy_to_remove)             # Discard the allergenic from every allergenic list
        foods[food_index] = food_list                       # Update the main list


# Parse the foods list
foods = list(map(map_foods, foods))

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
allergens = food_allergen_count.keys()

# See which ingredients appear the most for each allergenic
max_ingredients = []
for allergy in allergens:                       # For every allergenic:
    ingr_list = food_allergen_count[allergy]        # The allergenic list we're considering
    ingredients = ingr_list.values()                # Get the ingredient names
    max_count_value = max(ingredients)              # Get the value of the ingredients that appear the most
    for ingr in ingr_list.keys():
        if ingr_list[ingr] == max_count_value:      # If this ingredient if one of those that appears the most,
            max_ingredients += [ingr]               # add it to this list

# Remove all ingredients that might contain an allergen
for ingr in max_ingredients:
    remove_from_foods(ingr, '')

# Get the total number of allergy free foods
total = 0
for clean_food in foods:
    total += len(list(clean_food[0]))

# Show the result
print(total)
