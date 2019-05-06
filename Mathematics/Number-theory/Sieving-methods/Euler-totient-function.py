''' Sieve for the Euler totient function. '''

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


def euler_phi_2(n):
    phi = list(range(n+1))
    for p in range(2, n+1, 2):
        phi[p] >>= 1
    for p in range(3, n+1, 2):
        if phi[p] == p:
            phi[p] -= 1
            for j in range(2*p, n+1, p):
                phi[j] -= phi[j] // p
    return phi

#########################################################################






'''    Verification test    '''
if __name__ == "__main__":
    assert euler_phi_2(12312)[-1] == 3888

'''
Approximate runtime (Computing euler_phi_2(n)):
_______________________________________________
        n              time
       100             1e-4s
      10**4            0.01s
      10**6            0.045s
      10**8            6.8s
'''
