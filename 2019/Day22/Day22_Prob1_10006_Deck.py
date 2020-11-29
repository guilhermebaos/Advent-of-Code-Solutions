def unique_list(lst):
    to_eliminate = []
    for c, item in enumerate(lst):
        if lst.index(item) != c:
            to_eliminate += [c]
    to_eliminate.sort(reverse=True)
    for c in to_eliminate:
        lst.pop(c)
    return lst


def deal_into_new_stack(deck):
    new_deck = []
    for item in deck:
        new_deck.insert(0, item)
    return new_deck


def cut(deck, n):
    new_deck = []
    if n < 0:
        new_deck += deck[len(deck)+n:]
        new_deck += deck[:n]
    else:
        new_deck += deck[n:]
        new_deck += deck[:n]
    return new_deck


def deal_with_increment(deck, n):
    new_deck = []
    pos = 0
    take_from = 0
    for time in range(0, len(deck)):
        new_deck += [0]
    for time in range(0, len(deck)):
        if pos > len(new_deck)-1:
            pos -= len(new_deck)
        new_deck[pos] = deck[take_from]
        pos += n
        take_from += 1
    return new_deck


deck_10 = []
for c in range(0, 10007):
    deck_10 += [c]

string = '''cut 9374
deal with increment 48
cut -2354
deal with increment 12
cut -7039
deal with increment 14
cut -2325
deal with increment 40
deal into new stack
cut 4219
deal with increment 15
cut -3393
deal with increment 48
cut 1221
deal with increment 66
cut 1336
deal with increment 53
deal into new stack
cut -5008
deal into new stack
deal with increment 34
cut 8509
deal with increment 24
cut -1292
deal into new stack
cut 8404
deal with increment 17
cut -105
deal with increment 51
cut 2974
deal with increment 5
deal into new stack
deal with increment 53
cut 155
deal with increment 31
cut 2831
deal with increment 61
cut -4193
deal into new stack
cut 9942
deal with increment 13
cut -532
deal with increment 41
cut 2847
deal into new stack
cut -2609
deal with increment 72
cut 9098
deal with increment 64
deal into new stack
cut 4292
deal into new stack
cut -4427
deal with increment 24
cut -4713
deal into new stack
cut 5898
deal with increment 56
cut -2515
deal with increment 2
cut -5502
deal with increment 66
cut 8414
deal with increment 7
deal into new stack
deal with increment 35
deal into new stack
deal with increment 29
cut -2176
deal with increment 14
cut 7773
deal with increment 36
cut 2903
deal into new stack
deal with increment 75
cut 239
deal with increment 45
cut 5450
deal with increment 10
cut 6661
deal with increment 64
cut -6842
deal with increment 40
deal into new stack
deal with increment 31
deal into new stack
deal with increment 46
cut 6462
deal into new stack
cut -8752
deal with increment 28
deal into new stack
deal with increment 43
deal into new stack
deal with increment 54
cut 9645
deal with increment 44
cut 5342
deal with increment 66
cut 3785'''

string = string.split('\n')

for item in string:
    command = item.split()
    if command[0] == 'cut':
        deck_10 = cut(deck_10, int(command[-1]))
    else:
        if command[1] == 'into':
            deck_10 = deal_into_new_stack(deck_10)
        else:
            deck_10 = deal_with_increment(deck_10, int(command[-1]))

print(deck_10.index(2019))