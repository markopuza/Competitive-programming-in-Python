''' Sieve for the divisor functions. '''

#########################################################################

def num_of_divisors(n):
    nd = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            nd[j] += 1
    return nd


def sum_of_divisors(n):
    sd = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(i, n+1, i):
            sd[j] += i
    return sd

#########################################################################





'''    Verification test    '''
if __name__ == '__main__':
    from sympy import divisors
    from random import randint
    for _ in range(20):
        n = randint(1, 10**4)
        d = divisors(n)
        assert num_of_divisors(n)[-1] == len(d)
        assert sum_of_divisors(n)[-1] == sum(d)

'''
Approximate runtime (Computing num_of_divisors(n), sum_of_divisors(n)):
_______________________________________________
        n              time
       100             1e-4s
      10**4            0.004s
      10**6            0.08s
      10**8            22s
'''
