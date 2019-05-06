'''
Computes the Bernoulli numbers | https://en.wikipedia.org/wiki/Bernoulli_number

Note that the second term is subject to a sign convention B_1 = \pm 1/2
'''

#########################################################################
from fractions import Fraction

def bernoulli():
    ''' Generator of Bernoulli numbers. '''
    ber, m = [], 0
    while 1:
        ber.append(Fraction(1, m+1))
        for j in range(m, 0, -1):
            ber[j-1] = j*(ber[j-1] - ber[j])
        yield ber[0]
        m += 1
##########################################################################







'''    Verification test    '''
if __name__ == "__main__":
    bernoullis = [inum for inum in zip(range(61), bernoulli())]

    for n, b_n in bernoullis:
        print('B[{:d}] = {:s}'.format(n, str(b_n)))

'''
Approximate runtime (Computing B[n]):
_______________________________________________
        n              time
       100             0.05s
       200             0.28s
       300             0.84s
       500             4.00s
'''
