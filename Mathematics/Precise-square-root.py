'''
    Calculates square root of a non-square number n up to arbitrary precision.
'''




#########################################################################

def precise_square_root(n, precision=100):
    ''' . '''
    a, b = 5 * n, 5
    while len(str(b)) < precision + 5:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = 100 * (b // 10) + 5
    sb =  str(b)
    int_len = len(str(int(n**.5)))
    return (sb[:int_len] + '.' + sb[int_len:])[:precision]

#########################################################################





'''    Verification test    '''
if __name__ == "__main__":
    for n in [128937, 16]:
        print('    Number {:d}'.format(n))
        print('        Precise square root: {:s}'.format(precise_square_root(n, 30)))
        print('        Float square root  : {:.19f}'.format(n ** 0.5))
        print()
