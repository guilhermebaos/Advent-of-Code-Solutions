signal = '59709275180991144553584971145772909665510077889137728108418335914621187722143499835763391833539113913245874471724316543318206687063884235599476032241946131415288903315838365933464260961288979081653450180693829228376307468452214424448363604272171578101049695177870848804768766855959460302410160410252817677019061157656381257631671141130695064999297225192441065878259341014746742840736304437968599872885714729499069286593698777113907879332554209736653679474028316464493192062972874319626623316763537266681767610340623614648701699868901159785995894014509520642548386447251984766543776759949169049134947575625384064448900019906754502662096668908517457172'

test1 = '12345678'
test2 = '80871224585914546619083218645595'
test3 = '19617804207202209144916044189917'
test4 = '69317163492948606335995924319873'


def phase(num=''):
    num_list = []
    for iteration in range(1, len(num)+1):
        iteration_total = 0
        pattern = []
        for c0 in range(0, iteration):
            pattern += [0]
        for c0 in range(0, iteration):
            pattern += [1]
        for c0 in range(0, iteration):
            pattern += [0]
        for c0 in range(0, iteration):
            pattern += [-1]

        index0 = 0
        this_total = 0
        print(pattern)
        for digit in range(0, len(num)):
            if index0 < len(pattern)-1:
                index0 += 1
            else:
                index0 = 0
            iteration_total += int(num[digit])*pattern[index0]
            this_total += int(num[digit])*pattern[index0]
            if digit % (len(num) / 10000) == 0:
                print(this_total)
                this_total = 0
                input('')

        num_list += [str(iteration_total)[-1]]

    num_str = ''.join(num_list)
    return num_str


number = signal * 10000
print(len(signal))
for c in range(0, 100):
    number = phase(number)
    print(number)

print(number)
