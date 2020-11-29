# Check if there is at least one consecutive pais of equal digits
def adjacent_in_list(li=()):
    for c in range(0, len(li)-1):
        if li[c] == li[c+1]:
            if c == 0:
                if li[c] != li[c+2]:
                    return True
            elif c+1 == len(li)-1:
                if li[c] != li[c-1]:
                    return True
            else:
                if li[c] != li[c+2] and li[c] != li[c-1]:
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
    if int(n) > maxi or int(n) < mini:
        return False
    elif max(n_list) != n_list[-1]:
        return False
    elif not adjacent_in_list(n_list):
        return False
    elif list_gets_bigger(n_list):
        return True


passwords = []
pass_mini = 146810
pass_maxi = 612564
for c0 in range(pass_mini, pass_maxi):
    if password_criteria(c0, pass_mini, pass_maxi):
        passwords += [c0]

print(len(passwords), passwords)
