''' Legendre symbol indicates whether a is a quadratic residue modulo p '''

def legendre_symbol(a, p):
    ls = pow(a, (p - 1)//2, p)
    return -1 if ls == p - 1 else ls


'''    Verification test    '''
if __name__ == "__main__":
    assert [legendre_symbol(a, 23) for a in range(1, 31)] == [int(x) for x in \
    "1 1 1 1 -1 1 -1 1 1 -1 -1 1 1 -1 -1 1 -1 1 -1 -1 -1 -1 0 1 1 1 1 -1 1 -1".split()]
