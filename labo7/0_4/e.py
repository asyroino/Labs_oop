def calc_rec(a, n):
    D2 = a
    D1 = a ** 2 - 1
    k = 3
    while k < n:
        D = a * D1 - D2
        D2 = D1
        D1 = D
        k += 1
    return D1


def gen_rec(a, n):
    D2 = a
    D1 = a ** 2 - 1
    yield D2
    yield D1
    k = 3
    while k < n:
        D = a * D1 - D2
        D2 = D1
        D1 = D
        k += 1
        yield D1


if __name__ == '__main__':
    for i in gen_rec(3, 50):
        print(i)
