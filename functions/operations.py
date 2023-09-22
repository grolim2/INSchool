def soma(v1, v2):
    return v1 + v2


def subtracao(v1, v2):
    return v1 - v2


def divisao(v1, v2):
    while True:
        if v2 == 0:
            v2 = float(input('****O divisor é igual a zero. Digite outro valor.****\n'))
            continue
        else:
            return v1 / v2


def multi(v1, v2):
    return v1 * v2


def exp(v1, v2):
    return v1 ** v2