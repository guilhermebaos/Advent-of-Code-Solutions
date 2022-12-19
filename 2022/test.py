class BEE:

    def __init__(self):
        self.total = 0


    def aumenta(self):
        self.total += 1


a = {
    "AA": BEE(),
    "BB": BEE()
}

b = a.copy()
b["AA"].aumenta()
b["AA"].aumenta()
b["AA"].aumenta()

print(a["AA"].total)
print(b["AA"].total)