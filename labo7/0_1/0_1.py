def calc_rec(n):
    a = 2 ** 0.5
    k = 0
    while k < n:
        a = (2 + a) ** 0.5
        k += 1
    return a


def gen_rec(n):
    a = 2 ** 0.5
    yield a
    k = 0
    while k < n:
        a = (2 + a) ** 0.5
        k += 1
        yield a


if __name__ == '__main__':
    print(calc_rec(100))
    
    for i in gen_rec(50):
        print(i)
