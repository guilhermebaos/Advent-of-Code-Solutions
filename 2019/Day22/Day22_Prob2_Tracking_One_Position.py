deck_len = 119315717514047
shuffle_times = 101741582076661


def deal_into_new_stack(pos):
    return deck_len - pos - 1


def cut(pos, n):
    if n > 0:
        if deck_len - pos < n:
            pos -= deck_len - n
        else:
            pos += n
    else:
        if pos < abs(n):
            pos += deck_len - abs(n)
        else:
            pos -= abs(n)
    return pos


def deal_with_increment(pos, n):
    x = 0
    while True:
        new_pos = (pos + x * deck_len) / n
        if new_pos.is_integer():
            return int(new_pos)
        else:
            x += 1


real_string = '''cut 9374
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
string = real_string
string = string.split('\n')
string.reverse()

position = 2020

for time in range(0, shuffle_times):
    for item in string:
        command = item.split()
        if command[0] == 'cut':
            position = cut(position, int(command[-1]))
        else:
            if command[1] == 'into':
                position = deal_into_new_stack(position)
            else:
                position = deal_with_increment(position, int(command[-1]))
        if position >= deck_len:
            position -= deck_len * (position // deck_len)
        elif position < 0:
            position += deck_len * (position // deck_len)

    print(position)
    input('')
