def calc_rec(x, n):
    k = 0
    a = 1
    while k < n:
        k += 1
        a = x ** 2 / (2 * k * (2 * k - 1)) * a
    return a


def gen_rec(x, n):
    k = 0
    a = 1
    yield a
    while k < n:
        k += 1
        a = x ** 2 / (2 * k * (2 * k - 1)) * a
        yield a


if __name__ == '__main__':
    print(calc_rec(3, 100))

    for i in gen_rec(3, 50):
        print(i)
