def calc_rec(n):
    k = 2
    S = 1 / 2
    while k < n:
        k += 1
        S += 1 / ((k - 1) * k)
    return S


def gen_rec(n):
    k = 2
    S = 1 / 2
    yield S
    while k < n:
        k += 1
        S += 1 / ((k - 1) * k)
        yield S


if __name__ == '__main__':
    print(calc_rec(10000000))
