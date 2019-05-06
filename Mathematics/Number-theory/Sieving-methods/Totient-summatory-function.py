''' The Euler"s totient summatory function Phi. '''

#########################################################################

import itertools as it

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

# sieve of phi
def euler_phi(n, primes):
    phi = [1] * (n+1); phi[0] = 0
    for p in primes:
        phi[p] = p - 1
    for i in range(2, n+1):
        for p in primes:
            if i*p > n:
                break
            if i % p == 0:
                phi[i * p] = phi[i] * p
                break
            else:
                phi[i * p] = phi[i] * phi[p]
    return phi


# roughly O(n^2/3)
def Phi(n):
    ''' Returns two arrays Phi1, Phi2:
            Phi1[i] = Phi(i) for i <= sqrt(n)
            Phi2[i] = Phi(n // i) for i <= sqrt(n)
     '''
    L = int(n**0.62)
    phis = euler_phi(L, fast_prime_sieve(L))
    Phi1 = list(it.accumulate(phis))    # Phi1[i] = Phi(i)
    Phi2 = [0] * (n//L+1)               # Phi2[i] = Phi(n//i)
    for j in range(n//L, 0, -1):
        k = n//j
        ksqrt = int(k**0.5)
        v = 0
        for i in range(ksqrt, 1, -1):
            kdivi = k//i
            mult = kdivi - k//(i+1)
            if kdivi > L:
                v -= Phi2[n//kdivi]
            else:
                v -= Phi1[kdivi]
            v -= mult*Phi1[i]
        mult = k - k//2
        v -= mult*Phi1[1]
        if k//ksqrt == ksqrt:
            v += Phi1[ksqrt]
        Phi2[j] = v + k*(k+1)//2
    return Phi1, Phi2

#########################################################################




'''
Approximate runtime (Computing pi(n)):
_______________________________________________
        n              time
       100             1e-4s
      10**4            1e-3s
      10**6            0.015s
      10**8            0.06s
      10**10           5s
'''
