# Check if there are two adjacent digits that are the same
def adjacent_in_list(li=()):
    for c in range(0, len(li)-1):
        if li[c] == li[c+1]:
            return True
    return False


# Check if the list doesn't get smaller as the index increases
def list_gets_bigger(li=()):
    for c in range(0, len(li)-1):
        if li[c] > li[c+1]:
            return False
    else:
        return True


def password_criteria(n, mini, maxi):
    n_list = []
    n = str(n)
    for c in range(0, len(n)):
        n_list += [int(n[c])]
    if int(n) > maxi or int(n) < mini:      # Check if the number is in the range
        return False
    elif not adjacent_in_list(n_list):
        return False
    elif list_gets_bigger(n_list):
        return True


passwords = []
for c0 in range(146810, 612564):
    if password_criteria(c0, 146810, 612564):
        passwords += [c0]

print(len(passwords), passwords)
