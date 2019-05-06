''' Solves a system of congruences using the C.R.T.
            [ x == a_i   mod m_i ]
'''


#########################################################################

# O(|m| log(max(m) + max(a)))
def chinese_remainder(m, a):
    '''
        m - modulos, a - coefficients (arrays)
        * m have to be mutually COPRIME *

    '''
    res, prod = 0, 1
    for m_i in m:
        prod *= m_i
    for m_i, a_i in zip(m, a):
        p = prod // m_i
        res += a_i * modinv(p, m_i) * p
    return res % prod



# O(log(a+b))
def egcd(a, b):
    ''' Extended Euclidian algorithm. '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    ''' Finds modular inverse of a modulo m.  '''
    while a < 0:
        a += m
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

#########################################################################




'''    Verification test    '''
if __name__ == '__main__':
    m = [11, 16, 21, 25]
    a = [6, 13, 9, 19]
    x = chinese_remainder(m, a)
    for mm, aa in zip(m, a):
        assert(x%mm == aa)

    print('    The solution of: ')
    for mm, aa in zip(m, a):
        print('         x == {:<3d}    mod {:d}'.format(aa, mm))
    print('    is x = {:d}'.format(x))
