def calc_rec(n):
    k = 2
    S = 1 / 2
    while k < n:
        k += 1
        S += (-1) ** k * ((n - 1) / n)
    return S


def gen_rec(n):
    k = 2
    S = 1 / 2
    yield S
    while k < n:
        k += 1
        S += (-1) ** k * ((n - 1) / n)
        yield S


if __name__ == '__main__':
    for i in gen_rec(99):
        print(i)
        
    print(calc_rec(100))
