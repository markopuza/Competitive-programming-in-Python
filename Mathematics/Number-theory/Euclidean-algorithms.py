'''
    Euclidean algorithms.
'''


#########################################################################

def egcd(a, b):
    ''' Extended Euclidian algorithm. '''
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        # x * a + y * b = g
        return (g, x - (b // a) * y, y)

_gcd = lambda a, b: a+b if a==0 or b==0 else gcd(b, a % b)

def gcd(a, b):
    if a==0 or b == 0:
        return a+b
    return gcd(b, a % b)


#########################################################################
