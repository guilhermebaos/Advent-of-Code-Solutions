# Puzzle Input
with open('Day19_Input.txt') as puzzle_input:
    rules, messages = puzzle_input.read().split('\n\n')

# Split rules and messages
rules = rules.split('\n')
messages = messages.split('\n')

# Parse rules
parsed_rules = [[] for _ in range(len(rules))]              # Empty list to put the new rules in
for single_rule in rules:                                   # For every rule:
    if '"' in single_rule:                                      # Remove " if it has them
        single_rule = single_rule.replace('"', '', 2)
    single_rule = single_rule.split(' ')
    parsed_rules[int(single_rule[0][:-1])] = single_rule[1:]    # Put it in the right index


# Update Rules:
parsed_rules[8] = ['42', '|', '42', '8']
parsed_rules[11] = ['42', '31', '|', '42', '11', '31']


# Parse messages
messages = list(map(list, messages))


# Function to analise if expression matches rules
def match(rule_index, message_index):
    rule = parsed_rules[rule_index]                     # Get the rule from the global variable
    if rule_index == 8:                                 # Rule 8: Repeat rule 42 until one of two things happens:
        original_message = messages[message_index][:]
        if match(42, message_index):
            while True:
                original_message = messages[message_index][:]
                if match(11, message_index):                # Case 1: We see tha the rest of the message matches rule 11
                    messages[message_index] = original_message  # (Because Rule 0 is 8 11), returning True
                    return True
                if not match(42, message_index):            # Case 2: Rule 42 doesn't match anymore, returning False
                    messages[message_index] = original_message
                    break
            return True
        messages[message_index] = original_message          # Revert back to the original
        return False
    elif rule_index == 11:                              # Rule 11: Repeat rule 42 K times and then 31 K times
        original_message = messages[message_index][:]
        if match(42, message_index):
            matches42 = 1                               # Value of K
            while True:                                 # Repeat 42 until it is no longer possible
                temp_original_message = messages[message_index][:]          # Backup of the message to pass to rule 31
                if not match(42, message_index):
                    messages[message_index] = temp_original_message          # Revert back to the original
                    break
                matches42 += 1
            for _ in range(matches42):                  # Repeat rule 31 k times
                if not match(31, message_index):
                    messages[message_index] = original_message          # Revert back to the original
                    return False
            return True
        messages[message_index] = original_message          # Revert back to the original
        return False
    elif '|' in rule:                                   # If it has an OR operator:
        original_message = messages[message_index][:]       # Backup the original message
        if rule.index('|') == 1:                            # If it's RULE | RULE: it only has to match one of the rules
            if match(int(rule[0]), message_index):
                return True
            messages[message_index] = original_message      # Revert back to the original to test with the next rule
            if match(int(rule[2]), message_index):
                return True
        else:                                               # It's RULE RULE | RULE RULE: has to match one of the pairs
            if match(int(rule[0]), message_index) and match(int(rule[1]), message_index):
                return True
            messages[message_index] = original_message      # Revert back to the original to test with the next rule
            if match(int(rule[3]), message_index) and match(int(rule[4]), message_index):
                return True
        messages[message_index] = original_message
        return False
    elif rule[0].isnumeric():                               # If it's and AND of many rules:
        for sub_rule in rule:                                   # Has to match every rule, otherwise
            original_message = messages[message_index][:]
            if not match(int(sub_rule), message_index):
                messages[message_index] = original_message      # Revert back to the original to test with the next rule
                return False
        return True
    else:                                                   # If it is a single character, try to remove it
        char = rule[0]
        if len(messages[message_index]) == 0:                   # If the message is empty, it fails
            return False
        if messages[message_index][0] == char:                  # If the message starts with the character, remove it
            messages[message_index].pop(0)
            return True
        else:                                                   # Otherwise, it fails
            return False


# Get the total number os matching messages
total = 0
for index in range(len(messages)):                          # Test all messages
    is_a_match = match(0, index)                            # Allows to print this result
    total += is_a_match and len(messages[index]) == 0

# Show the result
print(total)
