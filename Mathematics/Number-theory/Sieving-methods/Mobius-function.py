''' Sieve for the Mobius function. '''

#########################################################################


def fast_prime_sieve(n):
    """
        Input n>=6, Returns a list of primes, 2 <= p <= n
        Taken from: https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/
    """
    n += 1
    n, correction = n-n%6+6, 2-(n%6>1)
    sieve = [True] * (n//3)
    for i in range(1,int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      k*k//3      ::2*k] = [False] * ((n//6-k*k//6-1)//k+1)
        sieve[k*(k-2*(i&1)+4)//3::2*k] = [False] * ((n//6-k*(k-2*(i&1)+4)//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]


def mobius(n, primes):
    mu = [1 for _ in range(n+1)]
    for p in primes:
        for j in range(p, n+1, p):
            mu[j] *= -1
        for j in range(p*p, n+1, p*p):
            mu[j] = 0
    return mu

#########################################################################








'''
Approximate runtime (Computing mobius(n), including primes):
_______________________________________________
        n              time
       100             1e-4s
      10**4            0.008s
      10**6            0.08s
      10**8            11s
'''
