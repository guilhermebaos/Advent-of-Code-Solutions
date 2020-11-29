input_to_clean = '''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''.replace(',', '')

first_list = input_to_clean.split('\n')

list_reaction = []
list_numbers = []

second_list = [x.split() for x in first_list]

print(second_list)

for item1 in second_list:
    to_be_list_numbers, to_be_list_reaction = [], []
    for item2 in item1:
        if item2.isdigit():
            to_be_list_numbers += [int(item2)]
        elif item2 != '=>':
            to_be_list_reaction += [str(item2)]
    list_numbers += [to_be_list_numbers[:]]
    list_reaction += [to_be_list_reaction[:]]

print(list_numbers)
print(list_reaction)
