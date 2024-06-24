def calc_rec(n):
    D2 = 3
    D1 = 7
    k = 3
    while k < n:
        D = 3 * D1 - 2 * D2
        D2 = D1
        D1 = D
        k += 1
    return D1


def gen_rec(n):
    D2 = 3
    D1 = 7
    yield D2
    yield D1
    k = 3
    while k < n:
        D = 3 * D1 - 2 * D2
        D2 = D1
        D1 = D
        k += 1
        yield D1
