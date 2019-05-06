''' Detects cycles in a given iterator. '''


#########################################################################

def cycle_length(f, x0, nmax=None):
    ''' Given iterator f, returns lambda, mu.

     Lambda is the length of the cycle, mu is the number of iterations before the cycle.
    '''
    nmax = int(nmax or 0)

    # main phase: search successive powers of two
    power = lam = 1
    tortoise, hare, i = x0, f(x0), 0
    while tortoise != hare and (not nmax or i < nmax):
        i += 1
        if power == lam:   # time to start a new power of two?
            tortoise = hare
            power <<= 1
            lam = 0
        hare = f(hare)
        lam += 1
    if nmax and i == nmax:
        return nmax, None

    # Find the position of the first repetition of length lambda
    mu = 0
    tortoise = hare = x0
    for i in range(lam):
        hare = f(hare)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(hare)
        mu += 1
    return lam, max(mu-1, 0)



#########################################################################









'''    Verification test    '''
if __name__ == '__main__':
    f = lambda x: x-1 if x >= 10000 else (x+1)%10000
    x0 = 10000 + 123
    assert cycle_length(f, x0) == (10000, 123)
