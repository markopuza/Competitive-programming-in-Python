'''
    Utility functions for working with continued fractions representations.
'''




#########################################################################

def continued_fraction_to_fraction(cf):
    ''' Converts a continued fraction into fraction. '''
    cf += [0,0]
    convergents = [(cf[0],1), (cf[1]*cf[0] + 1, cf[1])]
    for i in range(2, len(cf)):
        h = cf[i]*convergents[-1][0] + convergents[-2][0]
        k = cf[i]*convergents[-1][1] + convergents[-2][1]
        convergents.append((h, k))
    return convergents[-1]

def fraction_to_continued_fraction(f, precision=100):
    ''' Converts a fraction into continued fraction. '''
    n, d = f
    cf = []
    for _ in range(precision):
        cf.append(n//d)
        n, d = d, n - cf[-1]*d
        if not d:
            break
    return cf


def continued_fraction_square_root(n, precision=100):
    '''
        Given an integer n, returns continued fraction for \sqrt(n).
    '''
    # perfect square
    if int(n ** 0.5) == n ** 0.5:
        return [int(n ** 0.5)]

    m, d, a = 0, 1, int(n ** 0.5)
    cf = [a]
    for _ in range(precision):
        m = d*a - m
        d = (n - m*m)//d
        a = int((n ** 0.5  + m)/d)
        cf.append(a)
    return cf


def best_approximation(cf, den_bound=10**12):
    ''' Given a continued fraction, returns its best rational approximation in which
        the denominator is <= to the den_bound.
        For details see Wikipedia article on continued fractions.
    '''
    best = (-1, -1)
    convergents = [(cf[0],1), (cf[1]*cf[0] + 1, cf[1])]
    for i in range(2, len(cf)):
        h = cf[i]*convergents[-1][0] + convergents[-2][0]
        k = cf[i]*convergents[-1][1] + convergents[-2][1]

        startm = cf[i]//2 + 1 if cf[i]&1 else cf[i]//2
        if not cf[i]&1:
            ln, ld = continued_fraction_to_fraction(cf[1:i+1][::-1])
            rn, rd = continued_fraction_to_fraction(cf[i:])
            if not ln * rd > rn * ld:
                startm += 1

        for m in range(startm, cf[i]+1):
            sh = m*convergents[-1][0] + convergents[-2][0]
            sk = m*convergents[-1][1] + convergents[-2][1]
            if sk <= den_bound:
                best = (sh, sk)
            else:
                return best

        convergents.append((h, k))
    return best


#########################################################################







'''    Verification test    '''
if __name__ == "__main__":
    from fractions import Fraction
    print('Test 1:')
    for cf in [[0], [-1], [5], [1, 2], [1, 2, 3], [4, 2, 6, 7]]:
        print('    Continued fraction: {:<12s}  ->  {:s}'.format(str(cf), str(Fraction(*continued_fraction_to_fraction(cf)))))
    print('')

    print('Test 2: ')
    for f in [(0, 1), (-1, 1), (5, 1), (3, 2), (10, 7), (415, 93)]:
        print('    Fraction: {:<12s}  ->  {:s}'.format(str(Fraction(*f)), str(fraction_to_continued_fraction(f))))
    print('')

    print('Test 3: ')
    for i in list(range(10)) + [19]:
        print('    N = {:<5d}  ->  sqrt N = {:s}'.format(i, str(continued_fraction_square_root(i, 10))))
    print('')

    print('Test 4: ')
    cf = [0, 1, 5, 2, 2]
    f = continued_fraction_to_fraction(cf)
    print('    {:s} = {:s} = {:.5f}'.format(str(cf), str(Fraction(*f)), f[0]/f[1]))
    for i in range(1, 35):
        print('    Best rat. approx. with denominator bound {:d}:  {:s}'.format(i, str(Fraction(*best_approximation(cf, i)))))
