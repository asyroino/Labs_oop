def calc_rec(n):
    if n % 2 == 0:
        return 1
    else:
        return 0


def gen_rec(n):
    D2 = 0
    D1 = 1
    yield D2
    yield D1
    k = 2
    while k < n:
        D = 0 * D1 + D2
        D2 = D1
        D1 = D
        k += 1
        yield D


if __name__ == '__main__':
    for i in gen_rec(50):
        print(i)
