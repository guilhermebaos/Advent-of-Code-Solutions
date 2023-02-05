n = -3.5
m = 5


def factorial(n: float):
    den = 1
    for i in range(1, m + 1):
        den *= (n + i)

    num = den
    for i in range(1, n + 1):
        num *= i
